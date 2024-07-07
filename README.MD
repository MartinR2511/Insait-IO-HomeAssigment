# Insait IO - Homeassigment

This project is for the home assigment given by Insaint IO.
You can read about it in the file [ASSIGMENT.MD](ASSIGMENT.MD).

## Table of Contents
- [Insait IO - Homeassigment](#insait-io---homeassigment)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [General Explanaition](#general-explanaition)
  - [Versions](#versions)

## Installation
To install the project, follow these steps:
1. Clone the repository to your local machine:
        ```
        git clone https://github.com/MartinR2511/HomeAssigment.git
        ```
2. Navigate to the project directory:
        ```
        cd HomeAssigment
        ```
3. Create a virtual environment:
        ```
        python -m venv venv
        ```
4. Activate the virtual environment:
      - On Windows:
            ```
            venv\Scripts\activate
            ```
     - On macOS and Linux:
            ```
            source venv/bin/activate
            ```
5. Install the project dependencies:
        ```
        pip install -r requirements.txt
        ```
6. Configure Project Secrets:
   
   insert all the secrets in [.env](.env)



7. Start the project:

        docker-compose build
   
        docker-compose up -d
   
        alembic upgrade head
8. The project should now be up and running on your local machine.

## Usage
the /ask endpoint is working and you can post request any question you would like.
for easier testing of the /ask endpoint, you have been provided a [manual-test.py](manual-test.py) file in the root of the repository. This file is intended to make it easier for you to manually test the endpoint and verify its functionality.

To use the manual-test.py file, you can edit the question variable at line 6.
then you can run the script and see the printed output.

```
python manual-tester.py
```

## General Explanaition
* the flask app and the related files are located in the flaskapp/ folder.
* the alembic migraition files are located in the alembic/ folder.
* pytest test files are located in the flaskapp/tests/ folder.
* i have used the lastest postgres image for the database container.
* for ease of use i have left some db secrets in the .env file

## Versions
* V1.0.0
    * first working version
* V1.0.1
    * changed alembic and flask to use env variables 
    * added an ipaddress column, with migration in alembic
    * combined requirements for alembic and python to a single file
    * bugfixs:
        * fixed tests not finding modules
        * fixed tests not running with env variables  
