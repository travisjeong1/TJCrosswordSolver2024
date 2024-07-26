from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import re


app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():
   date_str = request.form['date']
   return solve_for_date(date_str)


@app.route('/solve_today')
def solve_today():
   today_str = datetime.today().strftime('%Y-%m-%d')
   return solve_for_date(today_str)


def solve_for_date(date_str):
   date = datetime.strptime(date_str, '%Y-%m-%d')
  
   # Check if the date is in the future
   if date > datetime.today():
       return render_template('error.html', message="The selected date is in the future. Please choose a past or current date.")


   formatted_date = date.strftime('%Y/%m/%d')  # Ensures the date is in 0000/00/00 format
  
   url = f"https://laxcrossword.com/{formatted_date}"


   # Use Selenium to handle dynamic content loaded via JavaScript
   chrome_options = Options()
   chrome_options.add_argument("--headless")  # Run in headless mode
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
   driver.get(url)
   page_source = driver.page_source
   driver.quit()


   soup = BeautifulSoup(page_source, 'html.parser')


   # Use elemnts to access the required data
   html = soup.find('html', class_='js')
   body = html.find('body', class_='archive date wp-embed-responsive')
   page = body.find('div', id='page', class_='hfeed site')
   site_content = page.find('div', class_='site-content')
   section = site_content.find('section', class_='content-area')
   main = section.find('main', class_='site-main', role='main')
   article = main.find('article')  # Since the article ID can change, just find the first article
   entry_content = article.find('div', class_='entry-content')
   across_googlies = entry_content.find('div', id='across_googlies')
   clue_list = across_googlies.find('div', id='clue_list')


   across_header = clue_list.find('h3', text='Across')
   down_header = clue_list.find('h3', text='Down')


   if across_header and down_header:
       across_section = across_header.find_next('p')
       down_section = down_header.find_next('p')


       if across_section and down_section:
           across_answers = format_clues(across_section.decode_contents())
           down_answers = format_clues(down_section.decode_contents())
       else:
           across_answers = ["No across answers found"]
           down_answers = ["No down answers found"]
   else:
       across_answers = ["Across/Down headers not found"]
       down_answers = ["Across/Down headers not found"]


   # Find the crossword grid image
   grid_div = entry_content.find('div', id='grid')
   if grid_div:
       img_tag = grid_div.find('img')
       if img_tag and 'src' in img_tag.attrs:
           img_src = img_tag['src']
       else:
           img_src = None
   else:
       img_src = None


   return render_template('result.html', date=date_str, across=across_answers, down=down_answers, img_src=img_src)


def format_clues(clue_html):
   # Remove <br> tags and split by new lines
   clues = clue_html.replace('<br/>', '\n').replace('<br>', '\n').split('\n')
   formatted_clues = []


   for clue in clues:
       clue = clue.strip() #changes presentation of clues
       if clue:
           clue = re.sub(r'(\d+)\s', r'\1. ', clue)
           clue = clue.replace(':', '-')
           if '-' in clue:
               parts = clue.rsplit('-', 1)
               clue = f'{parts[0]}- <u>{parts[1].strip()}</u>' #underline
           formatted_clues.append(f"{clue}")


   return formatted_clues


if __name__ == '__main__':
   app.run(debug=True)
