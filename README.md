# docker_projects

A collection of Docker-based projects demonstrating different aspects of containerization, such as API development, Python applications, volume usage, and web server hosting.

## 📁 Project Structure

- **api_demo**: Contains a simple API project containerized with Docker.
- **python_demo_project**: A basic Python application showcasing Docker containerization and dependency management.
- **volume_mount**: Demonstrates how to use Docker volumes for persistent data.
- **web_server_hosting/testapp**: Hosts a simple web application using a web server inside a Docker container.

## 🛠️ Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (for multi-container projects)

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/vaibhav208/docker_projects.git
   cd docker_projects
   ````

2. Navigate to a project directory:

   ```bash
   cd <project_directory>
   ```

3. Build the Docker image:

   ```bash
   docker build -t <image_name> .
   ```

4. Run the container:

   ```bash
   docker run -d -p <host_port>:<container_port> <image_name>
   ```
