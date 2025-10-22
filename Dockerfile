# Base image with Python 3.10 and Node.js 19
FROM nikolaik/python-nodejs:python3.10-nodejs19

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update Debian sources and install dependencies
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i '/security.debian.org/d' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg aria2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY . .

# Expose port (optional for webhooks)
EXPOSE 5000

# Run the bot
CMD ["python", "-m", "Alya"]