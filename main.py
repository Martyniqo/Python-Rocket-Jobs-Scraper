import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


print('Put some skill that you are not familiar with (it will be excluded)')
unfamiliar_skill = input('>>>')
print(f'Filtering out {unfamiliar_skill}..')


def find_python_jobs():
      
      html_text = requests.get('https://rocketjobs.pl/?keyword=python').text
      # print(html_text)
      soup = BeautifulSoup(html_text, 'lxml')
      base_url = 'https://rocketjobs.pl'

      # We are looking for information from all job cards on the given page:
      job_cards = soup.find_all('div', class_ = 'css-6xbxgh')
      
      job_titles = []
      company_names = []
      required_skills = []
      more_infos = []
      new_offers = []

      for job_card in job_cards:
                  
            #Job title
            job = job_card.find('div', class_ ='MuiBox-root css-6vg4fr')
            job_title = job.find('h2').text
            
            #Company name
            company_name = job_card.find('div', class_='css-jx23jo').span.text
            
            #Skills
            skills = job_card.find_all('div', class_ = 'css-12973y2')
            skills_list = [skill.text for skill in skills]
            # Tworzenie ciągu znaków bez elementu 'New'
            skills_without_new = [skill for skill in skills_list if skill != 'New']
            skills = ', '.join(skills_without_new)
            
            #Link to the job post
            relative_url = job_card.a['href']
            job_url = base_url + relative_url

            #Salary range
            #salary_range = job_card.find_all('div', class_ = 'css-lz8wxo')
            
            #New?
            new_or_not = False
            new_or_not = any('New' in skill for skill in skills_list)
            
            # if unfamiliar_skill not in skills:
            #       print(f'Job Title: {job_title}')
            #       print(f'Company Name: {company_name}')
            #       print(f'Required Skills: {skills}')
            #       print(f'More Info: {job_url}')
            #       print(f'New offer: {new_or_not}')
            
            if unfamiliar_skill not in skills:
                  job_titles.append(job_title)
                  company_names.append(company_name)
                  required_skills.append(skills)
                  more_infos.append(job_url)
                  new_offers.append(new_or_not)
            
            
      jobs_df = pd.DataFrame({
      'Job Title': job_titles,
      'Company Name': company_names,
      'Required Skills': required_skills,
      'More Info': more_infos,
      'New Offer': new_offers
      })

      job_posts = 'jobs_data.csv'
      jobs_df.to_csv(job_posts, index=False, header=True) 
      print(f'Dane zostały zapisane do pliku: {job_posts}')

#Main
if __name__ == '__main__':
      while True: 
            find_python_jobs()
            time_wait = 10
            print(f'Waiting {time_wait} minutes...')
            time.sleep(time_wait * 60) #allows program to wait certain amount of time 
  
    
    
