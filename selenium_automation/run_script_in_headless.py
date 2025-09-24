from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = r"C:\Users\****\****\selenium\chromedriver\win64\140.0.7339.185\chromedriver.exe"

# Correct headless mode configuration
options = Options()
options.add_argument('--headless=new')  # This is the key change!
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
options.add_argument('--window-size=1920,1080')

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(web)

# Rest of your code remains the same...
wait = WebDriverWait(driver, 10)

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
        
        try:
            title = container.find_element(By.XPATH, './/span').text
            print(f"Title found: {title[:50]}...")
        except:
            title = "No title found"
            print("No title element found")
        
        try:
            subtitle = container.find_element(By.XPATH, './/h3').text
            print(f"Subtitle found: {subtitle[:50]}...")
        except:
            subtitle = "No subtitle found"
            print("No subtitle element found")
        
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
df_headlines.to_csv('headline-headless.csv', index=False)

print(f"\nSuccessfully processed {len(titles)} articles")
driver.quit()
