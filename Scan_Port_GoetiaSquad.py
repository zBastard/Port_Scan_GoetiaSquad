import os
import colorama
from colorama import Fore
import ctypes 
import socket
import webbrowser

opt12 = "Inserte aqui la direccion IP >> "

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("πΎπ ππ₯ππππ’π¦ππ ππ π π")

def inicio():
	print(Fore.RED+"κ±α΄α΄Ι΄α΄Κ α΄α΄ α΄α΄α΄Κα΄α΄κ± |πΎππΌπππΈ|")
	print("")
	print(Fore.BLUE+"α΄α΄α΄α΄α΄ ΚΚ α΄Κα΄κ±α΄α΄Κα΄0")
	print("")
	print(Fore.CYAN+"πΌππππΌ πβ πππ»π")
	print("")
	print(Fore.BLUE+"1. πΎβππΌπ½πβπΎ")
	print(Fore.BLUE+"2. π»πππβπΎ")
	print("")
	inicio1 = input(Fore.WHITE+"κ±α΄Κα΄α΄α΄Ιͺα΄Ι΄α΄ α΄Ι΄ α΄α΄α΄α΄ >> ")
	if inicio1 == "1":
		os.system("cls")
		return main()
	if inicio2 == "2":
		os.system("cls")
		return doxing()
	else:
		os.system("cls")
		print(Fore.RED + "Β‘ππ πππππ  ππ£π£π πππ !")
		print("")
		GoetiaSquad = input(Fore.YELLOW + "α΄α΄Κκ±α΄ α΄Ι΄α΄α΄Κ α΄α΄Κα΄ α΄ α΄Κα΄ α΄Κ α΄Κ α΄α΄Ι΄α΄...")
		print("")
		return inicio1()

def main():
    print(Fore.LIGHTWHITE_EX + """
    βββββββββββββββββββββββββββββββββββββββββββββ   
    βββββββββββββββββββββββββββββββββββββββββββββ 
    βββββββββββββββββββββββββββββββββββββββββββββ 
    βββββββββββββββββββββββββββββββββββββββββββββ
    βββββββββββββββββββββββββββββββββββββββββββββ
    βββββββββββββββββββββββββββββββββββββββββββββ  
                                                           
                                                           
     """)

    print(Fore.LIGHTRED_EX + "ππ π π ππ πΎπ ππ₯ππππ’π¦ππ" + Fore.YELLOW)
    print(Fore.LIGHTRED_EX + "α΄ α΄Κκ±ΙͺΓ³Ι΄ 3.3.3.3.3 | βπ πππ ππͺ ππΉππ€π₯ππ£ππ")
    print()
    print(Fore.LIGHTRED_EX + "(1) Ι΄α΄α΄α΄")
    print(Fore.LIGHTRED_EX + "(2) κ±α΄Κα΄α΄α΄ΙͺΙ΄Ιͺα΄κ±")
    print(Fore.LIGHTRED_EX + "(3) α΄α΄α΄Κα΄α΄κ± α΄α΄ α΄α΄α΄ΙͺΙ΄Ιͺα΄κ±")
    print(Fore.LIGHTRED_EX + "(4) α΄α΄Ι΄κ±α΄Ι’α΄ΙͺΚ Ιͺα΄ α΄α΄ α΄Ι΄ α΄α΄α΄ΙͺΙ΄Ιͺα΄")
    print(Fore.LIGHTRED_EX + "(5) α΄α΄Ι΄α΄Κ α΄α΄Κ α΄Κα΄α΄α΄α΄Κ α΄α΄ Κα΄ α΄α΄α΄Κ")
    print("")

    menu = input(Fore.LIGHTWHITE_EX + "ΙͺΙ΄κ±α΄Κα΄α΄ α΄Ι΄α΄ α΄α΄α΄ΙͺΓ³Ι΄ >> ")

    if menu == "1":

    	nmap()

    if menu == "2":

    	subdomains()

    if menu == "3":

    	puertos()

    if menu == "4":

        os.system ("cls")
        asd = input (Fore.LIGHTRED_EX + "[πΎπ ππ₯ππππ’π¦ππ ππ π π] Inserte aqui la direccion IP >> " + Fore.LIGHTBLACK_EX)
        print()
        dsa = socket.gethostbyname(str(asd))
        print (Fore.LIGHTWHITE_EX+ "La direccion IP es >> " + Fore.LIGHTRED_EX + str(dsa))

        print()
        menu2331 = input(Fore.LIGHTWHITE_EX + "Presione la tecla intro para volver al menu...")

        os.system("cls")

        main()

    if menu == "5":
    	
    	webbrowser.open("https://www.youtube.com/channel/UCJSwZnPIN8Lx7M9hWhO8D9A", new=2, autoraise=True)
    	os.system("cls")
    	main()
    else:
        
        os.system("cls")
        print(Fore.LIGHTRED_EX + "Β‘Has introducido un numero incorrecto!")
        print()
        menu22331 = input(Fore.LIGHTWHITE_EX + "Presiona la tecla intro para volver al menu...")

        os.system("cls")

        main()

