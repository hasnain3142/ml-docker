# ML-DOCKER

This repository contains a simple FastAPI application for text summarization using the Hugging Face Transformers library. The application is containerized using Docker for easy deployment and scalability.

## Files in the Repository

1. **main.py**: The main FastAPI application file that defines the API endpoints for the summarization model.


2. **model.py**: Contains the summarization model implementation using the Hugging Face Transformers library.

3. **requirements.txt**: Lists the Python dependencies required for running the FastAPI application.

4. **Dockerfile**: The Dockerfile for building the Docker image. It sets up a Python environment, installs dependencies, and runs the FastAPI application.

5. **.github/workflows/docker-image.yml**: GitHub Actions workflow file for building and pushing the Docker image on each push to the main or releases branch.

## Running the Application

### 1. Virtual Environment Setup

```bash
# Create a virtual environment (Python 3.11)
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the FastAPI Application Locally

```bash
# Run the FastAPI application locally
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be accessible at [http://localhost:8000](http://localhost:8000).

### 3. Docker Setup and Run

```bash
# Build the Docker image
docker build -t your_docker_username/ml-docker:latest .

# Run the Docker container
docker run -p 8000:8000 your_docker_username/ml-docker:latest
```

The API will be accessible at [http://localhost:8000](http://localhost:8000).

## GitHub Actions Workflow

The provided GitHub Actions workflow (`docker-image.yml`) automates the process of building and pushing the Docker image to Docker Hub on each push to the main or releases branch. It uses Docker secrets for authentication.

Ensure you have the following secrets set in your GitHub repository:

- `DOCKER_LOGIN`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

## Note

Make sure to replace placeholders like `your_docker_username` with your actual Docker Hub username. Additionally, customize the summarization model in the `model.py` file as needed.

Feel free to reach out if you have any questions or encounter issues!