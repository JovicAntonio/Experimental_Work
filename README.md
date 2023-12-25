# Infrastructure for large-scale data

## 1. Introduction

This is a project meant as an experimental work for University course "Infrastructure for large-scale data".

## 2. Installation

To download repository, You can either download a zip file or clone repository with command:

```bash
git clone https://github.com/JovicAntonio/Experimental_Work.git
```

You will also need [Docker](https://www.docker.com/) which you can download for Windows by installing their installer, or for Linux. Depending of Linux distribution, it will either be Ubuntu, which is Debian, or any ArchLinux (it is preferred since this project was made on [EndevourOS](https://endeavouros.com/)).

**Ubuntu:**

```bash
sudo apt-get install docker 
```

**ArchLinux:**

```bash
sudo pacman -Sy docker 
```

Besides Docker, You will also need Python for running scripts if you want to make your own data:

```bash
sudo apt-get install python 
```

**ArchLinux:**

```bash
sudo pacman -Sy python 
```

Installing Python for Windows is same as Docker, by using installer.

## 3. Starting services

Containers can be built and started by using a commands:

```bash
docker-compose build
docker-compose up -d
```

It will make two containers:

- PostgreSQL database - database that uses relational model
- pgAdmin - which is used as a managment tool for PostgreSQL database

While Docker composes, it will also install Apache AB for benchmarking purposes. Installation is placed in Dockerfile

When containers are created and started, pgAdmin tool will be exposed on [localhost:8888](http://localhost:8888) where You can login using with `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` which are set as default in `docker-compose.yaml`.

## Database restore

In the project, there is folder which contains backup of my database. **ALL DATA** is faked using Faker. If you wish, you can restore my database which will essentially remove need to fake your own data and save you some time.

## 5. Using Apache AB benchmarking tool

Apache AB is meant to show you how performance changes e.g. with different number of concurrency and requests.

To use it, You can use command:

```bash
ab -n <number of requests> -c <number of concurrency> http://127.0.0.1:5432/
```

In command, You can select how big of a number those two will be. For hostname I have put hostname where the locally exposed database is. It's port number and hostname can be changed in `docker-compose.yaml`.

**Note:** A lot of this commands are also covered in Python Notebook. For detailed version, I suggest You to look into Python Notebook. Project also comes with added Python environment for easier management.
