#!/usr/bin/env python

cesar_tab = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

# retourne le texte ou le caractere en majuscule
def minToMaj(val):
	return val.upper()

# recupere dans le dictionnaire "cesar_tab" la cle correspondant a la valeur passe en argument et la retourne
def getKeyFromValue(val):
	for cle in cesar_tab.keys():
		if cesar_tab[cle] == val:
			return cle

# calcule et retourne le nombre de caractere present dans la chaine passe en argument
def numberOfChar(val):
	lenght = 0
	for word in val.split(" "):
		for char in word:
			lenght = lenght + 1
	return lenght

# passe le cle sous forme de tableau pour permettre la manipulation
def initKeyTab(key):
	key_tab = []
	for char in key:
		key_tab.append(char)
	return key_tab

# fonction qui encode la chaine "val" en utilisant la cle "key" passe en argument et affiche le resultat	
def encode_chaine(val,key):
	val=minToMaj(val)
	res=""
	i=0
	key_tab = initKeyTab(key)
	for char in val:
		if char in cesar_tab.keys():
			if i == numberOfChar(key):
				i=0
			new_index = (cesar_tab[char]+cesar_tab[key_tab[i]])%26
			new_char = getKeyFromValue(new_index)
			res=res+new_char
			i=i+1
		else:
			res=res+char
	print(res)

# fonction qui decode la chaine "val" en utilisant la cle "key" passe en argument et affiche le resultat
def decode_chaine(val,key):
	val=minToMaj(val)
	res=""
	i=0
	key_tab = initKeyTab(key)
	for char in val:
		if char in cesar_tab.keys():
			if i == numberOfChar(key):
				i=0
			new_index = (cesar_tab[char]-cesar_tab[key_tab[i]])%26
			new_char = getKeyFromValue(new_index)
			res=res+new_char
			i=i+1
		else:
			res=res+char
	print(res)
	
#main

while 1:
	print("\n ********\n * Menu *\n ********")
	print(" 1 - Encode")
	print(" 2 - Decode")
	print(" 0 - Quit")
	print("")
	print("---------------------------")
	choice = raw_input("your choice : ")
	print("---------------------------")
	print("")
	if choice=="1":
		chaine = raw_input("Enter what you want encode : ")
		key = raw_input("Enter the key for encode : ")
		encode_chaine(chaine,key.upper())
	if choice=="2":
		chaine = raw_input("Enter what you want decode : ")
		key = raw_input("Enter the key for decode : ")
		decode_chaine(chaine,key.upper())
	if choice=="0":
		print("\n Exiting ... \n")
		break 
		
