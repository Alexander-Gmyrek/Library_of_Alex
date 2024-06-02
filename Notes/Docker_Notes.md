# Docker Notes

Created: May 31, 2024 2:32 PM

## Quick notes

## What is Docker?

Docker is a platform that allows you to package applications into nice little boxes. This includes everything they need to function, aka their “dependencies”.  This box is called a “Container” and is the core piece in the “Containerization” process. This box can be accessed via "ports" that allow you to send info in or out, along with a few other access methods. These boxes can be run on any machine with Docker installed regardless of operating system or other device specific software configurations, assuming it meets the necessary hardware requirements. This means that you can give the box to anyone with Docker and they will be able to use it without needing anything else. 

## Docker Containers

- **Image:** A static executable snapshot of the application that contains everything need to run the application. This includes the application’s code, libraries, runtime, environment variables, and configuration files. It is a static definition of  what a container should contain and how it should behave.
- **Dockerfile:** a text file that contains a series of instructions on how to build a Docker Image. Each instruction in the the Dockerfile corresponds to a layer in the container image. The Dockerfile specifies the base image, environment setup, dependencies, configuration files, and the command to run the application.
- **Layers:** Read only files that represent filesystem changes. Each layer in the container image corresponds to the instruction in the Dockerfile. Layers are stacked on top of each other to form the final container image. The Union File System or UFS combines these layers, making them appear as a single coherent filesystem.
- **Container Runtime:** the software that runs and manages containers on a host system. Docker Engine is the most common container runtime. The runtime is responsible for creating, starting, stopping, and managing containers.
- **Namespaces:** Provide isolation for running containers. They ensure that each container has its own isolated environment, including process IDs (PID namespace), network interfaces (net namespace), filesystem (mount namespace), and other system resources.
- **Cgroups:** Aka Control Groups, are a Linux kernel feature used to limit prioritize and account for the resource usage, i.e. CPU, memory, disk I/O, network, etc. of a  container. Cgroups ensure that containers do not exceed their allocated resources and help in resource management.
- **Volumes:** used to persist data generated and used by Docker containers. They provide a way to share data between the host system and containers, or between multiple containers.
- **Docker Networks:** Docker provides networking capabilities to allow containers to communicate with each other and with external systems. Docker networks can be configured to use different drivers (e.g., bridge, host, overlay) to control how containers are connected and isolated.
- **Configuration:** Containers can be configured using environment variables, configuration files, and Docker secrets. These mechanisms allow for the dynamic configuration of containers without modifying the container image.
- **Secrets:** Provide a secure way to store sensitive data such as passwords, API keys, and certificates.

## Necessary files

- Dockerfile (This is just a text file)
- docker-compose.yml
- (This is usually but not always required) requirements.txt
- .dockerignore

## Dockerfile

A Dockerfile is a script that contains a series of instructions on how to build a Docker image. It automates the process of creating a Docker image by specifying the operating system, software packages, configurations, and dependencies required for your application. 

**Dockerfile tips:**

- It’s important to remember that layers build up so they can only affect what comes after them.
- To comment use “#”

**Basic Structure of a Dockerfile:**

- **FROM:** Specifies the base image you want to use for your docker image. Every Dockerfile starts with a “FROM” instruction.
    - Example: “FROM python:3.9”
    - This will use the official python runtime as the base image.
- **LABEL**: Adds metadata to the image, such as maintainer information or version.
    - Example: “LABEL maintainer="your.email@example.com"”
    - So people know where to send their complements… or more likely tell you it broke.
- **RUN**: Executes commands in the container during the image building process. It’s often used to install software packages.
    - Example: RUN pip install --no-cache-dir -r requirements.txt
    - This tells pip to install all of the packages you need
    - Note: Docker uses the sh shell in case you were wondering
- **COPY** or **ADD**: Copies files or directories from your local filesystem to the Docker image.
    - Example: ”COPY . /app”
    - This copies the current directory contents into the container at /app
- **WORKDIR**: Sets the working directory for the subsequent instructions, simplifying the file path references.
    - Example: “WORKDIR /app”
    - This setts the working dir to /app
- **EXPOSE**: Specifies the ports that the container will listen on at runtime. This is where you would connect to your program.
    - Example: “EXPOSE 3360”
    - In this case we are using 3360. Make sure this port is open. You can check with “netstat -ano | findstr :<port number>” on Windows.
- **CMD**: Provides the default command to run when the container starts. Unlike `RUN`, `CMD` is not executed during the build process.
    - Example: “CMD ["flask", "run", "--host=0.0.0.0"]”
    - This tells it to run flask when the container launches
- **ENTRYPOINT**: Configures a container that will run as an executable.
    - Example: (Needs Example)
- **ENV:** Defines an Environment Variable. These aren’t very secure so try using docker secrets if that is something you are worried about.
    - Example: “ENV FLASK_APP=app.py”
    - This sets FLASK_APP equal to app.py for all subsequent layers.

**Example Docker File:** 

```docker
# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run flask when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
```

## docker-compose.yml

A configuration for defining and running multi-container docker applications. Docker Compose allows you to manage multiple containers as a single service. This means less work so it’s super important.

