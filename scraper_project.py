from bs4 import BeautifulSoup 
import requests 
import pandas as pd 

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars" 
PAGE=requests.get(START_URL) 

soup = BeautifulSoup(PAGE.text, 'html.parser') 
print(soup.prettify()) 
star_table = soup.find('table') 

temp_list= [] 
table_rows = star_table.find_all('tr') 

for tr in table_rows: 
    td = tr.find_all('td') 
    row = [i.text.rstrip() for i in td] 
    temp_list.append(row) 
Star_names = [] 
Distance =[] 
Mass = [] 
Radius =[] 
Lum = [] 
Magnitude = []
Spectral =[]
Bayer = []
for i in range(1,len(temp_list)): 
    Magnitude.append(temp_list[i][0])
    Star_names.append(temp_list[i][1]) 
    Bayer.append(temp_list[i][2]) 
    Distance.append(temp_list[i][3]) 
    Spectral.append(temp_list[i][4]) 
    Mass.append(temp_list[i][5]) 
    Radius.append(temp_list[i][6]) 
    Lum.append(temp_list[i][7]) 
    df2 = pd.DataFrame(list(zip(Magnitude,Star_names,Bayer,Distance,Spectral,Mass,Radius,Lum)),columns=['Magnitude','Star_name','Bayer','Distance','Spectral','Mass','Radius','Luminosity']) 

print(df2) 
df2.to_csv('bright_stars_2.csv')