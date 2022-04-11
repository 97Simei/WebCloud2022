# WebCloud2022

# Structure
- Assignment1: root folder of the first assignment 
- static: css style 
- templates: html file
- - app.py: main logic
- - README.md: this file
- - run.sh: bash file to intstall the requirement packages and run the application

# Run the code
- Create your own virtual environment:
Follow the link: https://docs.python.org/3/library/venv.html
- Activate your virtual environment:
- Run the code:
    sh run.sh
- You can quit the venv by:
    deactivate

# Use Service-Example:
- Shorten a Url：
Input the Url and Click “Submit” button
- See All URL：
rederict to http://127.0.0.1:5000/URLList
- Delete a URL：
hashid could get from the URLList
http://127.0.0.1:5000/delete/{hashid}
- Delete all URLs：
http://127.0.0.1:5000/delete/All
- Update a URL：
http://127.0.0.1:5000/update/{hashid}
