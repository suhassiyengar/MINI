# MINI

# Remote Device Control System (IoT Simulation)

## Description
This project implements a remote device control system that simulates an IoT environment using a client-server architecture. A central controller communicates with multiple device clients over TCP sockets, allowing commands to be issued remotely through a web-based interface built using Flask.

## Features
- Multi-device communication using TCP sockets  
- Token-based authentication between controller and devices  
- Web-based control panel using Flask  
- Command execution such as opening websites and checking status  
- JSON-based communication protocol  
- Real-time response from devices  

## Architecture
Web Browser (Frontend)  
→ Flask Server (app.py)  
→ Controller (controller.py)  
→ Device Clients (device_client.py)  

## How It Works
1. Device clients connect to the controller using sockets  
2. Each device authenticates using a predefined token  
3. The user sends commands through the web interface  
4. Flask forwards the command to the controller  
5. The controller sends the command to connected devices  
6. Devices execute the command and return a response  
7. The response is displayed on the web interface  

## Commands Supported
- OPEN_GOOGLE → Opens Google on the device  
- OPEN_YOUTUBE → Opens YouTube on the device  
- STATUS → Returns device status  

## Project Structure