**Basic Structure of docker-compose.yml:**

- **version**: Specifies the version of the Compose file format.
    - Example: “version: '3’”
    - I use 3 will be using 3.
- **services**: Defines a list of services (containers) that are part of the application.
    - Example:
    
    ```yaml
    services:
    	web:
    		# Service configuration goes here
    	database:
    		# Service configuration goes here
    ```
    
- **service configuration**: Within each service, you specify how the container should be built and run.
    - **Key Configuration Options:**
        - 
        - **image**: Specifies the Docker image to use for the container.
            
            ```yaml
            services:
              mysql:
                image:mysql:latest
            ```
            
        - **build**: Provides instructions to build the Docker image from a Dockerfile.
            
            ```yaml
            services:
              web:
                build: .
            ```
            
        - **ports**: Maps ports between the container and the host machine.
            
            ```yaml
            services:
              web:
                ports:
                  - "3360:3360"
            ```
            
        - **volumes**: Mounts host machine directories or files into the container.
            
            ```yaml
            services:
              web:
                volumes:
                  - db_data:/var/lib/mysql
                  - ./init.sql:/docker-entrypoint-initdb.d/init.sql
            ```
            
        - **environment**: Sets environment variables for the container.
            
            ```yaml
            services:
              database:
                image: mysql:latest
                environment:
                  MYSQL_ROOT_PASSWORD: GoodPassword
                  MYSQL_DATABASE: ExampleDB
                  MYSQL_USER: ExampleUser
                  MYSQL_PASSWORD: ExamplePassword
            ```
            
        - **depends_on**: Specifies dependencies between services, determining the order in which they are started.
            
            ```yaml
            services:
              web:
                depends_on:
                  - mysql
            ```
            

**Example ‘docker-compose.yml’ File:**

```yaml
version: '3'
services:
  mysql:
    image: mysql:latest
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: ExamplePassword
      MYSQL_DATABASE: ExampleDB
      MYSQL_USER: ExampleUser
      MYSQL_PASSWORD: ExampleUserPassword
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

  web:
    build: .
    container_name: flask_app
    volumes:
      - .:/app
    ports:
      - "5000:5000"
    depends_on:
      - mysql

volumes:
  db_data:

```

## To Start

- docker-compose up --build
- To run the services in the background try “docker-compose up -d”
- If someone is using your ports try “netstat -ano | findstr :<port number>” then “taskkill /PID <pid_number> /F”
- **Stop: “**docker-compose down**”**

## **Basic Docker Setup/Steps**

1. Install Docker. You can do that here: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Write a Dockerfile.
3. Build the Docker image. 
4. Run the Docker container. You can do this in the terminal with “docker-compose up --build”
5. Use Docker Compose for multi-container setups.

## Access methods

*More info on these please.

- **Ports:** Used for network communication
- **Volumes:** Used to persist data and share it between the container and the host.
- **Environment Variables:** Used to pass configuration data to containers.
- **Docker Networks:** Facilitate communication between multiple containers.

## Docker Secrets

*Needs more research

## Definitions

- **Containerization:** Making standardized “boxes” or “containers” that can be used anywhere and run without additional set up or dependencies. It can be seen as an application level of abstraction and is an integral part of the engineering design process. Allowing easy deployment and division of labor.
- **Dependencies:** External components an application requires to function. This includes Libraries, Frameworks, external services, configuration files, system dependencies, and packages.
- **Library:** Collections of prewritten code that a developer can use to optimize tasks
- **Framework:** A larger structure that provides a foundation on which to build programs. Selecting the proper framework/s is an important part of the project design process as the often dictate the architecture, format, and functionality of an application.
- **External Service:** Services that an application relies on, such as databases, authentication services, or APIs from third parties.
- **Configuration File:** Files that define how a software interacts with it’s environment, such as environment settings, database connection strings, API keys, and more.
- **System Dependencies:** Operating system-level components that the application needs to run, such as specific versions of runtime environments, system utilities, or other system software.
- **Packages:** Bundled sets of code and recourses distributed through a package manager.
- **Package Manager:** a language specific application that allows you to download, update, and delete packages in your environment, usually accessed through the command line.
- **Application:** A ready made program or collection of program designed to help a user complete a task or group of tasks. If you imagine programs as kitchen tools like a knife, whisk, or pot, used to complete one specific task or part of a task like chop vegetables or whisk eggs, you can imagine an application like an appliance with many functions that helps you prepare an entire dish.
- **Program:** sets of instructions a computer can execute to preform a specific task. They are the fundamental building blocks of software. Programs are used to automate tasks. Programs are made up of executable instructions written in source code that are then compiled into machine code for the computer to execute or interpreted by the computer at run time.
- **Dockerfile:** A text file with instructions on how to build a Docker image.
- **Docker Image:** A snapshot of a container that includes everything needed to run an application.
- **Docker Container:** A running instance of a Docker image.
- **Docker Compose:** A tool for defining and running multi-container Docker applications using a `docker-compose.yml` file.
- **A:** a

<aside>
💡 make a file on the project design process

</aside>