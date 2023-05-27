#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# User input for the product to search
product_to_search = input("Enter the product to search: ")


driver = webdriver.Chrome()


driver.get("https://www.amazon.in/")


search_box = driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
search_box.send_keys(product_to_search)


search_box.send_keys(Keys.RETURN)


driver.implicitly_wait(5)


# Close the browser
driver.quit()


# In[ ]:


#question-2


# In[ ]:


#2.	In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then scrape all the products available under that product name. Details to be scraped are: "Brand 
#Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
#“Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 


# In[12]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_amazon_product(product_name):
    base_url = "https://www.amazon.in"
    search_url = f"{base_url}/s?k={product_name}"

    product_data = []

    while True:
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        products = soup.find_all('div', {'data-component-type': 's-search-result'})

        if not products:
            break

        for product in products:
            product_info = {}
            # Get product details
            brand_element = product.find('span', class_='a-size-base-plus')
            if brand_element:
                product_info['Brand Name'] = brand_element.text.strip()
            else:
                product_info['Brand Name'] = '-'

            name_element = product.find('span', class_='a-size-medium')
            if name_element:
                product_info['Name of the Product'] = name_element.text.strip()
            else:
                product_info['Name of the Product'] = '-'

            price_element = product.find('span', class_='a-offscreen')
            if price_element:
                product_info['Price'] = price_element.text.strip()
            else:
                product_info['Price'] = '-'

            return_element = product.find('span', class_='a-size-small')
            if return_element:
                product_info['Return/Exchange'] = return_element.text.strip()
            else:
                product_info['Return/Exchange'] = '-'

            delivery_element = product.find('span', class_='a-text-bold')
            if delivery_element:
                product_info['Expected Delivery'] = delivery_element.text.strip()
            else:
                product_info['Expected Delivery'] = '-'

            availability_element = product.find('span', class_='a-size-base')
            if availability_element:
                product_info['Availability'] = availability_element.text.strip()
            else:
                product_info['Availability'] = '-'

            product_info['Product URL'] = base_url + product.find('a', class_='a-link-normal')['href']

            product_data.append(product_info)

        # Check if there is a next page
        next_page = soup.find('a', {'title': 'Next Page'})
        if next_page:
            search_url = base_url + next_page['href']
        else:
            break

    return product_data

# Get user input for the product to search
product_name = input("Enter the product to search on Amazon.in: ")

# Search for the product and scrape the details
search_results = search_amazon_product(product_name)

# Create a DataFrame from the scraped data
df = pd.DataFrame(search_results)

# Replace missing details with "-"
df.fillna('-', inplace=True)

# Save the DataFrame to a CSV file
df.to_csv('amazon_product_data.csv', index=False)

# Display the DataFrame
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#question-3
#Write a python program to access the search bar and search button on images.google.com and scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’


# In[6]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


# In[7]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[8]:


driver.get('https://images.google.com/?gws_rd=ssl')


# In[10]:


time.sleep(2)  # Wait for the page to load

# Define the keyword
keyword = 'fruits'

# Locate the search bar element and clear any existing text
search_bar = driver.find_element(By.CLASS_NAME,"gLFyf")
search_bar.clear()

# Enter the keyword in the search bar and submit the form
search_bar.send_keys(keyword)
search_bar.send_keys(Keys.RETURN)
time.sleep(2)  # Wait for the search results to load

# Scroll down to load more images
scroll_count = 0
while scroll_count < 3:  # Scroll 3 times
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    scroll_count += 1

# Find all the image thumbnails
thumbnails = driver.find_elements_by_css_selector("img.rg_i")

# Create a directory for the keyword if it doesn't exist
directory = f"images/{keyword}"
if not os.path.exists(directory):
    os.makedirs(directory)

