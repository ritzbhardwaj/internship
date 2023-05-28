#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"


response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


table = soup.find("table", class_="wikitable sortable")


ranks = []
names = []
artists = []
upload_dates = []
views = []


for row in table.find_all("tr")[1:]:
    
    cells = row.find_all("td")
    rank = cells[0].text.strip()
    name = cells[1].text.strip()
    artist = cells[2].text.strip()
    upload_date = cells[3].text.strip()
    view_count = cells[4].text.strip()
    
    
    ranks.append(rank)
    names.append(name)
    artists.append(artist)
    upload_dates.append(upload_date)
    views.append(view_count)


for i in range(len(ranks)):
    print(f"Rank: {ranks[i]}")
    print(f"Name: {names[i]}")
    print(f"Artist: {artists[i]}")
    print(f"Upload Date: {upload_dates[i]}")
    print(f"Views: {views[i]}")
    print()


# In[ ]:


#question --2 


# In[2]:


pip install selenium chromedriver-binary


# In[3]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode


webdriver_service = Service('path_to_chromedriver_executable')


driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)


url = "https://www.bcci.tv/"


driver.get(url)


menu_item = driver.find_element(By.CLASS_NAME, "navigation__item--international")
menu_item.click()


fixtures_link = driver.find_element(By.LINK_TEXT, "Fixtures")
fixtures_link.click()


driver.implicitly_wait(10)


fixtures_container = driver.find_element(By.CLASS_NAME, "js-list")


fixture_items = fixtures_container.find_elements(By.CLASS_NAME, "fixture-list__item")


match_titles = []
series_names = []
places = []
dates = []
times = []


for item in fixture_items:
    
    match_title = item.find_element(By.CLASS_NAME, "fixture-date").text.strip()
    series_name = item.find_element(By.CLASS_NAME, "u-unskewed-text").text.strip()
    place = item.find_element(By.CLASS_NAME, "fixture-stadium").text.strip()
    date = item.find_element(By.CLASS_NAME, "fixture-date__day").text.strip()
    time = item.find_element(By.CLASS_NAME, "fixture-time").text.strip()
    
    
    match_titles.append(match_title)
    series_names.append(series_name)
    places.append(place)
    dates.append(date)
    times.append(time)


for i in range(len(match_titles)):
    print(f"Match Title: {match_titles[i]}")
    print(f"Series: {series_names[i]}")
    print(f"Place: {places[i]}")
    print(f"Date: {dates[i]}")
    print(f"Time: {times[i]}")
    print()


# In[ ]:


#question--3


# In[ ]:


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = "http://statisticstimes.com/"
driver.get(url)

economy_link = driver.find_element_by_xpath("//a[contains(text(), 'Economy')]")
economy_link.click()

driver.implicitly_wait(5)

economy_page_html = driver.page_source


soup = BeautifulSoup(economy_page_html, "html.parser")
table = soup.find("table", class_="display compact")
rows = table.find_all("tr")

# Extract the details of State-wise GDP
for row in rows[1:]:
    cells = row.find_all("td")
    rank = cells[0].text.strip()
    state = cells[1].text.strip()
    gdp_18_19 = cells[2].text.strip()
    gdp_19_20 = cells[3].text.strip()
    share_18_19 = cells[4].text.strip()
    gdp_billion = cells[5].text.strip()
    
    print("Rank:", rank)
    print("State:", state)
    print("GSDP(18-19) - at current prices:", gdp_18_19)
    print("GSDP(19-20) - at current prices:", gdp_19_20)
    print("Share(18-19):", share_18_19)
    print("GDP($ billion):", gdp_billion)
    print("------------------------------------")

# Close the Selenium WebDriver
driver.quit()


# In[ ]:


#question-4


# In[ ]:


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()


url = "https://github.com/"
driver.get(url)

explore_menu = driver.find_element_by_xpath("//summary[contains(text(), 'Explore')]")
explore_menu.click()


trending_option = driver.find_element_by_xpath("//a[contains(text(), 'Trending')]")
trending_option.click()


driver.implicitly_wait(5)


trending_page_html = driver.page_source

soup = BeautifulSoup(trending_page_html, "html.parser")
repositories = soup.find_all("article")

for repository in repositories:
    title = repository.find("h1").text.strip()
    description = repository.find("p").text.strip()
    contributors_count = repository.find("a", class_="muted-link").text.strip().split()[0]
    language = repository.find("span", itemprop="programmingLanguage").text.strip()
    
    print("Repository Title:", title)
    print("Repository Description:", description)
    print("Contributors Count:", contributors_count)
    print("Language Used:", language)
    print("------------------------------------")

# Close the Selenium WebDriver
driver.quit()


# In[ ]:





# In[ ]:


#question-5


# In[ ]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

try:
    
    url = "https://www.billboard.com/"
    driver.get(url)

    
    charts_option = driver.find_element(By.LINK_TEXT, "Charts")
    charts_option.click()

    
    hot_100_link = driver.find_element(By.LINK_TEXT, "Hot 100")
    hot_100_link.click()

    
    driver.implicitly_wait(5)

    
    hot_100_page_html = driver.page_source

    
    soup = BeautifulSoup(hot_100_page_html, "html.parser")
    songs = soup.find_all("li", class_="chart-list__element")

    
    for song in songs:
        try:
            song_name = song.find("span", class_="chart-element__information__song").text.strip()
        except NoSuchElementException:
            song_name = "N/A"
        
        try:
            artist_name = song.find("span", class_="chart-element__information__artist").text.strip()
        except NoSuchElementException:
            artist_name = "N/A"
        
        try:
            last_week_rank = song.find("span", class_="chart-element__meta text--last").text.strip()
        except NoSuchElementException:
            last_week_rank = "N/A"
        
        try:
            peak_rank = song.find("span", class_="chart-element__meta text--peak").text.strip()
        except NoSuchElementException:
            peak_rank = "N/A"
        
        try:
            weeks_on_board = song.find("span", class_="chart-element__meta text--week").text.strip()
        except NoSuchElementException:
            weeks_on_board = "N/A"
        
        print("Song Name:", song_name)
        print("Artist Name:", artist_name)
        print("Last Week Rank:", last_week_rank)
        print("Peak Rank:", peak_rank)
        print("Weeks on Board:", weeks_on_board)
        print("------------------------------------")

