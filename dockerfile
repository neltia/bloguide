FROM ubuntu:22.04

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

# net-tools
RUN apt-get update
RUN apt-get install -y vim

# python packages install
RUN apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential -y
RUN python3 -m pip install --upgrade pip

# lib install
RUN pip install --no-cache-dir -r requirements.txt

# port number
EXPOSE 8080

# start command
CMD ["sleep", "infinity"]