FROM ubuntu:22.04

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

# lib install
RUN pip install --no-cache-dir -r requirements.txt

# docker install
RUN apt install -y docker.io

# port number
EXPOSE 9001

# start command
CMD ["bash", "/app/start.sh"]
