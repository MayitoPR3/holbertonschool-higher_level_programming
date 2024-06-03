# Use the same Alpine base image as the previous exercise
FROM alpine:latest

# Install curl package
RUN apk add --no-cache curl

# Copy the configuration file to the /app directory in the container
COPY config.txt /app/config.txt

# Specify the default command to run when the container starts
CMD ["sh"]
