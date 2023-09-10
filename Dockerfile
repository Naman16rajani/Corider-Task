# Base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 5000

# Install MongoDB client
RUN apt-get update && apt-get install -y mongodb-clients

# Set the environment variables for MongoDB connection
ENV MONGO_HOST=mongodb
ENV MONGO_PORT=27017

# Set the command to run the MongoDB service
CMD mongod --bind_ip_all --smallfiles --nojournal & python app.py
