# Use the official Python 3.12 image with support for SQLite
FROM python:3.12-slim

# Install SQLite and other dependencies
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Set the working directory
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Command to run your application
CMD ["python", "manage.py", "runserver"]
