#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[2]:


#python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data. 
#This task will be done in following steps: 
#1.	First get the webpage https://www.naukri.com/ 
#2.	Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field. 
#3.	Then click the search button. 
#4.	Then scrape the data for the first 10 jobs results you get. 
#5.	Finally create a dataframe of the scraped data. 


# In[3]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[4]:


driver.get("https://www.naukri.com/")


# In[5]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
#that was the class name
designation.send_keys("Data Analyst")
#that was to tell the pointer to jump on the search bar
#send_keys is to when you want to right something on the box


# In[6]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('banglore')


# In[7]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[52]:


job_titles=[]
job_locations=[]
company_name=[]
exp_req=[]


# In[53]:


#scraping the title
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_titles.append(title)


# In[54]:


#scraping the location
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    loc=i.text
    job_locations.append(loc)


# In[55]:


#scraping the company name
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    comp=i.text
    company_name.append(comp)


# In[56]:


#scraping the experience
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    exp_req.append(exp)


# In[57]:


import pandas as pd
df=pd.DataFrame({'titles':job_titles,'location':job_locations,'company name':company_name,'experience required':exp_req})
df


# In[58]:


#question--2


# In[59]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[60]:


driver.get("https://www.naukri.com/")


# In[61]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
#that was the class name
designation.send_keys("Data Analyst")
#that was to tell the pointer to jump on the search bar
#send_keys is to when you want to right something on the box


# In[62]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[63]:


job_titles=[]
job_locations=[]
company_name=[]
exp_req=[]


# In[64]:



title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_titles.append(title)


# In[65]:


#scraping the location
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    loc=i.text
    job_locations.append(loc)


# In[66]:


#scraping the company name
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    comp=i.text
    company_name.append(comp)


# In[67]:


#scraping the experience
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    exp_req.append(exp)


# In[68]:


import pandas as pd
df=pd.DataFrame({'titles':job_titles,'location':job_locations,'company name':company_name,'experience required':exp_req})
df


# In[ ]:





# In[38]:


#question-3


# In[266]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[267]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[268]:


driver.get("https://www.flipkart.com/?ef_id=abc149afa0381bd43b3a2dcaefbf33a9:G:s&s_kwcid=AL!739!10!76484942419895!76485137405439&semcmpid=sem_F1167BY7_Brand_adcenter")


# In[269]:


product=driver.find_element(By.CLASS_NAME,'_3704LK')
#that was the class name
product.send_keys("sunglasses")
#that was to tell the pointer to jump on the search bar
#send_keys is to when you want to right something on the box


# In[270]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[271]:


brands=[]
prices=[]
descriptions=[]


# In[280]:


result_count=0


# In[281]:


while result_count < 100:
    brand_tags = driver.find_elements(By.XPATH, '//div[@class="_2WkVRV"]')
    for tag in brand_tags:
        brandy = tag.text
        brands.append(brandy)
        result_count += 1
        if result_count == 100:
            break

    price_tags = driver.find_elements(By.XPATH, '//div[@class="_30jeq3"]')
    for tag in price_tags:
        pricey = tag.text
        prices.append(pricey)

    description_tags = driver.find_elements(By.XPATH, '//a[@class="IRpwTa"]')
    for tag in description_tags:
        desy = tag.text
        descriptions.append(desy)


# In[273]:


next_button = driver.find_element(By.XPATH, '//a[@class="_1LKTO3"]')
next_button.click()


# In[282]:


brands = brands[:100]
prices = prices[:100]
descriptions = descriptions[:100]


# In[283]:


length = min(len(brands), len(prices), len(descriptions))
brands = brands[:length]
prices = prices[:length]
descriptions = descriptions[:length]


# In[284]:


data = {
    'Brand': brands,
    'Price': prices,
    'Description': descriptions
}

df = pd.DataFrame(data)

# Print the dataframe
print(df)


# In[285]:


import pandas as pd
df=pd.DataFrame({'brand pf product':brands,'price of product':prices,'written description':descriptions})
df


# In[ ]:


