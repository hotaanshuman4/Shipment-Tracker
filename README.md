![Chatbot Demo](https://github.com/hotaanshuman4/Shipment-Tracker-Chatbot/blob/f9e5e916aa93d7a5ae2e1707baa1d51163df265f/Screenshot%20(67).png)
# Shipment Tracking Chatbot

Welcome to the Shipment Tracker Chatbot! This project is a conversational AI tool designed to help users track shipments seamlessly through a chatbot interface. Built with modern technologies, it provides real-time updates and an intuitive user experience for managing shipment tracking.

## Overview
The Shipment Tracker Chatbot allows users to input tracking numbers and receive real-time updates on their shipment status. Whether you're a business owner managing multiple deliveries or an individual waiting for a package, this chatbot simplifies the process with natural language interaction.

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

## License

This project is licensed under the MIT License. See the  file for details

## Contact

For questions or suggestions, reach out to the project maintainer:
GitHub: hotaanshuman4
Email: your-email@example.com
