#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1)	Write a python program to display all the header tags from wikipedia.org and make data frame. 
get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')


# In[1]:


from bs4 import BeautifulSoup
import requests


# In[32]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[33]:


soup = BeautifulSoup(page.content)
soup


# In[34]:


headers = []

for i in soup.find_all('span',class_="mw-headline"):                 
    headers.append(i.text)

headers


# In[35]:


import pandas as pd
df=pd.DataFrame({'headers':headers})
df


# In[36]:


#2)	Write a python program to display IMDB’s Top rated 50 movies’ data (i.e. name, rating, year of release) and make data frame. 


# In[37]:


from bs4 import BeautifulSoup
import requests


# In[38]:


page=requests.get('https://www.imdb.com/list/ls055386972/')


# In[39]:


soup=BeautifulSoup(page.content)
soup


# In[40]:



names = []

for i in soup.find_all('h3',class_="lister-item-header"):
    names.append(i.text.strip())


print(names)



# In[41]:



years = []


for i in soup.find_all('span', class_='lister-item-year'):
    
    years.append(i.text.strip('(|)'))


print(years)


# In[42]:



ratings = []

for i in soup.find_all('div', class_='ipl-rating-star small'):
    ratings.append(i.text.strip())


print(ratings)


# In[43]:


#making DataFrame
import pandas as pd
df=pd.DataFrame({'names':names,'ratings':ratings,'year of release':years})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:


#4)	Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm and make data frame. 
 


# In[34]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[42]:


soup=BeautifulSoup(page.content)
soup


# In[47]:


presidents = soup.find_all('div', class_='presidentListing')
president_data = []


# In[50]:


for president in presidents:
    name = president.find('h3').text.strip()
    term_of_office = president.find('p').text.strip().replace('Term of Office:', '')
    president_data.append((name, term_of_office))


# In[53]:


import pandas as pd


# In[ ]:





# In[ ]:





# In[78]:


df = pd.DataFrame(president_data, columns=['Name', 'Term of Office'])
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


###5)	Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame- 
#a)	Top 10 ODI teams in men’s cricket along with the records for matches, points and rating. 
#b)	Top 10 ODI Batsmen along with the records of their team and rating. 
#c)	Top 10 ODI bowlers along with the records of their team andrating


# In[68]:


page =requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[69]:


soup=BeautifulSoup(page.content)
soup


# In[77]:


team_data = []
table = soup.select_one('.table')

# Find all the rows in the table
rows = table.select('tr')

# Loop through each row (excluding the header row) up to 10 rows
for row in rows[1:11]:
    # Find all the columns in the row
    columns = row.select('td')
    team = columns[1].text.strip()
    matches = columns[2].text.strip()
    points = columns[3].text.strip()
    ratings = columns[4].text.strip()
    team_data.append((team, matches, points, ratings))

df = pd.DataFrame(team_data, columns=['Team', 'Matches', 'Points', 'Ratings'])
df


# In[76]:


batsman_data = []
table = soup.select_one('.table')

# Find all the rows in the table
rows = table.select('tr')

# Loop through each row (excluding the header row) up to 10 rows
for row in rows[1:11]:
    # Find all the columns in the row
    columns = row.select('td')
    position = columns[0].text.strip()
    batsman = columns[1].text.strip()
    team = columns[2].text.strip()
    rating = columns[3].text.strip()
    batsman_data.append((position, batsman, team, rating))

df = pd.DataFrame(batsman_data, columns=['Position', 'Batsman', 'Team', 'Rating'])
df


# In[75]:


bowler_data = []
table = soup.select_one('.table')

# Find all the rows in the table
rows = table.select('tr')

# Loop through each row (excluding the header row) up to 10 rows
for row in rows[1:11]:
    # Find all the columns in the row
    columns = row.select('td')
    position = columns[0].text.strip()
    if columns[1].find('a'):
        bowler = columns[1].find('a').text.strip()
    else:
        bowler = columns[1].text.strip()
    team = columns[2].text.strip()
    rating = columns[3].text.strip()
    bowler_data.append((position, bowler, team, rating))

df = pd.DataFrame(bowler_data, columns=['Position', 'Bowler', 'Team', 'Rating'])
df


# In[ ]:


