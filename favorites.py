import sqlite3
import webbrowser

conn = sqlite3.connect(':memory:')  # vytvorenie prepojenia na sqlite3, meno databázy bude memory
# conn = sqlite3.connect('favs.db')  # iný spôsob s vytvorením súboru s databázou

c = conn.cursor()

# vytvorenie tabuľky s názvom favorites v databáze, názov je typu TEXT a url je typu TEXT
c.execute('''CREATE TABLE IF NOT EXISTS favorites
	(title TEXT, url TEXT)''')

# 2.3
# vloženie prvého riadka do tabuľky
def add_fav(title, url):
	# c.execute('''INSERT INTO favorites (title, url)
	#	VALUES ('w', 'https://webyxl.com')''')
	c.execute('''INSERT INTO favorites (title, url)
		VALUES (?, ?)''', (title, url))
# ešte to treba commitnúť do databázy
	conn.commit()

# 2.4
# zmazanie riadka z tabuľky
def remove_fav(title):
	c.execute('''DELETE FROM favorites WHERE title=?''', (title,))
	conn.commit()

# 2.2 vytvorenie funkcie ktorá vypíše celú tabuľku
def get_favs():
	# už je vytvorená tabuľka, ale aby sme ju videli musíme mať príkaz SELECT *
	c.execute('''SELECT * FROM favorites''')
	# vybrať všetko a vložiť do results
	# results = c.fetchall
	return c.fetchall()

# print(results)
# 2.1 vytvorenie funkcie ktorá otvorí vybranú stránku podľa vpísanej skratky-short
cut-tu je to "title" z tabuľky
def get_fav(title):
	c.execute('''SELECT * FROM favorites WHERE title=?''', (title,))
		# v zátvorke je to, čo chceme nahradiť na miesto otáznika. Aby to bolo tupple, dáme za to čiarku
	return c.fetchone()  # return tupple

# potom dať run 'favorites' pre skontrolovanie

#-----------------------------------------------------------------------------------

# 1. vytvorenie úvodných inštrukcií programu pomocou While True:

# prvý spôsob zápisu While True
# while True:  # bude sa opakovať dookola, kým niekto neskončí aplikáciu
# 	print('v to visit a favorite, ls for list, add for new, '
# 		'rm to delete , q to quit: ')  # toto vypíše na začiatku, za dvojbodku sa vpisuje input
# 	input()

# druhý spôsob zápisu While True. Text je priamo vo funkcii input a celé vložené do premennej response
while True:  # bude sa opakovať dookola, kým niekto neskončí aplikáciu
	response = input('v to visit a favorite, ls for list, add for new, '
		'rm to delete , q to quit: ')  # toto vypíše na začiatku, za dvojbodku sa vpisuje input
#	print(response)

# potom dať run 'favorites' pre skontrolovanie

# 2. priradenie funkcií k skratkám v, ls, add, rm, q v inštrukciách:
# 2.1
	if response == 'v':
		# print('visiting...')
		# webbrowser.open('https://google.com')
		# namiesto print a webbrowser.open použijeme funkciu
		shortcut = input("What is the shortcut?:  ")  # to čo sa vpíše, sa potom vloží do premennej shortcut
		record = get_fav(shortcut)  # vykoná sa funkcia get_fav s premennou shortcut ako "title" a výsledok sa vloží do record
		print(record)  # toto vypíše obsah tabuľky
		try:  # try použijeme aby nám nevyhadzovalo Exception Error ak nenájde dtránku
			webbrowser.open(record[1])  # record vypíše všetko z tabuľky, record[1] vypíše druhý stĺpec, čiže url adresu
		except:
			print("Cannot open")
# 2.2
	elif response == 'ls':
		# print('listing')
		# print(results)
		print(get_favs())
# 2.3
	elif response == 'add':
		# print('adding')
		destination = input('Where do you want this shortcut to go?: ')
		shortcut = input('What is the shortcut?: ')
		add_fav(shortcut, destination)
# 2.4
	elif response == 'rm':
		#print('removing')
		shortcut = input('What is the shortcut?: ')
		remove_fav(shortcut)
	elif response == 'q':
		break
