# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/app:/usr/local/lib/python3.11/site-packages"

# Set work directory
WORKDIR /app

# Install system dependencies and clean up in the same layer to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install PraisonAI and FLAML with required extras
RUN pip install --no-cache-dir --upgrade \
    "praisonai[call]" 

# Create a non-root user and switch to it
RUN useradd -m -r appuser && chown -R appuser /app
USER appuser

# Expose the port the app runs on
EXPOSE 8090

# Run the application
CMD ["praisonai", "call", "--public"]
