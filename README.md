#Flask App on ECS

This repository contains a simple Flask web application designed to be deployed on AWS Elastic Container Service (ECS). It demonstrates how to containerize a Python application and run it in a cloud environment.

## Features

- **Basic Flask Application**
  - `/` endpoint: Welcome message.
  - `/health` endpoint: Health check route.
- **Containerization**
  - Dockerfile provided to containerize the application.
- **Minimal Setup**
  - Lightweight dependencies.

## Prerequisites

- Python 3.7 or above
- Docker installed
- AWS CLI configured (optional, for deployment)

## Project Structure

```
flask-app-ecs/
app.py              # Main Flask application file
run.py              # Entry point for the Flask app
requirements.txt    # Python dependencies
Dockerfile          # Dockerfile for containerization
README.md           # Project documentation
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/purveshsune/flask-app-ecs.git
   cd flask-app-ecs
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate    # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app locally:
   ```bash
   python run.py
   ```

   The app should be accessible at `http://<YOUR_IP-ADDRESS>:5000/`

## Dockerization

1. Build the Docker image:
   ```bash
   docker build -t flask-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 5000:5000 flask-app
   ```

3. Access the app in your browser:
   - [http://localhost:5000](http://localhost:5000)

## AWS ECS Deployment

To deploy this app to AWS ECS:

1. Push the Docker image to Amazon Elastic Container Registry (ECR).
2. Configure an ECS cluster and service.
3. Set up task definitions referencing the Docker image.
4. Deploy and monitor via the AWS Management Console or CLI.

## Endpoints

- `/` - Returns: `Hey, welcome to DevOps Zero To Hero`
- `/health` - Returns: `Server is up and running`

## Technologies Used

- **Flask**: Python-based web framework.
- **Docker**: For containerization.
- **AWS ECS**: For deployment (optional).

## Author

Created by Purvesh Sune https://github.com/purveshsune

