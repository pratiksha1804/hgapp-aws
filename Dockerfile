FROM python:3.6-slim-buster
RUN python -m venv /opt/venv 
ENV PATH="/opt/venv/bin:$PATH" \
 OAUTHLIB_INSECURE_TRANSPORT=1 
RUN echo $OAUTHLIB_INSECURE_TRANSPORT

# Copying the app folder of Project to the Container Work Directory /app
WORKDIR /hgapp-aws
COPY . .

# Installing Build Essentials for Compiling and Building of Python Packages
RUN apt update
RUN apt-get install -y build-essential

# Installing Python Packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposing Port
EXPOSE 5002
# Running the Python App
CMD ["python3", "app.py"]
