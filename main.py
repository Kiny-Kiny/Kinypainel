global R,B,C,Y,G,RT,CY,CO
CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
## Distribuido livremente pela licença MIT,
## Aos que não sabem o que isso significa,sugerimos estudo.
#######################
## Gostamos das suas atualizações no nosso github p0is0n,
## espero que você não fique bravo se usarmos elas,né?
## :p abraços,Yato e Kiny.
#######################
## Obrigado pelo apoio snuking
#######################

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
import os,sys,time,base64, json, re,tools,subprocess
try:
    import requests,api,platform,signal,atexit,argparse,random,hashlib,urllib3,html5lib,phonenumbers,json,tools
    from colorama import Fore, Style
    from bs4 import BeautifulSoup
    from phonenumbers import carrier
    from phonenumbers import geocoder
    from phonenumbers import timezone
    from urllib.parse import urlencode
    from fordev.generator import people
except:
    os.system('pip3 install requests phonenumbers urllib3 colorama bs4 html5lib argparse fordev')
    for i in range(3):
    	tools.clear()
    	print(f'{C}[{Y}i{C}] Reiniciando o painel em {i} seg...')
    	time.sleep(1)
    restart()

requests = requests.Session()
def clear_config():
	if os.path.exists('options.txt'):
    			try:
    				os.remove('options.txt')
    			except:
    				os.system('rm options.txt')

	if os.path.exists('user'):
    			try:
    				os.remove('user')
    			except:
    				os.system('rm user')

def write():
    clear_config()
    f = open('options.txt','a')
    f.write(str(login))
    f.write(str(cpf_api))
    f.write(str(ip_api))
    f.write(str(placa_api))
    f.write(str(cnpj_api))
    f.write(str(anim))
    f.write(str(menu_return))
    f.close()
    if os.path.exists('user'):
        os.remove('user')
    f = open("user","a")
    f.write(user)
    f.close

global login
global user
global cpf_api
global ip_api
global placa_api
global cnpj_api

if os.path.exists('options.txt') and os.path.exists('user'):
    f = open('options.txt','r') # Não espero que vc se ache hacker por saber mexer com esse arquivo
    data = f.read()
    login = int(data[0])
    cpf_api = int(data[1])
    ip_api = int(data[2])
    placa_api = int(data[3])
    cnpj_api = int(data[4])
    anim = int(data[5])
    menu_return = int(data[6])
    f.close()
    f = open('user','r')
    user = f.read()
    f.close()
    del data
else:
    login = '1' # Não,eu não vou reclamar por você ter corrompido a data :D
    user = 0
    cpf_api = 0
    ip_api = 0
    placa_api = 0
    cnpj_api = 0
    menu_return = 0
    anim = 0

token = ["f01e0024a26baef3cc53a2ac208dd141"]
welcome_msg = ["Que a força esteja com você", "Bem vindo", "Você é um mito", "Okaerinasai"]

if __name__ == '__main__':
    print(f'{G} Checando por atualizacoes... {C}')
    update = subprocess.check_output('git pull', shell=True)
    if 'Already up to date' not in update.decode():
        print(f'{G}Atualizacao instalada!\nReiciando app...{C}')
        time.sleep(5)
        subprocess.run('clear')
        restart()
    else:
        print('Nenhuma atualizacao disponivel.')
        time.sleep(2)

if login == 1:
    tools.clear()
    user = input("USERNAME:  ")
    snh = 'VirtualInsanity'
    if input("PASSWORD:  ").strip() == snh:
        tools.clear()
    else:
        print("{C}[{R}ERROR{C}] Wrong Password....Yare Yare")
        if anim == 1:
            time.sleep(1)
        exit()
    print("\n ")
if user == 'YATO' or user == 'KINY':
    kinymode=1
    kiny=1
    print("Nova Opção Desbloqueada")
else:
    kinymode=0

