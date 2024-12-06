# Dockerfile

# lightweight python image
FROM python:3.9-slim

# set working directory
WORKDIR /app

# install necessary build tools
RUN apt-get update && apt-get install -y \
    postgresql-client \
    iputils-ping \
    gcc \
    g++ \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# copy requirements files first for Docker caches the dependency installation layer separately.
COPY requirements.txt /app/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# copy the rest of project files
COPY . /app

# expose streamlit's default port
EXPOSE 8501

# Default command to run the app
CMD ["streamlit", "run", "app_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
