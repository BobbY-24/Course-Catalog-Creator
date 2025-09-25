Course Catalog Scraper
This project scrapes course information from a university course catalog webpage and exports it into a structured CSV file. It uses Python, BeautifulSoup, and regular expressions to extract course codes, credit hours, names, and descriptions.
Features
Fetches course catalog data from a given URL.


Extracts:


class_code → formatted course code (e.g., CS_1331).


credit_hours → number of credit hours (defaults to 1 if not numeric).


official_name → official course title.


description → course description text.


Stores results in a CSV file with customizable filename.


Handles file renaming safely with error handling.


Requirements
Install dependencies via pip:
pip install requests beautifulsoup4

Usage
from scraper import csv_creator  

# Example usage
url = "https://example.edu/course-catalog"  
csv_creator(url, "courses")  

This will create a file named courses.csv in the working directory.
Example CSV Output
class_code,credit_hours,official_name,description
CS_1331,3,Introduction to Object-Oriented Programming,An introduction to object-oriented principles using Java.
MATH_1554,4,Linear Algebra,Matrix methods and linear algebra with applications.

File Structure
.
├── scraper.py   # main script
├── README.md    # project documentation
└── requirements.txt 

Notes
Works best with HTML pages that follow a consistent catalog structure (<strong> for course titles/credits and .courseblockdesc for descriptions).


You may need to adjust the parsing logic (soup.find_all) if the target site’s HTML differs.


License
MIT License — feel free to use and modify for your own projects.

