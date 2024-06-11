# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Download and install the Spacy language model
RUN python -m spacy download de_core_news_sm

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 8005

# Command to run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]