#question-5


# In[295]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[296]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[297]:


driver.get("https://www.flipkart.com/apple-iphone-11-white-64-gb/product-reviews/itmfc6a7091eb20b?pid=MOBFWQ6BVWVEH3XE&lid=LSTMOBFWQ6BVWVEH3XEMXQMLO&marketplace=FLIPKART")


# In[298]:


ratings=[]
review_summarys=[]
full_reviews=[]


# In[299]:


result_count=0


# In[300]:


while result_count < 100:
    rating_tags = driver.find_elements(By.XPATH, '//div[@class="_3LWZlK _1BLPMq"]')
    for tag in rating_tags:
        rate = tag.text
        ratings.append(rate)
        result_count += 1
        if result_count == 100:
            break

    review_summary_tags = driver.find_elements(By.XPATH, '//p[@class="_2-N8zT"]')
    for tag in review_summary_tags:
        summer = tag.text
        review_summarys.append(summer)

    full_review_tags = driver.find_elements(By.XPATH, '//div[@class="t-ZTKy"]')
    for tag in full_review_tags:
        fullr = tag.text
        full_reviews.append(fullr)


# In[301]:


next_button = driver.find_element(By.XPATH, '//a[@class="_1LKTO3"]')
next_button.click()


# In[302]:


ratings= ratings[:100]
review_summarys = review_summarys[:100]
full_reviews = full_reviews[:100]


# In[303]:


import pandas as pd
df=pd.DataFrame({'ratingss':ratings,'review summarys':review_summarys,'full reviews':full_reviews})
df


# In[304]:


#question--6


# In[305]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[306]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[307]:


driver.get("https://www.flipkart.com/search?q=sneakers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")


# In[308]:


brands=[]
prices=[]
descriptions=[]


# In[309]:


result_count=0


# In[310]:


while result_count < 100:
    brand_tags = driver.find_elements(By.XPATH, '//div[@class="_2WkVRV"]')
    for tag in brand_tags:
        brandy = tag.text
        brands.append(brandy)
        result_count += 1
        if result_count == 100:
            break

    price_tags = driver.find_elements(By.XPATH, '//div[@class="_30jeq3"]')
    for tag in price_tags:
        pricey = tag.text
        prices.append(pricey)

    description_tags = driver.find_elements(By.XPATH, '//a[@class="IRpwTa"]')
    for tag in description_tags:
        desy = tag.text
        descriptions.append(desy)


# In[311]:


length = min(len(brands), len(prices), len(descriptions))
brands = brands[:length]
prices = prices[:length]
descriptions = descriptions[:length]


# In[312]:


import pandas as pd
df=pd.DataFrame({'brand pf product':brands,'price of product':prices,'written description':descriptions})
df


# In[313]:


#question--7


# In[339]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[340]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[341]:


driver.get("https://www.amazon.in/s?k=laptop&rh=n%3A1375424031%2Cp_n_feature_thirteen_browse-bin%3A12598163031&dc&ds=v1%3A6Tux315j3x%2BpOWHIKs9d2kHAuvvN3KUNOz84YeGZjLs&qid=1684426611&rnid=12598141031&ref=sr_nr_p_n_feature_thirteen_browse-bin_9")


# In[342]:


titles=[]
ratings=[]
prices=[]


# In[343]:


title_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tags[0:10]:
    title=i.text
    titles.append(title)


# In[344]:


rating_tags=driver.find_elements(By.XPATH,'//span[@class="a-icon-alt"]')
for i in rating_tags[0:10]:
    rat=i.text
    ratings.append(rat)


# In[345]:


price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags[0:10]:
    pri=i.text
    prices.append(pri)


# In[346]:


import pandas as pd
df=pd.DataFrame({'product title':titles,'ratingss':ratings,'price of product':prices})
df


# In[335]:


#question-7


# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[2]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[3]:


driver.get('https://www.azquotes.com/top_quotes.html')


# In[4]:


quotes=[]
authors=[]
types=[]


# In[5]:


