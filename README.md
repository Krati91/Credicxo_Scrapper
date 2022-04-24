# Credicxo Scrapper and Amazon Captcha Solver
This repository contains two tasks (The Scrapper, and The Amazon Captcha Solver)

**The Scrapper**    
This scrapes relevant information from the amazon pages based on the values from the csv and stores them in the database as well as generates a json file.      
It uses Beautiful Soup, requests, json, pandas and psycopg2 libraries.      

**The Amazon Captcha Solver**   
This lands on a amazon captcha page, extracts the image and solves it and fills the form.    
It uses Beautiful Soup, requests, pytesseract, PIL libraries.


**Steps to use the files**   

**1. Create a python virtual environment**   
`python -m venv venv`   
**2. Install all requirements**   
`pip install -r requirements.txt`    
**3. Activate the virtual environment**    
On windows - `venv\Scripts\activate`     
**4. To run scrapper**    
`python scrapper.py`    
**5. To run the captacha solver**   
`cd Bonus Task`    
`python captacha.py`
