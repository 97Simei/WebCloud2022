# WebCloud2022

# Structure
- Assignment3.1: root folder of the second assignment 
    - static: folder, css style 
    - templates: folder, html files
    - app.py: shortenurl service 
    - user.py: user service
    - app.sh: bash file to run shortenurl service (port 5002)
    - user.sh: bash file to run user service (port 5001)
    - requirement.txt packages need in the application
    - README.md: this file
    - Dockerileapp: dockerfile to build image for app
    - Dockerileuser: dockerfile to build image for user
    - as3deployapp.yaml: k8s deployment file for app
    - as3deployuser.yaml: k8s deployment file for user
    - as3serviceapp.yaml: k8s service file for app
    - as3serviceuser.yaml: k8s service file for user

# Run
- Set up the Kubernetes cluster and install Docker inside.
- Build the docker containers in all the nodes:
    ```
    docker build -f Dockerfileuser -t k8s-user .
    docker build -f Dockerfileapp -t k8s-app .
    ```
- Create deployments and services
  ```
  kubectl apply -f as3deployuser.yaml 
  kubectl apply -f as3deployapp.yaml 
  kubectl apply -f as3serviceuser.yaml
  kubectl apply -f as3serviceapp.yaml 
  ```
- "http://<IP<IP>>:5001/users": user register
- "http://<<IP>>:5001/users/login": user login and generate jwt code then send to the front end local storage
- Click the button in the above page to use the shortenurl service:
      <img width="805" alt="Screenshot 2022-04-21 at 21 55 42" src="https://user-images.githubusercontent.com/86485345/164542282-3b130a0c-ec5d-4625-9137-02e51fe591bd.png">

