# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''

    options = Options()
    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1120, 1000)
    
    url = "https://www.glassdoor.com/Job/Jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=%22data+scientist%22&sc.keyword=%22data+scientist%22&locT=&locId=&jobType="
    #url = f"https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword={keyword}&sc.keyword={keyword}&locT=&locId=&jobType="
    driver.get(url)
    jobs = []
    close = True
    
    while len(jobs) < num_jobs:
        time.sleep(slp_time)

        try:
            driver.find_element(By.CLASS_NAME, 'selected').click()
        except ElementClickInterceptedException:
            pass
    
        time.sleep(.1)
        
        while close:
            close_button_selector = '#LoginModal > div > div > div > div.actionBarMt0.css-gss116.e1jtvglp0 > button'
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, close_button_selector)))
            close_button.click()
            close = False
            time.sleep(1)  # Add a longer delay here, such as 2 seconds.


        job_buttons = driver.find_elements(By.XPATH, '//*[@id="MainCol"]/div[1]/ul')
        for job_button in job_buttons:
        
            print(f"Progress: {len(jobs)}/{num_jobs}")
            if len(jobs) >= num_jobs:
                break
    
            job_button.click()
            time.sleep(1)
            collected_successfully = False
                    
        
            while not collected_successfully:
                try:
                    company_name = driver.find_element(By.XPATH, './/div[@data-test="employerName"]').text
                    location = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    job_title = driver.find_element(By.XPATH, './/div[@data-test="jobTitle"]').text
                    try:
                        job_description = driver.find_element(By.XPATH, '//*[@id="JobDesc1008783773032"]/div/div/p[1]').text
                    except NoSuchElementException:
                        job_description = "N/A"
    
                    collected_successfully = True
                except:
                    time.sleep(5)
        
   
            try:
                salary_estimate = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
            except NoSuchElementException:
                salary_estimate = -1

            try:
                rating = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div/span').text
            except NoSuchElementException:
                rating = -1

            # ... (rest of the code for company tab)
            
            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                driver.find_element(By.XPATH,'.//div[@class="tab" and @data-tab-type="overview"]').click()
                time.sleep(1)
                try:
                    #<div class="infoEntity">
                    #    <label>Headquarters</label>
                    #    <span class="value">San Francisco, CA</span>
                    #</div>
                    headquarters = driver.find_element(By.XPATH,'//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                except NoSuchElementException:
                    headquarters = -1

                try:
                    size = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]').text
                except NoSuchElementException:
                    revenue = -1

            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1

                
            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({
                "Job Title": job_title,
                "Salary Estimate": salary_estimate,
                "Job Description": job_description,
                "Rating": rating,
                "Company Name": company_name,
                "Location": location,
                "Headquarters": headquarters,
                "Size": size,
                "Founded": founded,
                "Type of Ownership": type_of_ownership,
                "Industry": industry,
                "Sector": sector,
                "Revenue": revenue,
            })
        '''
        try:
            next_button = driver.find_element(By.XPATH, './/li[@class="next"]//a')
            next_button.click()
            time.sleep(2)  # Adding a short delay here
        except NoSuchElementException:
            print("Scraping terminated before reaching the target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break
        '''
    driver.quit()  # Close the browser after scraping
    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.
        
        