# Scrape 10 images
count = 0
for thumbnail in thumbnails[:10]:
    # Get the image source URL
    image_url = thumbnail.get_attribute("src")

    # Download the image
    response = requests.get(image_url)
    image_path = f"{directory}/{keyword}_{count+1}.jpg"
    with open(image_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded image: {image_path}")
    count += 1

# Close the browser
driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#question - 4


# In[4]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import requests


# In[5]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[6]:


driver.get('https://www.flipkart.com/')


# In[7]:


product=driver.find_element(By.CLASS_NAME,'_3704LK')
#that was the class name
product.send_keys("oneplus nord")
#that was to tell the pointer to jump on the search bar
#send_keys is to when you want to right something on the box


# In[8]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[2]:


# Find all the elements with class '_4rR01T'
elements = driver.find_elements(By.CLASS_NAME, '_4rR01T')

# Extract the brand names, phone models, colors, and storage
brand_names = []
phone_models = []
colors = []
storage = []

for element in elements:
    text = element.text.strip()
    if text:
        parts = text.split(' ')
        brand_names.append(parts[0])
        phone_models.append(' '.join(parts[1:]))

        siblings = element.find_elements(By.XPATH, './following-sibling::ul[1]//li')
        color = siblings[0].text.strip() if len(siblings) > 0 else '-'
        storage_value = siblings[1].text.strip() if len(siblings) > 1 else '-'

        colors.append(color)
        storage.append(storage_value)

# Print the extracted brand names, phone models, colors, and storage
for brand, model, color, storage_value in zip(brand_names, phone_models, colors, storage):
    print(f"Brand: {brand}")
    print(f"Model: {model}")
    print(f"Color: {color}")
    print(f"Storage: {storage_value}")
    print()


# In[ ]:





# In[ ]:





# In[ ]:


#question--5


# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_coordinates(city):
    # Configure Selenium
    service = Service('path/to/chromedriver')  # Set the path to your ChromeDriver executable
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (without opening a browser window)
    driver = webdriver.Chrome(service=service, options=options)

    # Format the city name for the search query
    search_query = city.replace(' ', '+')

    # Load Google Maps with the search query
    url = f'https://www.google.com/maps/search/{search_query}'
    driver.get(url)

    # Find the element containing the coordinates
    coordinates_element = driver.find_element(By.CSS_SELECTOR, 'meta[itemprop="image"][content*="center"]')

    # Extract the coordinates from the content attribute
    content = coordinates_element.get_attribute('content')

    # Find the latitude and longitude values
    latitude = None
    longitude = None
    for part in content.split(';'):
        if part.startswith('center='):
            coordinates = part.split('=')[1].split(',')
            latitude = coordinates[0]
            longitude = coordinates[1]
            break

    # Quit the Selenium driver
    driver.quit()

    return latitude, longitude

# Example usage
city_name = 'delhi'
latitude, longitude = get_coordinates(city_name)
if latitude and longitude:
    print(f"Coordinates of {city_name}: Latitude {latitude}, Longitude {longitude}")
else:
    print(f"Coordinates of {city_name} not found.")


# In[ ]:





# In[ ]:


#Question--6


# In[2]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def scrape_funding_deals():
    # Configure Selenium
    service = Service('path/to/chromedriver')  # Set the path to your ChromeDriver executable
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (without opening a browser window)
    driver = webdriver.Chrome(service=service, options=options)

    # Load the funding deals page
    url = 'https://trak.in/india-startup-funding-investment-2015/'
    driver.get(url)

    # Wait for the table to load
    table_locator = (By.XPATH, '//table[@id="tablepress-48"]')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(table_locator))

    # Extract the details of each funding deal
    deals = []
    rows = driver.find_elements(By.XPATH, '//table[@id="tablepress-48"]/tbody/tr')
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        deal = {
            'Date': columns[0].text.strip(),
            'Startup Name': columns[1].text.strip(),
            'Industry/Vertical': columns[2].text.strip(),
            'Sub-Vertical': columns[3].text.strip(),
            'City/Location': columns[4].text.strip(),
            'Investor Name': columns[5].text.strip(),
            'Investment Type': columns[6].text.strip(),
            'Amount (In USD)': columns[7].text.strip()
        }
        deals.append(deal)

    # Quit the Selenium driver
    driver.quit()

    return deals

# Scrape funding deals
funding_deals = scrape_funding_deals()

# Create a DataFrame from the funding deals
df = pd.DataFrame(funding_deals)

# Print the DataFrame
df


# In[ ]:


#Question--7


# In[3]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

# Set up the webdriver
driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')

# Navigate to the website
driver.get("https://www.digit.in/")

# Click on the 'Gaming' section
gaming_section = driver.find_element(By.XPATH, '//span[@class="arrow_down gaming"]')
gaming_section.click()

# Click on 'Best Gaming Laptops'
best_gaming_laptops = driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[5]/div[2]/div/div[2]/div/ul[3]/li[4]/a')
best_gaming_laptops.click()

# Click on 'Best Gaming Laptops under 50,000'
best_laptops_under_50k = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/h2/a')
best_laptops_under_50k.click()

# Scrape the details of the gaming laptops
laptop_names = []
descriptions = []

laptop_tags = driver.find_elements(By.XPATH, '//div[@class="right-container"]/h3')
for tag in laptop_tags:
    laptop_name = tag.text
    laptop_names.append(laptop_name)

des_tags = driver.find_elements(By.XPATH, '//div[@class="Section-center"]//p')
for tag in des_tags:
    description = tag.text
    descriptions.append(description)

# Create a DataFrame
df = pd.DataFrame({'Laptop Name': laptop_names, 'Description': descriptions})

# Display the DataFrame
print(df)


