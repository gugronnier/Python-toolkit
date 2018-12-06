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
			if char in cesar_tab.keys():
				lenght = lenght + 1
	return lenght

# calcule la frequence d'apparition des differents caracteres et les range dans un tableau. Finalement elle retourne ce tableau.
def char_frequencies(val):
	alpha_count_tab=[]
	lenght = numberOfChar(val)
	for i in range(26):
		alpha_count_tab.append(0)
	for char in val:
		if char in cesar_tab.keys():
			alpha_count_tab[cesar_tab[char]] = alpha_count_tab[cesar_tab[char]] + 1
	for i in range(25):
		alpha_count_tab[i] = alpha_count_tab[i]*100/lenght
	return alpha_count_tab

# retourne l'index du carctere le plus present dans le texte passe en argument
def morePresent(val):
	frequencies = char_frequencies(val)
	index = 0
	for i in range(25):
		if (frequencies[index] > frequencies [i]):
			index = index
		else:
			index = i
	return index

# fonction principal qui est charge de "cracker" le chiffrement cesar utilise
def crack_chaine(val):
	val=minToMaj(val)
	index = morePresent(val)
	nbchar = numberOfChar(val)
	key = "nothing"
	if nbchar >= 70:
		key = getKeyFromValue(abs(cesar_tab["E"]-index))
	if nbchar >= 60 and nbchar < 70:
		key = getKeyFromValue(abs(cesar_tab["S"]-index))
	if nbchar >= 50 and nbchar < 60:
		key = getKeyFromValue(abs(cesar_tab["I"]-index))
	if key not in "nothing":
		decode_chaine(val,key)
	else:
		print "\n-------------\n text too short, it can't be decode with frequencies analysis \n-------------"
	

# fonction qui decode la chaine "val" en utilisant la cle "key" passe en argument et affiche le resultat
def decode_chaine(val,key):
	res=""
	for char in val:
		if char in cesar_tab.keys():
			new_index = (cesar_tab[char]-cesar_tab[key])%26
			new_char = getKeyFromValue(new_index)
			res=res+new_char
		else:
			res=res+char
	print("\n-------------\n result :")
	print(res)
	print "\n-------------"

# ------------------------------------------------------	
# MAIN
# ------------------------------------------------------
chaine = raw_input("Enter what you want crack : ")
crack_chaine(chaine)
	
		