try:
    os.system("pkg update")
    os.system("pkg install figlet")
except:
    os.system("apt update")
    os.system("apt install figlet")

Sair = False
while(Sair == False):

    tools.clear()
    print(f"Coded By: {CY} KINY {CO} and {CY} YATO {CO} in 07/02/2021")
    print()
    os.system("figlet KINY")
    print(f'{C}[{G}*{C}]'+random.choice(welcome_msg)+' '+user+'!')
    if anim == 1:
        time.sleep(1)
    print()
    print(f"{C}{G}[1]{C} BUSCADOR DE CEP")
    print(f"{C}{G}[2]{C} GEO LOCALIZADOR DE IP")
    print(f"{C}{G}[3]{C} KINY-SITE-INFOGA")
    print(f"{C}{G}[4]{C} CONSULTA DE CNPJ")
    print(f"{C}{G}[5]{C} CONSULTA BANCARIA")
    print(f"{C}{G}[6]{C} CONSULTA CPF")
    print(f"{C}{G}[7]{C} CONSULTA CNS")
    print(f"{C}{G}[8]{C} CONSULTA PLACA")
    print(f"{C}{G}[9]{C} CONSULTA CRM")
    print(f"{C}{G}[10]{C} CONSULTA DE NUMERO")
    print(f"{C}{G}[11]{C} CONSULTA BIN")
    print(f"{C}{G}[12]{C} GERAR PESSOA")
    print(f"{C}{G}[13]{C} MOSTRAR MEU IP")
    print(f"{C}{G}[14]{C} CC CHECKER")
    print(f"{C}{G}[15]{C} COVID19")
    if kinymode == 1:
    	print(f"{C}{G}[16]{C} FERRAMENTAS")
    if anim==1:
        time.sleep(1)
    print()
    if login:
    	pass
    else:
    	print(f"{C}{G}[95]{C} Mudar username")
    print(f"{C}{G}[96]{C} Opções")
    print(f"{C}{G}[97]{C} Notas de versão")
    #print("{C}[{G}98{C}] Auto-update")
    print(f"{C}{G}[99]{C} Update && Upgrade")
    print(f"{C}{G}[00]{C} EXIT")
    op = input("===>").strip()
    tools.clear()

    if op == '16' and kinymode == 1:
        os.system('figlet KINY')
        print()
        print(f'{C}[{G}1{C}] Gerar link whatsapp')
        print(f'{C}[{G}2{C}] Youtube downloader')
        print()
        choice = input('===>')
        if choice == '1' or choice == '01':
            tools.gerarlinkwhats()
        if choice == '2' or choice == '02':
            tools.youtube()

    if op == '95':
    	print()
    	print(f'{C}[{G}i{C}] Me diga como quer ser chamado.')
    	user = input('===>')
    	write()

    if op == '96':
            os.system('figlet KINY')
            print(f'{C}[{G}1{C}] Login : {login}')
            print(f'{C}[{G}2{C}] Trocar APIs')
            print(f'{C}[{G}3{C}] Limpar data')
            print(f'{C}[{G}4{C}] Animação: {anim}')
            #print(f'{C}[{G}5{C}] Inserir token pessoal')
            print(f'{C}[{G}5{C}] Modo retornar ao menu: {menu_return}')
            print()
            print(f'{C}[{G}0{C}] Voltar')
            choice = input('===>')
            tools.clear()
            if choice == '1' or choice == '01':
                login ^= 1
            if choice == '2' or choice == '02':
                lista_api_cpf = ["MTE","null"]
                cpf_api_name = (lista_api_cpf[cpf_api])
                lista_api_ip = ["IP-API 1","API-IP 2","Todas"]
                ip_api_name = (lista_api_ip[ip_api])
                lista_api_cnpj = ["receitaws","Governo","Todas"]
                cnpj_api_name = (lista_api_cnpj[cnpj_api])
                lista_api_placa = ["receitaws","Governo","Todas"]
                placa_api_name = (lista_api_placa[placa_api])
                print(f'{C}[{G}1{C}] CPF API: {cpf_api_name}')
                print(f'{C}[{G}2{C}] IP API: {ip_api_name}')
                print(f'{C}[{G}3{C}] PLACA API: {placa_api_name}')
                print(f'{C}[{G}4{C}] CNPJ API: {cnpj_api_name}')
                print()
                print(f'{C}[{G}0{C}] Voltar')
                choice2 = input('===>')

                if choice2 == '1' or choice2 == '01':
                    cpf_api = cpf_api + 1
                if choice2 == '2' or choice2 == '02':
                    ip_api = ip_api + 1
                if choice2 == '3' or choice2 == '03':
                    placa_api = placa_api + 1
                if choice2 == '4' or choice2 == '04':
                    cnpj_api = cnpj_api + 1

                if int(cpf_api) >= int('3'):
                    cpf_api = 0
                if int(cnpj_api) >= int('3'):
                    cnpj_api = 0
                if int(placa_api) >= int('3'):
                    placa_api = 0
                if int(ip_api) >= int('3'):
                    ip_api = 0
            if choice == '3' or choice == '03':
                clear_config()
            if choice == '4' or choice == '04':
                anim ^= 1
            if choice == '5' or choice == '05':
                menu_return ^= 1
            #if choice == '5' or choice == '05':
                #print(f'{C}[{G}i{C}] Digite o seu token de acesso ou d para o token de acesso publico.')
                #token_inn = input('===>')
                #if token_inn == d:
                #    token[0] = "f01e0024a26baef3cc53a2ac208dd141"
                #else:
                #    token[0] = token_inn
            if choice != 1 and choice !=2 and choice !=3 and choice!=4 and choice!=5 and choice!=0:
                tools.clear()
                print(f'{C}[{R}ERROR{C}] Opção inválida')
            write()

    if op == '97':
        tools.notes()

    if op == '15':
    	tools.covid19()

    if op == '14':
        tools.cc_checker()

    if op == '13':
    	tools.ip(ip_api,0)

    if op == '12':
        tools.gerar_pessoa(token)

    if op == '11':
        tools.bin()

    if op == '10':
        def consultaphone():
            api.phone()
            print(f'{C}[{Y}i{C}]Deseja realizar uma nova consulta?')
            print('1.Sim')
            print('2.Não')
            choice = input("===>")
            if choice == '1' or choice == '01':
                tiposop()
            if choice == '2' or choice == '02':
                pass
            else:
                print(f'{C}[{R}i{C}] Opção inválida')
                time.sleep(3)
                tiposop()
        def tiposop():
            tools.consultatel()

    if op == '9' or op == '09':
        tools.crm()

    if op == '8' or op == '08':
        tools.consultaplaca()

    if op == '7' or op == '07':
        tools.cns(token,anim)

    if op == '6' or op == '06':
        tools.consultacpf()

    if op == '5' or op == '05':
        tools.bank(anim)

    if op == '1' or op == '01':
        tools.cep(anim)

    if op == '00' or op == '0':
        os.system("clear")
        Sair = True

    if op == '99' or op == '99':
        os.system("clear")
        os.system("pkg update && pkg update")
        pass

    if op == '3' or op == '03':
        tools.kiny_infoga()

    if op == '2' or op == '02':
        mode = 1
        tools.ip(ip_api,mode)

    if op == '4' or op == '04':
        os.system('figlet KINY')
        print(f'''
{C}[{Y}i{C}] O QUE DESEJA FAZER?
{C}[{G}1{C}] GERAR CNPJ
{C}[{G}2{C}] CONSULTAR CNPJ
        ''')
        kct = input("===> ")
        tools.cnpj(kct,token,anim)
os.system('rm -rf __pycache__')
print(f'{C}{R} Arrivederci{C}')
