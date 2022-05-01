# WebCloud2022

# Structure
- Assignment3: root folder of the second assignment 
    - static: folder, css style 
    - templates: folder, html files
    - nginx: folder, nginx files
    - app.py: shortenurl service 
    - user.py: user service
    - app.sh: bash file to run shortenurl service (port 5002)
    - user.sh: bash file to run user service (port 5001)
    - requirement.txt packages need in the application
    - README.md: this file
    - Dockerileapp: dockerfile to build image for app.
    - Dockerileuser: dockerfile to build image for user.
    - docker-compose.yml: docker compose file for nginx proxy.

# Run the basic code
    - Build the docker containers:
    ''' 
    docker build -f Dockerfileuser -t user .
    docker build -f Dockerfileapp -t app .
    '''
    - Run the containers separately:
    '''
    docker run -p 5001:5001 user
    '''
    '''
    docker run -p 5002:5002 app
    '''
    - "http://127.0.0.1:5001/users": user register
    <img width="805" alt="Screenshot 2022-04-21 at 21 55 42" src="https://user-images.githubusercontent.com/86485345/164542282-3b130a0c-ec5d-4625-9137-02e51fe591bd.png">
    
# Run the nginx proxy
    '''
    docker compose up
    '''
