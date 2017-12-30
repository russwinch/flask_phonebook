# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /appd

# Copy the current directory contents into the container at /app
ADD . /appd

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 4000

# Define environment variable
ENV FLASK_CONFIG development

# Run app.py when the container launches
CMD ["python", "run.py"]