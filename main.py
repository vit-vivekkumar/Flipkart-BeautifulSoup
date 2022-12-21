import pandas as pd
import requests
from bs4 import BeautifulSoup

product_title=[]
prices=[]
rating=[]

for i in range(2,5):
	url='https://www.flipkart.com/search?q=mobile+phone+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+phone+under+10000%7CMobiles&requestId=9c0bd0f0-b02f-485d-bb45-862fbd551475&as-backfill=on&page='+str(i)
	r=requests.get(url)
	soup=BeautifulSoup(r.text,'lxml')

	items=soup.find("div",class_="_1YokD2 _3Mn1Gg")

	title=items.find_all('div', class_='_4rR01T')
	price=items.find_all('div', class_='_30jeq3 _1_WHN1')
	rate=items.find_all('div', class_='_3LWZlK')

	# print(title)
	# print(price)

	product_title
	for i in title:
		temp=i.text
		product_title.append(temp)
	print(product_title)


	#product_price
	for i in price:
		temp=i.text
		prices.append(temp)
	print(prices)


	#product_ratting
	for i in rate:
		temp=i.text
		rating.append(temp)
		print(temp)	

		
print(len(product_title))
print(len(prices))
print(len(rating))




df=pd.DataFrame({'product_title':product_title,'product_price':prices,'product_ratting':rating})
print(df)
