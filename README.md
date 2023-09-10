# Flask Application with MongoDB Docker Setup

This repository contains a Flask application that uses MongoDB as its database. The application is designed to run within a Docker container. Follow the steps below to set up and run the application.

## Prerequisites

- Docker installed on your system: [Get Docker](https://docs.docker.com/get-docker/)

## Getting Started

1. Clone this repository to your local machine.

```bash
git clone https://github.com/Naman16rajani/Corider-Task
cd your-repo
```

2. Create a `.env` file in the root directory of the project to store the MongoDB URI and database name. Replace `<YOUR_MONGO_URI>` and `<YOUR_DATABASE_NAME>` with your MongoDB details.

```env
MONGO_URI=<YOUR_MONGO_URI>
DATABASE_NAME=<YOUR_DATABASE_NAME>
```

3. Build the Docker image.

```bash
docker build -t Corider-Task .
```

## Running the Application

4. Start the Docker container.

```bash
docker run -p 5000:5000 --env-file .env Corider-Task
```

The Flask application and MongoDB server will start within the Docker container.

## Accessing the Application

Visit [http://localhost:5000](http://localhost:5000) in your web browser to access the Flask application.

## Stopping the Application

To stop the Docker container, use the following command:

```bash
docker stop $(docker ps -q --filter ancestor=Corider-Task)
```

## Notes

- The `.env` file should never be committed to version control as it contains sensitive information.
- Ensure your MongoDB server is running and accessible before starting the Docker container.

---

Replace `<YOUR_MONGO_URI>` and `<YOUR_DATABASE_NAME>` with your actual MongoDB connection URI and database name. Also, be sure to customize the repository and image names to match your project.

This README provides a basic guide for setting up and running your Flask application with MongoDB in a Docker container. Feel free to add more detailed instructions, troubleshooting tips, or any additional information specific to your application.
