# Dockerfile
FROM httpd:latest
FROM archlinux/archlinux

EXPOSE 5432

RUN pacman -Sy --noconfirm apache || \ 
    apk --no-cache add apache2-utils || \
    apt-get install apache2-tools