#!/usr/bin/env python

import re
import sys
import socket

# !!!!!!!!!!!!!!!  reste a faire parcours recursif des pages web

#traduction du domaine en ip
def host_to_ip (host):
	addr = socket.gethostbyname(host)
	return addr
	
# recherche des emails dans les pages
def scan_mail (host):
	data = requests.get(host)
	emails = ""
	for email in re.findall(r'(\w+@\w+\.com)', data):
		if emails == "":
			emails = email
		else:
			emails = emails + ";" + email
	return emails
			
# recherche des numeros de telephone dans les pages
def scan_tel (host):
	data = requests.get(host)
	num_tels = ""
	for num_tel in re.findall(r'^(\d{2})\D+(\d{2})\D+(\d{2})\D+(\d+)$', data):
		if num_tels == "":
			num_tels = num_tel
		else:
			num_tels = num_tels + "&" + num_tel
	return num_tels

# scan de port sur les machine du domaine
def scan_port (host):
	ip = host_to_ip(host)
	site = ip.split(".")
	port_list = open("nmap_ports.conf","r") #les ports sont stocker de <un_protocole>:<un_port> (tcp:...)(udp:...)(all:...)
	p_var = ""
	for ligne in port_list:
		word = ligne.split(":")
		word = word.upper()
		if word[0] == "TCP":
			if p_var == "":
				p_var = "T:"+word[2]
			else:
				p_var = ",T:"+word[2]
		if word[0] == "UDP":
			if p_var == "":
				p_var = "U:"+word[2]
			else:
				p_var = ",U:"+word[2]
		if word[0] == "ALL":
			if p_var == "":
				p_var = word[2]
			else:
				p_var = ","+word[2]
	ip_var = site[0] + "." + site[1] + "." + site[3] + ".1-254"
	result = nmap ip_var -p p_var -sV -Pn
	return result

# envoi un email
def send_mail (dest,mails,phones,res_ports):
	msg = MIMEMultipart()
	email_src = raw_input("Enter your email : ")
	msg['From'] = email_src
	email_dst = raw_input("Enter destination email : ")
	msg['To'] = email_dst
	msg['Subject'] = '[CDAISI][FC][TP7] log automatique Guillaume GRONNIER'
	message = "emails trouvés :"
	mails = mails.spilt(";")
	for mail in mails:
		message = message + "  " + mail
	message = message + "\n" + "numéros de téléphone trouvés :" 
	for phone in phones:
		message = message + "  " + phone 
	message = message + "\n" + "ports ouverts trouvés et services associés : " + res_ports
	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP('smtp.gmail.com',587)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	password = raw_input("Enter your mail password")
	mailserver.login(email_src,password)
	mailserver.sendmail(email_src,email_dst,msg.as_string())
	mailserver.quit()

# main
site = raw_input("adresse du site : ")
mail = scan_mail(site)
phone = scan_tel(site)
res_port = scan_port(site)
email_dest = raw_input("destination email : ")
send_mail(email_dest,mail,phone,res_port)
