from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = r"C:\Users\****\****\selenium\chromedriver\win64\140.0.7339.185\chromedriver.exe"

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Finding Elements
containers = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="teaser__copy-container"]'))
)

print(f"Found {len(containers)} containers")

titles = []
subtitles = []
links = []

for i, container in enumerate(containers):
    try:
        print(f"\n--- Processing container {i+1} ---")
        
        # Try to find title (span)
        try:
            title = container.find_element(By.XPATH, './/span').text
            print(f"Title found: {title[:50]}...")
        except:
            title = "No title found"
            print("No title element found")
        
        # Try to find subtitle (h3)
        try:
            subtitle = container.find_element(By.XPATH, './/h3').text
            print(f"Subtitle found: {subtitle[:50]}...")
        except:
            subtitle = "No subtitle found"
            print("No subtitle element found")
        
        # Try to find link (a) - handle case where there might not be one
        try:
            link = container.find_element(By.XPATH, './/a').get_attribute('href')
            print(f"Link found: {link[:50]}...")
        except:
            link = "No link found"
            print("No link element found")
        
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)
        
    except Exception as e:
        print(f"Error processing container {i+1}: {e}")
        titles.append("Error")
        subtitles.append("Error")
        links.append("Error")

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv', index=False)

print(f"\nSuccessfully processed {len(titles)} articles")
print(f"Titles with content: {sum(1 for t in titles if t not in ['No title found', 'Error'])}")
print(f"Links with content: {sum(1 for l in links if l not in ['No link found', 'Error'])}")

driver.quit()