#a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame- 
#a)	Top 10 ODI teams in women’s cricket along with the records for matches, points and rating. 
#b)	Top 10 women’s ODI Batting players along with the records of their team and rating. 
#c)	Top 10 women’s ODI all-rounder along with the records of their team and rating. 
 


# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# In[84]:


player_data = []
table = soup.select_one('.table')

# Find all the rows in the table
rows = table.select('tr')

# Loop through each row (excluding the header row) up to 10 rows
for row in rows[1:11]:
    # Find all the columns in the row
    columns = row.select('td')
    team = columns[2].text.strip()
    rating = columns[3].text.strip()
    player_data.append((team, rating))

df = pd.DataFrame(player_data, columns=['Team', 'Rating'])
df


# In[86]:


all_rounder_data = []
table = soup.select_one('.table')

# Find all the rows in the table
rows = table.select('tr')

# Loop through each row (excluding the header row) up to 10 rows
for row in rows[1:11]:
    # Find all the columns in the row
    columns = row.select('td')
    team = columns[2].text.strip()
    rating = columns[3].text.strip()
    all_rounder_data.append((team, rating))

df = pd.DataFrame(all_rounder_data, columns=['Team', 'Rating'])
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


#7)	Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame- i) Headline ii) Time 
#iii) News Link


# In[94]:


page =requests.get('https://www.cnbc.com/social-media/')


# In[95]:


soup=BeautifulSoup(page.content)
soup


# In[ ]:





# In[96]:


headlines=[]

for i in soup.find_all('a',class_="Card-title"):
    headlines.append(i.text)

headlines
    


# In[97]:


time=[]

for i in soup.find_all('span',class_="Card-time"):
    time.append(i.text)
time


# In[103]:


news_links = []

# Find all the news link elements
for link in soup.find_all('a', class_='Card-title'):
    news_links.append(link['href'])

print(news_links)


# In[104]:


import pandas as pd
df=pd.DataFrame({'newslinks':news_links,'headlinesss':headlines,'times':time})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#8)	Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame- i) 	Paper Title ii) 	Authors iii) 	Published Date iv) 	Paper URL 


# In[116]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[117]:


soup=BeautifulSoup(page.content)
soup


# In[118]:


paper_title=[]

for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)

paper_title


# In[119]:


publish_date=[]

for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    publish_date.append(i.text)
    
publish_date


# In[120]:


authors_name=[]

for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    authors_name.append(i.text)

authors_name


# In[127]:


paper_url=soup.find_all('href')
paper_url

for link in soup.find_all('a'):
    print(link.get('href'))


# In[130]:



links = [link.get('href') for link in soup.find_all('a')]

# Filter out the links of articles only
article_links = [link for link in links if link.startswith('https://www.sciencedirect.com/science/article')]

print(article_links)


# In[133]:


print(len('publish_date'))


# In[136]:


import pandas as pd
df=pd.DataFrame({'paper_titles':paper_title,'author_names':authors_name,'paper_url':article_links})
df


# In[ ]:





# In[ ]:





# In[ ]:


#•	Write a python program to scrape mentioned details from dineout.co.in and make data frame- i) Restaurant name 
#ii)	Cuisine 
#iii)	Location iv) 	Ratings 
#	v) 	Image URL 


# In[238]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants')


# In[239]:


soup = BeautifulSoup(page.content)
soup


# In[240]:


#scraping the name from the site
rest_name = []
     
for i in soup.find_all('a', class_="restnt-name ellipsis"):
        rest_name.append(i.text)
        
rest_name


# In[241]:


loc = []

for  i in soup.find_all('div',class_="restnt-loc ellipsis"):
      loc.append(i.text)
loc


# In[242]:


images = []
 
for i in soup.find_all('img',class_="no-img"):
    images.append(i.get('data-src'))
    
images


# In[250]:


rating=[]
 
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[244]:


cuisines = []

for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisines.append(i.text.split('|')[1].strip())
    
cuisines


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[251]:


import pandas as pd
df=pd.DataFrame({'name':rest_name,'location':loc,'images_url':images,'ratings':rating,'cuisiness':cuisines})
df


# In[252]:


print(len('rating'))


# In[253]:


print(len(rest_name))
print(len(loc))
print(len(images))
print(len(rating))
print(len(cuisines))


# In[ ]:





# In[ ]:





# In[ ]:




