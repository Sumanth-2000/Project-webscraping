import requests
import pandas as pd
from bs4 import BeautifulSoup
r=requests.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
c=r.content
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class': 'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
