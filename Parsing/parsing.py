f = open('G:/Textbook-Sem5/BT3051 Data Structures and Algorithms/Class Problems/Turing Award - Wikipedia.html','r')
from bs4 import BeautifulSoup
soup = BeautifulSoup(f,'html.parser')
# print(soup.find_all("title"))
# for string in soup.find_all('a'):
#     print(string.get('title'))
# print(soup.get_text())
listofnames = []
z = soup.find_all('table')[1].find_all('td')
for elem in z:
	links = elem.find_all('a')
	if len(links)==1:
		if str(links).find('"image"')!=-1:
			continue
		if str(links).find('cite')!=-1:
			continue
		listofnames.append(links[0].get_text())
print(listofnames)