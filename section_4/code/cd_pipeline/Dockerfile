# base image
FROM alpine:3.7

RUN echo "https://alpine.global.ssl.fastly.net/alpine/v3.7/main" > /etc/apk/repositories
RUN echo "https://alpine.global.ssl.fastly.net/alpine/v3.7/community" >> /etc/apk/repositories
RUN apk update

# Install python 3 and pip
RUN apk add --update python3

# Install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Tell the port number the container should expose
EXPOSE 5000

# Run the application
CMD ["python3", "/usr/src/app/app.py"]
