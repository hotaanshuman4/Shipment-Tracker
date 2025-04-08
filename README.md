# Shipment Tracking Chatbot

A modern, containerized chatbot application for tracking shipments with a beautiful UI.

## Features

- User authentication (login/register)
- Realistic shipment tracking responses
- Beautiful, responsive UI
- Docker containerization
- Multiple delivery partners
- Detailed tracking information

## Running with Docker

1. Build the Docker image:
```bash
docker build -t shipment-tracker .
```

2. Run the container:
```bash
docker run -p 5000:5000 shipment-tracker
```

3. Access the application at http://localhost:5000

## Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access the application at http://localhost:5000

## Tracking Information

The chatbot provides realistic tracking information including:
- Current status (In Transit, Out for Delivery, Delivered, etc.)
- Delivery partner (Amazon, DHL, BlueDart, etc.)
- Current location
- Last update timestamp
- Expected delivery date 