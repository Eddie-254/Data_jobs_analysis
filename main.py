import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


def scrap(country: str, country_code: str, role: str, filename: str) -> None:
    """
    Scrapes job listings from Indeed website and saves the data to a CSV file.

    Args:
        country (str): The country for which job listings should be scraped
        (e.g., 'us' for the United States).
        country_code (str): The country code used for language translation
        (e.g., 'en' for English).
        role (str): The job role or title to search for. ie, analyst,
        scientist, engineer
        filename (str): The name of the CSV file where the scraped data will
        be saved.

    Returns:
        None: This function does not return a value.
    """
    for i in range(10, 201, 10):
        url = f"https://{country}.indeed.com/jobs?q=data+{role}&start={i}"
        # Use the session to get the website data
        exec_path = r"C:\Users\WEIDIAN\Downloads\chromedriver.exe"
        options = Options()
        options.add_experimental_option('prefs', {
            'translate': {'enabled': 'true'},
            'translate_whitelists': {f'{country_code}': 'en'},
        })
        driver = webdriver.Chrome(
            executable_path=exec_path, chrome_options=options)

        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div#onetrust-button-group')))

        accept_button = driver.find_element_by_css_selector(
            'button#onetrust-accept-btn-handler')
        ActionChains(driver).move_to_element(
            accept_button).click(accept_button).perform()

        job_listings = driver.find_elements_by_css_selector('.cardOutline')

        count = 0
        job_data = []
        for job in job_listings:
            if count == 15:
                break
            for attempt in range(3):
                try:
                    job.click()
                    break
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
                    if attempt == 2:
                        print("Moving to next job listing...")
                        continue

            try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.jobsearch-JobInfoHeader-title')))
            except TimeoutException:
                print("Timeout Over. Moving to next job listing...")
                continue

            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            try:
                job_title = soup.find(
                    'h2', class_='jobsearch-JobInfoHeader-title').text.strip()
            except AttributeError:
                job_title = "Not found"

            try:
                company_location = soup.find(
                    'div', class_='css-6z8o9s').text.strip()
            except AttributeError:
                company_location = "Not found"

            try:
                job_summary = soup.find(
                    'div', class_='jobsearch-JobComponent-description'
                ).text.strip()
            except AttributeError:
                job_summary = "Not found"

            try:
                salary_element = soup.find(
                    'div', class_='css-k5flys').text.strip()
            except AttributeError:
                salary_element = "Not found"

            job_data.append({
                'Job Title': job_title,
                "Location": company_location,
                'Job Summary': job_summary,
                'Salary': salary_element,
            })

            count += 1

        df = pd.DataFrame(job_data)
        df.to_csv(f'{filename}_{i}.csv', index=False)

        driver.quit()
        time.sleep(10)


if __name__ == '__main__':
    scrap('uk', 'en', 'analyst', 'anas')