except Exception as e:
    print("An error occurred:",


# In[ ]:


#question -6


# In[ ]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

try:
    # Load the website
    url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey"
    driver.get(url)

    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find("table", class_="in-article sortable")

    
    rows = table.find_all("tr")
    for row in rows[1:]:
        try:
            cells = row.find_all("td")
            book_name = cells[1].text.strip()
            author_name = cells[2].text.strip()
            volumes_sold = cells[3].text.strip()
            publisher = cells[4].text.strip()
            genre = cells[5].text.strip()

            print("Book Name:", book_name)
            print("Author Name:", author_name)
            print("Volumes Sold:", volumes_sold)
            print("Publisher:", publisher)
            print("Genre:", genre)
            print("------------------------------------")
        except NoSuchElementException:
            print("Error occurred while scraping row:", row)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the Selenium WebDriver
    driver.quit()


# In[ ]:


#question - 7


# In[1]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

try:
    
    url = "https://www.imdb.com/list/ls095964455/"
    driver.get(url)

    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    series_list = soup.find("div", class_="lister-list")

    
    series_items = series_list.find_all("div", class_="lister-item-content")
    for series_item in series_items:
        try:
            name = series_item.find("a").text.strip()
        except NoSuchElementException:
            name = "N/A"
        
        try:
            year_span = series_item.find("span", class_="lister-item-year").text.strip("()").strip()
        except NoSuchElementException:
            year_span = "N/A"
        
        try:
            genre = series_item.find("span", class_="genre").text.strip()
        except NoSuchElementException:
            genre = "N/A"
        
        try:
            run_time = series_item.find("span", class_="runtime").text.strip()
        except NoSuchElementException:
            run_time = "N/A"
        
        try:
            ratings = series_item.find("strong").text.strip()
        except NoSuchElementException:
            ratings = "N/A"
        
        try:
            votes = series_item.find("span", attrs={"name": "nv"}).text.strip()
        except NoSuchElementException:
            votes = "N/A"
        
        print("Name:", name)
        print("Year Span:", year_span)
        print("Genre:", genre)
        print("Run Time:", run_time)
        print("Ratings:", ratings)
        print("Votes:", votes)
        print("------------------------------------")
    
except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the Selenium WebDriver
    driver.quit()


# In[ ]:


#question - 8


# In[ ]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

try:
    
    url = "https://archive.ics.uci.edu/"
    driver.get(url)

    
    view_all_datasets_link = driver.find_element(By.LINK_TEXT, "View All Data Sets")
    view_all_datasets_link.click()

    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    dataset_table = soup.find("table", class_="table")

    
    dataset_rows = dataset_table.find_all("tr")
    for row in dataset_rows[1:]:
        try:
            cells = row.find_all("td")
            dataset_name = cells[0].text.strip()
            data_type = cells[1].text.strip()
            task = cells[2].text.strip()
            attribute_type = cells[3].text.strip()
            num_instances = cells[4].text.strip()
            num_attributes = cells[5].text.strip()
            year = cells[6].text.strip()

            print("Dataset Name:", dataset_name)
            print("Data Type:", data_type)
            print("Task:", task)
            print("Attribute Type:", attribute_type)
            print("Number of Instances:", num_instances)
            print("Number of Attributes:", num_attributes)
            print("Year:", year)
            print("------------------------------------")
        except NoSuchElementException:
            print("Error occurred while scraping row:", row)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the Selenium WebDriver
    driver.quit()


# In[ ]:


#question-9


# In[ ]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    
    url = "https://www.naukri.com/"
    driver.get(url)


    recruiters_option = driver.find_element(By.LINK_TEXT, "Recruiters")
    recruiters_option.click()

    
    driver.switch_to.window(driver.window_handles[-1]
                            
                                                        
    search_pane = driver.find_element(By.ID, "root-autocomplete")
    search_pane.send_keys("Data Science")

    search_button = driver.find_element(By.ID, "root-keywords")
    search_button.click()

    driver.implicitly_wait(5)

    
    recruiter_list = driver.find_element(By.CSS_SELECTOR, "div.row")
    recruiters = recruiter_list.find_elements(By.CSS_SELECTOR, "article")

    
    for recruiter in recruiters:
        try:
            name = recruiter.find_element(By.CSS_SELECTOR, "a.name").text.strip()
        except NoSuchElementException:
            name = "N/A"

        try:
            designation = recruiter.find_element(By.CSS_SELECTOR, "span.designation").text.strip()
        except NoSuchElementException:
            designation = "N/A"

        try:
            company = recruiter.find_element(By.CSS_SELECTOR, "a.company").text.strip()
        except NoSuchElementException:
            company = "N/A"

        try:
            skills = recruiter.find_element(By.CSS_SELECTOR, "div.skills").text.strip()
        except NoSuchElementException:
            skills = "N/A"

        try:
            location = recruiter.find_element(By.CSS_SELECTOR, "div.location").text.strip()
        except NoSuchElementException:
            location = "N/A"

        print("Name:", name)
        print("Designation:", designation)
        print("Company:", company)
        print("Skills They Hire For:", skills)
        print("Location:", location)
        print("------------------------------------")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the Selenium WebDriver
    driver.quit()

