import urllib.request
import urllib.parse
import re
import bs4 as bs
import config

sauce = list()
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Ratusz').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Koszary').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Stajnia').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Warsztat').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Ku%C5%BAnia').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Plac').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Rynek').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Tartak').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Cegielnia').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Huta_%C5%BCelaza').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Zagroda').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Spichlerz').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Mur_obronny').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Pa%C5%82ac').read())
sauce.append(urllib.request.urlopen('https://help.plemiona.pl/wiki/Piedesta%C5%82').read())
v = len(sauce)
for wrr in range(v):
	wood = list()
	stone = list()
	iron = list()
	workers = list()

	soup = bs.BeautifulSoup(sauce[wrr], 'lxml')

	table = soup.find('table', class_="wikitable")
	table_rows = table.find_all('tr')
	for tr in table_rows:
		td = tr.find_all('td')
		row = list()
		x=0

		for i in td:
			row.append(i.text)
			if x == 1:
				text=i.text
				text=text.replace('.','')
				try:
					wood.append(int(text))
				except:
					print("skip")
			elif x == 2:
				text=i.text
				text=text.replace('.','')
				try:
					stone.append(int(text))
				except:
					print("skip")
			elif x == 3:
				text=i.text
				text=text.replace('.','')
				try:
					iron.append(int(text))
				except:
					print("skip")
			elif x == 4:
				text=re.search(' *[0-9]*',i.text).group()
				try:
					workers.append(int(text))
				except:
					print("skip")

			x+=1
	config.wood_list.append(wood)
	config.stone_list.append(stone)
	config.iron_list.append(iron)
	config.workers_list.append(workers)		

print(config.wood_list)
print('----------------------------------------------------')
print(config.stone_list)
print('----------------------------------------------------')
print(config.iron_list)
print('----------------------------------------------------')
print(config.workers_list)
print('----------------------------------------------------')