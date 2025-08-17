FROM python:3.10-slim

# Set working directory
WORKDIR /app
# Install system dependencies first (if needed)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt



# Copy app
COPY . .

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