quote_tags = driver.find_elements(By.XPATH, '//a[@class="title"]')

for quote in quote_tags:
    quote_texts.append(quote.text)
print(quote_texts)



# In[ ]:


author_tags = driver.find_elements(By.XPATH, '//div[@class="author"]')
for author in author_tags:
    authors.append(author.text)

print(authors)


# In[ ]:


type_tags = driver.find_elements(By.XPATH, '//div[@class="tags"]')
for tag in type_tags:
    types.append(tag.text)

print(types)


# In[7]:


data = []


for i in range(len(author_tags)):
    author = author_tags[i].text
    quote = quote_tags[i].text
    type = type_tags[i].text
    data.append({
        'Author': author,
        'Quote': quote,
        'Type': type
    })

df = pd.DataFrame(data)
df


# In[ ]:





# In[4]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[5]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[6]:


driver.get('https://www.jagranjosh.com/')


# In[7]:


gk_button = driver.find_element(By.XPATH, '//a[text()="GK"]')
gk_button.click()


# In[8]:


link = driver.find_element(By.XPATH, '//a[text()="List of all Prime Ministers of India"]')
link.click()


# In[15]:


names = driver.find_elements(By.XPATH, '//div[@class="table-box"]/table/tbody/tr/td[2]/p')

name_list = []
for name in names:
    name_list.append(name.text)

# Print the extracted names
for name in name_list:
    print(name)


# In[16]:


born_values = []
dead_values = []

rows = driver.find_elements(By.XPATH, '//div[@class="table-box"]/table/tbody/tr')

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    
    if len(cells) >= 4:
        born_values.append(cells[2].text)
        dead_values.append(cells[3].text)

# Print the extracted values
for i in range(len(born_values)):
    print("Born:", born_values[i])
    print("Dead:", dead_values[i])
    print()

# Alternatively, you can store the values in a pandas DataFrame
data = {
    'Born': born_values,
    'Dead': dead_values
}

df = pd.DataFrame(data)
print(df)


# In[17]:


term_of_office_values = []

rows = driver.find_elements(By.XPATH, '//div[@class="table-box"]/table/tbody/tr')

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    
    if len(cells) >= 5:
        term_of_office_values.append(cells[4].text)

# Print the extracted values
for value in term_of_office_values:
    print("Term of Office:", value)
    print()

# Alternatively, you can store the values in a pandas DataFrame
data = {
    'Term of Office': term_of_office_values
}

df = pd.DataFrame(data)
print(df)


# In[19]:


import pandas as pd
df=pd.DataFrame({'namess':names,'born_valuess':born_values,'dead_valuees':dead_values,'term of office':term_of_office_values})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#This task will be done in following steps: 
#1.	First get the webpage https://www.motor1.com/ 
#2.	Then You have to click on the List option from Dropdown menu on left side. 
#3.	Then click on 50 most expensive cars in the world.. 
#4.	Then scrap the mentioned data and make the dataframe. 


# In[38]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[39]:


driver=webdriver.Chrome(r"C:\Users\RITVIK BHARDWAJ\Desktop\chrome web driver\chrome.exe")


# In[40]:


driver.get('https://www.motor1.com/')


# In[41]:


button=driver.find_element(By.XPATH,'//div[@class="m1-hamburger-button"]')
button.click()


# In[44]:


button_a=driver.find_element(By.XPATH,'//button[@class="dropdown-toggle"]')
button_a.click()


# In[47]:


button_list=driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[6]/ul/li[1]/a')
button_list.click()


# In[48]:


item = driver.find_element(By.XPATH, '/html/body/div[3]/div[8]/div[1]/div[1]/div/div/div[7]/div/div[1]/h3/a')
item.click()


# In[49]:


cars_name=[]


# In[76]:


car_name_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in car_name_tags[:50]:
    car=i.text
    cars_name.append(car)


# In[77]:


print(cars_name)


# In[78]:


import pandas as pd
df=pd.DataFrame({'cars name':cars_name})
df


# In[ ]:





# In[ ]:




