# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app


# Make port 8000 available to the world outside this container
EXPOSE 8080


# Run app.py when the container launches
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8080"]