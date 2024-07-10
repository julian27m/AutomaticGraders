# Base image
FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

# Copy grader files
COPY grader.py /autograder/source/
COPY util.py /autograder/source/

# Set the working directory
WORKDIR /autograder/source

# Set the entrypoint
ENTRYPOINT ["python3", "grader.py"]
