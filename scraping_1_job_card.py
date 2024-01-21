import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://rocketjobs.pl/?keyword=python').text
# print(html_text) # without .text this prints request status [200] = working! 

soup = BeautifulSoup(html_text, 'lxml') # 'html.parser'

base_url = 'https://rocketjobs.pl'

# We are looking for information from JUST 1 job card:
job_card = soup.find('div', class_ = 'css-6xbxgh')
# print(job_card)

job = job_card.find('div', class_ ='MuiBox-root css-6vg4fr')
job_title = job.find('h2').text
# print(job_title)

company_name = job_card.find('div', class_='css-jx23jo').span.text
# print(company_name)

skills = job_card.find_all('div', class_ = 'css-12973y2')
skills_list = [skill.text for skill in skills]
skills = ', '.join(skills_list)
# print(skills)

#Link to the job post
relative_url = job_card.a['href']
url = base_url + relative_url
print(url)

salary_range = job_card.find_all('div', class_ = 'css-lz8wxo')
# for salary in salary_range:
#     print(salary.text)

new_or_not = False
new_or_not = any('New' in skill for skill in skills_list)
# print(new_or_not)

# print(f'''
# Job title: {job_title}
# Company Name: {company_name}
# Required Skills: {skills}
# New: {new_or_not}
#         ''')