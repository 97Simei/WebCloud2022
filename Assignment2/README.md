# WebCloud2022

# Structure
- Assignment2: root folder of the second assignment 
    - static: folder, css style 
    - templates: folder, html files
    - app.py: shortenurl service 
    - user.py: user service
    - README.md: this file
    - app.sh: bash file to run shortenurl service (port 5002)
    - user.sh: bash file to run user service (port 5001)
    - requirement.txt packages need in the application
# Run the code
- Create your own virtual environment:
Follow the link: https://docs.python.org/3/library/venv.html
- Activate your virtual environment:
- Install 
    pip install -r requirement.txt
- Run the code:
    sh app.sh
    sh user.sh
- You can quit the venv by:
    deactivate

# Use Service-Example:
- "http://127.0.0.1:5001/users" : user register
- "http://127.0.0.1:5001/users/login": user login and generate jwt code then send to the front end local storage
-  Click the button in the above page to use the shortenurl service:

