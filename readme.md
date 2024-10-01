# Encoder - Decoder

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [API Documentation](#api-documentation)
  - [Testing](#testing)
  
- [Contributing](#contributing)
- [License](#license)


## Introduction
 The String Encoder-Decoder is an application built with <a href="https://www.django-rest-framework.org/">Django Rest Framework</a>. This system provides an API service that allows users to securely encode and decode strings using a specified salt key and index. The application enhances data integrity and security by incorporating salt into the encoding process.


### Features
 - String Encoding: Users can input a string along with a salt key and salt index to generate an encoded version of the string.
 - String Decoding: Users can decode previously encoded strings by providing the correct salt key and index, allowing retrieval of the original data.


### Technologies Used
 - Django: The web framework used to build the application.
 - Django Rest Framework: Utilized for creating the RESTful API endpoints for encoding and decoding.
 - Base64: A method used for encoding and decoding the string data.
 - Testing: Django's built-in test framework (APITestCase, APIClient) for verifying the functionality of the API.

## Getting Started

To run this web application on your local machine, follow the steps below:

### Prerequisites

Before getting started, ensure that you have the following software installed on your machine:

- Python: Download and install Python from the official website: https://www.python.org/downloads/
- GIT: Download and install GIT from the official website: https://git-scm.com/downloads


### Installation

Step-by-step guide on how to install the project and its dependencies.

1. Clone the repository to your local machine using Git: <br>
HTTPS

```bash
git clone https://github.com/bosukeme/encoder-decoder.git
```

SSH
```bash
git clone git@github.com:bosukeme/encoder-decoder.git
```

<br>

2. Navigate to the project directory

```bash
cd encoder-decoder
```

Before you start the application, you need to set up an environment variables. Here's how you can do it:

- Create a file called `.env` file at the root folder with the environment variables in the `.env.sample` file


### start application

navigate to the root directory

```bash
python manage.py migrate
python manage.py runserver
```

### API documentation

Access API documentation via Swagger UI using the link below after starting up the application

```bash
http://localhost:8000/
```

### Testing

```bash
python manage.py test
```

## Contributing
If you would like to contribute, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bugfix.
- Submit a pull request.


## Author

Ukeme Wilson
- <a href="https://www.linkedin.com/in/ukeme-wilson-4825a383/">Linkedin</a>.
- <a href="https://medium.com/@ukemeboswilson">Medium</a>.
- <a href="https://www.ukemewilson.sbs/">Website</a>.

