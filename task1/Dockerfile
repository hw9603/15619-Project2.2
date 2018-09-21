# Complete this Dockerfile to launch a Nginx server
# Ubuntu Linux as the base image
FROM ubuntu:16.04

# Install the packages
RUN apt-get update && \
    apt-get upgrade && \
    apt-get -y install nginx

EXPOSE 80

# CMD ["start"]

ADD index.html /var/www/html/

ENTRYPOINT ["nginx", "-g", "daemon off;"]
