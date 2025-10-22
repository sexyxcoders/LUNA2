# Use slim Python 3.10 base image
FROM python:3.10-slim-bullseye

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies: FFmpeg, curl, Node.js (LTS)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    gnupg \
    build-essential \
    aria2 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 19 (latest)
RUN curl -fsSL https://deb.nodesource.com/setup_19.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

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

# Start bot
CMD ["python", "-m", "Alya"]