# In[ ]:





# In[ ]:





# In[ ]:


#QUESTION-8


# In[ ]:


#8.	Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. 


# In[35]:


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_argument("--headless")  
service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)


url = 'https://www.forbes.com/billionaires/'
driver.get(url)


time.sleep(3)


# In[ ]:


scroll_pause_time = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

table = driver.find_element(By.XPATH, '//table[@class="table"]')


data = []
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows[1:]:
    columns = row.find_elements(By.TAG_NAME, 'td')
    rank = columns[0].text
    name = columns[1].text
    net_worth = columns[2].text
    age = columns[3].text
    citizenship = columns[4].text
    source = columns[5].text
    industry = columns[6].text
    data.append([rank, name, net_worth, age, citizenship, source, industry])


df = pd.DataFrame(data, columns=["Rank", "Name", "Net worth", "Age", "Citizenship", "Source", "Industry"])

# Print the DataFrame
print(df)


# In[ ]:


#QUESTION - 9


# In[37]:


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service('path/to/chromedriver')  # Replace with the actual path to your chromedriver executable
driver = webdriver.Chrome(service=service)


video_url = 'https://www.youtube.com/watch?v=xpPLpDWeznw'  


driver.get(video_url)


scroll_pause_time = 2
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    
    if new_height == last_height:
        break
    
    last_height = new_height


comment_elements = driver.find_elements(By.CSS_SELECTOR, '#comment #content-text')
upvote_elements = driver.find_elements(By.CSS_SELECTOR, '#comment #vote-count-middle')


comments = []
for i in range(len(comment_elements)):
    comment_text = comment_elements[i].text
    upvotes = upvote_elements[i].text
    comment_time_element = driver.find_element(By.CSS_SELECTOR, f'#comment-time-{i}')
    comment_time = comment_time_element.get_attribute('datetime')
    comments.append({
        'comment': comment_text,
        'upvotes': upvotes,
        'time': comment_time
    })

    if len(comments) >= 500:
        break

# Print the extracted comments
for comment in comments:
    print('Comment:', comment['comment'])
    print('Upvotes:', comment['upvotes'])
    print('Time:', comment['time'])


# In[ ]:


#question - 10


# In[38]:


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the Selenium Chrome driver
service = Service('path/to/chromedriver')  # Replace with the actual path to your chromedriver executable
driver = webdriver.Chrome(service=service)

# Specify the Hostelworld search URL for London
search_url = 'https://www.hostelworld.com/search?city=London&country=England'

driver.get(search_url)


time.sleep(3)


hostel_list = driver.find_element(By.CLASS_NAME, 'fabresult')

# Iterate over each hostel
hostels = hostel_list.find_elements(By.CLASS_NAME, 'fabresult__content')

for hostel in hostels:
    # Extract hostel name
    name_element = hostel.find_element(By.CLASS_NAME, 'fabresult__title')
    hostel_name = name_element.text
    
    # Extract distance from city center
    distance_element = hostel.find_element(By.CLASS_NAME, 'fabresult__distance')
    distance = distance_element.text
    
    # Extract ratings
    rating_element = hostel.find_element(By.CLASS_NAME, 'fabresult__rating')
    rating = rating_element.get_attribute('data-score')
    
    # Extract total reviews
    total_reviews_element = hostel.find_element(By.CLASS_NAME, 'fabresult__reviews')
    total_reviews = total_reviews_element.text
    
    # Extract overall reviews
    overall_reviews_element = hostel.find_element(By.CLASS_NAME, 'fabresult__rating--text')
    overall_reviews = overall_reviews_element.text
    
    # Extract privates from price
    privates_from_element = hostel.find_element(By.CLASS_NAME, 'fabresult__price')
    privates_from_price = privates_from_element.text
    
    # Extract dorms from price
    dorms_from_element = hostel.find_element(By.CLASS_NAME, 'fabresult__pricedorms')
    dorms_from_price = dorms_from_element.text
    
    # Extract facilities
    facilities_elements = hostel.find_elements(By.CLASS_NAME, 'fabresult__facilities')
    facilities = ', '.join([facility.text for facility in facilities_elements])
    
    # Extract property description
    description_element = hostel.find_element(By.CLASS_NAME, 'fabresult__desc')
    description = description_element.text
    
    # Print the scraped data
    print('Hostel:', hostel_name)
    print('Distance from city center:', distance)
    print('Ratings:', rating)
    print('Total Reviews:', total_reviews)
    print('Overall Reviews:', overall_reviews)
    print('Privates from price:', privates_from_price)
    print('Dorms from price:', dorms_from_price)
    print('Facilities:', facilities)
    print('Property Description:', description)
    print('---')


# In[ ]:





# In[ ]:





# In[ ]:




