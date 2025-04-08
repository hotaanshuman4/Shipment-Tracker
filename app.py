from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import random
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# AfterShip API Configuration
AFTERSHIP_API_KEY = 'apik_rXEKIBH4c4xiKdixrexQGCDHtHCBYM'
AFTERSHIP_API_URL = 'https://api.aftership.com/v4/trackings'

# Delivery Partners
DELIVERY_PARTNERS = [
    "Amazon Logistics",
    "DHL Express",
    "BlueDart",
    "Ekart",
    "FedEx",
    "DTDC",
    "Delhivery",
    "XpressBees"
]

# Tracking Statuses with their descriptions
TRACKING_STATUSES = {
    "In Transit": [
        "Package is in transit to the next facility",
        "Package is moving through our network",
        "Package is on its way to the destination"
    ],
    "Out for Delivery": [
        "Package is out for delivery with the courier",
        "Courier is on the way to deliver your package",
        "Package is in the final delivery stage"
    ],
    "Delivered": [
        "Package has been successfully delivered",
        "Delivery completed",
        "Package has reached its destination"
    ],
    "In Warehouse": [
        "Package is being processed at our warehouse",
        "Package is in sorting facility",
        "Package is being prepared for shipment"
    ],
    "At Nearest Hub": [
        "Package has arrived at the local delivery hub",
        "Package is at the nearest distribution center",
        "Package is ready for local delivery"
    ]
}

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('chatbot'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('chatbot'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/chatbot')
@login_required
def chatbot():
    return render_template('chatbot.html')

def generate_tracking_response(tracking_number):
    # Generate a deterministic but seemingly random status based on tracking number
    status_seed = sum(ord(c) for c in tracking_number)
    status_index = status_seed % len(TRACKING_STATUSES)
    status = list(TRACKING_STATUSES.keys())[status_index]
    
    # Select a random description for the status
    description = random.choice(TRACKING_STATUSES[status])
    
    # Generate a delivery partner based on tracking number
    partner_seed = sum(ord(c) for c in tracking_number)
    delivery_partner = DELIVERY_PARTNERS[partner_seed % len(DELIVERY_PARTNERS)]
    
    # Generate a realistic timestamp
    current_time = datetime.now()
    if status == "Delivered":
        timestamp = current_time - timedelta(hours=random.randint(1, 24))
    elif status == "Out for Delivery":
        timestamp = current_time - timedelta(hours=random.randint(1, 3))
    elif status == "In Transit":
        timestamp = current_time - timedelta(hours=random.randint(4, 48))
    else:
        timestamp = current_time - timedelta(hours=random.randint(1, 72))
    
    # Generate expected delivery date
    if status != "Delivered":
        expected_delivery = current_time + timedelta(days=random.randint(1, 5))
        expected_delivery_str = expected_delivery.strftime("%B %d, %Y")
    else:
        expected_delivery_str = "Already delivered"
    
    # Generate location based on status
    locations = {
        "In Transit": ["Mumbai Hub", "Delhi Distribution Center", "Bangalore Warehouse"],
        "Out for Delivery": ["Local Delivery Center", "Nearest Sorting Facility"],
        "Delivered": ["Final Destination", "Delivery Location"],
        "In Warehouse": ["Main Sorting Facility", "Primary Distribution Center"],
        "At Nearest Hub": ["Local Hub", "City Distribution Center"]
    }
    location = random.choice(locations[status])
    
    # Format the message with line breaks for better readability
    message = (
        f"📦 Tracking Status: {status}\n\n"
        f"📝 Description: {description}\n\n"
        f"🚚 Delivery Partner: {delivery_partner}\n\n"
        f"📍 Current Location: {location}\n\n"
        f"🕒 Last Update: {timestamp.strftime('%B %d, %Y %I:%M %p')}\n\n"
        f"📅 Expected Delivery: {expected_delivery_str}"
    )
    
    return {
        'status': 'success',
        'message': message
    }

@app.route('/track', methods=['POST'])
@login_required
def track_shipment():
    tracking_number = request.json.get('tracking_number')
    
    # Check if the input contains numeric data
    if any(char.isdigit() for char in tracking_number):
        # If it contains numbers, treat it as a tracking number and return tracking details
        return jsonify(generate_tracking_response(tracking_number))
    else:
        # If it doesn't contain numbers, return a message asking for delivery-related queries
        return jsonify({
            'status': 'error',
            'message': "I didn't understand, ask related to delivery query"
        })

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000) 