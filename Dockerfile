# Use a Linux base image
FROM ubuntu:latest

# Install Google Chrome dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    apt-transport-https \
    --no-install-recommends

# Download and install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Install Python and pip
RUN apt-get install -y python3 python3-pip

# Install dependencies for Selenium and Chrome driver
RUN apt-get install -y \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libfontconfig1 \
    libnss3 \
    libasound2 \
    libxtst6 \
    libxss1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm-dev \
    fonts-liberation

# Copy your web scraping code to the Docker image
COPY . /app/

# Set the working directory
WORKDIR /app

# Install Python packages required for your code
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Run your web scraping code
CMD ["python3", "src/_03_app.py"]
