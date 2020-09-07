f = open('G:/Textbook-Sem5/BT3051 Data Structures and Algorithms/Class Problems/Avengers_ Endgame - Wikipedia.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(f,'html.parser')
# print(soup.prettify())

# for table in soup.find_all('table'):
# 	try:
# 		bb = str(table.a.text)
# 	except Exception as e:
# 		pass
	
# 	print(bb)
plot = soup.h2.find('span', id='Plot')
try:
	summary = plot.p.text
except Exception as e:
	summary=''

print(summary)