def nmap():
	os.system("cls")     
	print ("")    
	print ("")
	print ("")
	print (Fore.LIGHTMAGENTA_EX + "1) Rango bajo (1-1000)")
	print (Fore.LIGHTMAGENTA_EX + "2) Rango Medio (1-25600)")
	print (Fore.LIGHTMAGENTA_EX + "3) Rango alto (1-65535)")
	print ("")
	x = input(Fore.LIGHTWHITE_EX + 'Seleciona una opcion>> ')
	if x == "1":
		os.system("cls")
		choice = input(Fore.LIGHTWHITE_EX + "Introduzca una IP >> " "")
		print(Fore.LIGHTGREEN_EX)
		os.system("nmap -p 1-1000 -T5 -v -A -Pn " + (choice))
		print()
		menu123 = input(Fore.LIGHTRED_EX + "El escaneo a finalizado, pulse intro para volver al menu...")
		os.system("cls")
		main()
	elif x == "2":
		os.system("cls")
		choice1 = input(Fore.LIGHTWHITE_EX + "Introduzca una IP >> " "")
		print(Fore.YELLOW)
		os.system("nmap -p 1-25600 -T5 -v -A -Pn " + (choice1))
		menu1234 = input(Fore.LIGHTRED_EX + "El escaneo a finalizado, pulse intro para volver al menu...")
		os.system("cls")
		main()
	elif x == "3":
		os.system("cls")
		choice2 = input(Fore.WLIGHTWHITE_EX + "Introduzca una IP >> " "")
		print(Fore.YELLOW)
		os.system("nmap -p 1-65535 -T5 -v -A -Pn " + (choice2))
		menu12345 = input(Fore.LIGHTRED_EX + "El escaneo a finalizado, pulse intro para volver al menu...")
		os.system("cls")
		main()



def subdomains():

	os.system("cls")
	print()
	print()
	subdomains0 = ["www", "ovh-birdmc", "cpanel", "ns-vps", "d", "t", "short", "jar", "iptables", "ufw", "recuperar", "baneados", "imagenes", "samp", "social", "holo", "donaciones", "shoprp", "wow", "multicraft", "mail", "radio3", "radio2", "fr", "teamdub", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "docker", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "web", "dev", "tv", "deposito", "depositos", "extra", "extras", "bungee1", "torneoyt", "hcf", "uhc5", "uhc4", "uhc3", "uhc2", "uhc1", "uhc", "dedicado5", "dedicado4", "dedicado3", "dedicado2", "ded5", "ded4", "ded3", "ded2", "ded1", "ded", "gamehitodrh", "servidor4", "webmail", "monitor", "servidor001", "servidor10", "servidor9", "servidor8", "servidor7", "servidor6", "servidor5", "servidor4", "servidor3", "hvokfcic7sm", "autodiscover", "tauchet", "hg10", "ping", "hg9", "hg8", "hg7", "hg6", "hg5", "hg4", "hg3", "hg2", "hg1", "tienda", "status", "ayuda", "playstation", "home", "job", "firewall", "rank", "mantenimiento", "beta", "pay", "private", "port", "bb", "stor", "mx5", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "translations", "staff", "help", "render", "ts3", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "sv3", "sv2", "sv1",  "vps", "build", "web", "dev", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh", "ts"]
	victima0 = input (Fore.RED + "[SUBDOMAINS TOOL] Inserte el dominio >> " + "" + Fore.LIGHTWHITE_EX+"")
	print()
	for ejecutar0 in subdomains0:
		try:
			ipserver0 = str(ejecutar0)+"."+str(victima0)
			iphost0 = socket.gethostbyname(str(ipserver0))
			print (Fore.LIGHTRED_EX+"[SUBDOMAIN TOOL] (πΎπ ππ₯ππππ’π¦ππ) SUBDOMAINS FOUNDS >> "+Fore.LIGHTRED_EX+""+str(ejecutar0)+"."+str(victima0)+" >> "+Fore.LIGHTRED_EX+""+str(iphost0))
		except:
			pass

	menu2332 = input(Fore.LIGHTWHITE_EX + "El scan de subdomains a finalizado, presione intro para volver al menu...")

	os.system("cls")

	main()

def puertos():
	os.system("cls")
	puerto = input(Fore.LIGHTWHITE_EX + "Introduzca la IP >> ")
	print(Fore.LIGHTRED_EX)
	os.system("nmap -p 1-65535 -T5 -v -A -Pn " + (puerto))
	print()
	print()
	print(Fore.LIGHTRED_EX + "ESCANEO COMPLETADO!!!!")
	
	volver = input(Fore.LIGHTWHITE_EX + "Presiona la tecla intro para volver al menu ...")
	
	os.system("cls")
	
	main()

def doxing():
	pass
	
os.system("cls")
main()