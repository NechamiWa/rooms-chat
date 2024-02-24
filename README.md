# Flask Chat Server Dockerized

## Description:

This repository contains the source code for a simple Flask chat server, packaged as a Docker image for easy deployment. The chat server allows users to create chat rooms, send messages to existing rooms, and view messages in real-time.

## Features:
- Create chat rooms: Users can create new chat rooms by navigating to the desired room URL.
- Send messages: Users can send messages to chat rooms by entering their username and message text in the provided form.
- Real-time updates: Messages are displayed in real-time, allowing users to see new messages as they are sent.
- Dockerized: The chat server is packaged as a Docker image, making it easy to deploy and run in various environments.

## Technologies:
- Flask: The chat server is built using the Flask web framework, providing a lightweight and flexible foundation for building web applications.
- Docker: The chat server is Dockerized, allowing for easy deployment and scalability across different environments.
- JSON data storage: Chat room data and messages are stored in a JSON file, providing a simple and portable data storage solution.

## Usage:


1. Clone the repository: `git clone https://github.com/yourusername/flask-chat-server.git`


2. Build the Docker image: `docker build -t flask-chat-server .`


3. Run the Docker container: `docker run -d -p 5000:5000 flask-chat-server`


4. Access the chat server: Open a web browser and navigate to `http://localhost:5000` to access the chat server.

## Contributing:
Contributions to the project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.



#### For more information, please visit the project repository: https://github.com/NechamiWa