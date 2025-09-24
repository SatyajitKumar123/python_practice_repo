from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = r"C:\Users\****\****\selenium\chromedriver\win64\140.0.7339.185\chromedriver.exe"

driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

wait = WebDriverWait(driver, 10)

# Try finding articles using a different approach - look for article containers
articles = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "teaser")]//a[.//span and .//h3]'))
)

titles = []
subtitles = []
links = []

for article in articles:
    try:
        title = article.find_element(By.XPATH, './/span').text
        subtitle = article.find_element(By.XPATH, './/h3').text
        link = article.get_attribute('href')
        
        if title and link:  # Only add if we have content
            titles.append(title)
            subtitles.append(subtitle)
            links.append(link)
    except:
        continue

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv', index=False)

print(f"Successfully extracted {len(titles)} articles")

driver.quit()
