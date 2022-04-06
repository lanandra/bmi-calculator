# Dockerfile

# Get base image
FROM python:3.9.10-slim-buster

# Copy and install requirements
COPY requirements.txt /
RUN pip install -r requirements.txt

# Copy remaining files and set workdir
COPY . /usr/local/lib/python3.9/site-packages/bmi-calculator
WORKDIR /usr/local/lib/python3.9/site-packages/bmi-calculator

# Run application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
