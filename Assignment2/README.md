# WebCloud2022
<img width="1154" alt="Screenshot 2022-04-11 at 11 02 40" src="https://user-images.githubusercontent.com/86485345/162702732-ff5196bb-8b1f-44ac-991f-665d7780504f.png">


# Structure
- Assignment1: root folder of the first assignment 
    - static: folder, css style 
    - templates: folder, html files
    - app.py: main logic
    - README.md: this file
    - run.sh: bash file to intstall the requirement packages and run the application

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
- See All URLs：
rederict to http://127.0.0.1:5000/URLList
- Delete a URL：
hashid could get from the URLList
http://127.0.0.1:5000/delete/{hashid}
- Delete all URLs：
http://127.0.0.1:5000/delete/All
- Update a URL：
http://127.0.0.1:5000/update/{hashid}
