global R,B,C,Y,G,RT,CY,CO
CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
import os,base64,requests,time,json

a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
a=a.encode('ascii')
a=base64.b64decode(a)
a=a.decode('ascii')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def notes():
    print(f'{C}==={R}{C} Notas de versão {C}==={R}{C}')
    print(f'''
-Novas APIs
-Configurações-
-Modo sem senha-
-Remoção de opção inútil-
-Otimização do código
-Nova opção no menu
    Agradecemos ao P0is0n pelo novo método de atualização e
        pelas boas vindas a comunidade OpenSource
    ''')
    print(f'{C}{B}YATO{C} & {C}{B}KINY{C} , 2021')
    pause = input('Pressione enter para retornar.')

def covid19():
    os.system('figlet KINY')
    print(f'{C}[{Y}i{C}] Informe o UF. Exemplo: sp, pa, ba ')
    choice = input('===>')
    data = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(choice)).json()
    clear()
    os.system('figlet KINY')
    print("Data e horario local: {}".format(data['datetime']))
    print("Estado: {}".format(data['state']))
    print("UF: {}".format(data['uf']))
    print("UID: {}".format(data['uid']))
    print("Casos: {}".format(data['cases']))
    print("Mortes: {}".format(data['deaths']))
    print("Suspeitas: {}".format(data['suspects']))
    print("Recusados: {}".format(data['refuses']))
    pausa = input('Pressione enter para retornar ao menu.')

def ip(ip_api,mode):
    os.system('figlet KINY')
    if ip_api == 1:
        if mode == 0:
            data = requests.get('http://ip-api.com/json/')
        else:
            ip_input = input("===>")
            data = requests.get('http://ip-api.com/json/{}'.format(ip_input))
        adress_data = data.json()
        weather_data = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=25d800a8b8e8b99d77c809567aa291b8')
        weather = json.loads(weather_data.text)
        if (adress_data['status']) == 'success':
            print('IP: {}'.format(adress_data['query']))
            print('Status: {}'.format(adress_data['status']))
            print('Pais: {}'.format(adress_data['country']))
            print('Regiao: {}'.format(adress_data['regionName']))
            print('Cidade: {}'.format(adress_data['city']))
            print('ZIP: {}'.format(adress_data['zip']))
            print('Latitude: {}'.format(adress_data['lat']))
            print('Longitude: {}'.format(adress_data['lon']))
            print('Fuso-Horarro: {}'.format(adress_data['timezone']))
            print('Internet-Info: {}'.format(adress_data['as']))
            print('ISP: {}'.format(adress_data['isp']))
            print('ORG: {}'.format(adress_data['org']))
            #print('Temperatura: {}'.format(weather["weather"]["main"]))
    else:
        print('another API')
    print(f"{C}[{Y}i{C}]DESEJA LOCALIZAR UM NOVO IP?")
    print(f"{C}{G}[1]{C} Sim")
    print(f"{C}{G}[2]{C} Não")
    vi = input('===> ')
    if vi == '1' or vi == '01':
        clear()
        ip(ip_api,mode)

def bin():
    os.system('figlet KINY')
    print('Exemplo:45717360')
    print(f'{C}[{Y}i{C}] Digite a BIN.')
    bin_input = input("===>")
    headers = {"Accept-Version":"3","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    try:
        req = requests.get('https://lookup.binlist.net/'+bin_input,headers = headers)
        req_data = req.json()
    except:
        print(f'{C}[{R}i{C}] Ocorreu um erro,tente novamente.')
        clear()
        os.system('figlet KINY')
        print('Bandeira: {}'.format(req_data['scheme']))
        print('Marca: {}'.format(req_data['brand']))
        print('Tipo: {}'.format(req_data['type']))
        print('Pais: {}'.format(req_data['country']['name']))
        print('Latitude: {}'.format(req_data['country']['latitude']))
        print('Longitude: {}'.format(req_data['country']['longitude']))
        print('Moeda: {}'.format(req_data['country']['currency']))
        print('Emoji: {}'.format(req_data['country']['emoji']))
        print(f'{C}[{Y}i{C}] Deseja realizar uma nova consulta?')
        print('1.Sim')
        print('2.Não')
        choice = input("===>")
        if choice == '1' or choice == '01':
            consultabin()
        if choice == '2' or choice == '02':
            pass
        else:
            print(f'{C}[{R}i{C}] Opção inválida')
            time.sleep(3)
            pass

def crm():
    os.system("figlet KINY")
    print(f'{C}[{G}i{C}] Digite o numero do CRM.')
    crm_input = input("===>")
    print(f'{C}[{G}i{C}] Digite o UF.')
    uf_input = input("===>")
    url = 'https://www.consultacrm.com.br/api/index.php?tipo=crm&uf='+uf_input
    data = requests.get(url+'&q={}&chave=5072097263&destino=json'.format(crm_input))
    crm_data = data.json()
            #consultas = (crm_data['api_limite']) - (crm_data['api_consultas'])
    if (crm_data['status']) == "true":
                #print('Consultas restantes ='+consultas)
        try:
            print('CRM: {}'.format(crm_data["item"][0]["numero"]))
            print('Nome: {}'.format(crm_data["item"][0]["nome"]))
            print('UF: {}'.format(crm_data["item"][0]["uf"]))
            print('Situacao: {}'.format(crm_data["item"][0]["situacao"]))
            print('Profissão: {}'.format(crm_data["item"][0]["profissao"]))
        except:
            print(f'{C}[{R}*{C}] Erro! dados invalidos!')
            time.sleep(3)
            consultacrm()
    else:
        print(f'{C}[{R}i{C}] CRM invalido')

def gerar_pessoa(): #####REWORK
    print("refazer")

def consultaplaca():
    #http://api.masterplaca.devplank.com/v2/placa/{placa}/json
            os.system("figlet KINY")
            print(f'{C}[{G}i]{C}Digite o numero da placa.')
            placa_input = input("===>")
            req = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa_input), verify = False) # JSQ7436
            placa_data = req.json()
            tools.clear()
            os.system('figlet KINY')
            try:
                if (placa_data['codigoRetorno']) == "0":
                    print(f"{C}Ano: {B}{placa_data['ano']}{C}")
                    print(f"Data: {B}{placa_data['data']}{C}")
                    print(f"Modelo: {B}{placa_data['modelo']}{C}")
                    print(f"Ano do modelo: {B}{placa_data['anoModelo']}{C}")
                    print(f"Cor: {B}{placa_data['cor']}{C}")
                    print(f"Marca: {B}{placa_data['marca']}{C}")
                    print(f"Roubo/furto: {B}{placa_data['dataAtualizacaoRouboFurto']}{C}")
                    print(f"Situação: {B}{placa_data['situacao']}{C}")
                    print(f"Placa: {B}{placa_data['placa']}{C}")
                    print(f"Chassi: {B}{placa_data['chassi']}{C}")
                    print(f"UF: {B}{placa_data['uf']}{C}")
                    print(f"Município: {B}{placa_data['municipio']}{C}")
                    print(f"Modificada em: {B}{placa_data['dataAtualizacaoCaracteristicasVeiculo']}{C}")
                    print(f"Alarme atualizado: {B}{placa_data['dataAtualizacaoAlarme']}{C}")
                    print(f"Mensagem de retorno: {B}{placa_data['mensagemRetorno']}{C}")
                    print(f"Código de retorno: {B}{placa_data['codigoRetorno']}{C}")
                else:
                    print(f'{C}[{R}i]{C} Sem dados sobre.')
            except:
                print(f'{C}[{R}i{C}] Placa invalida')
                time.sleep(3)

def cns(token,anim):
    os.system('figlet KINY')
    print(f'''
{C}[{G}i{C}]Formas de operação
[{G}1{C}]Gerar CNS
[{G}2{C}]Consultar CNS
''')
    choice = input('===>')
    clear()
    if choice == '1' or choice == '01':
            print(f'{C}[{G}i{C}] Gerando CNS')
            cns=requests.request('GET','http://geradorapp.com/api/v1/cns/generate?token={}'.format(token)).json()
            cns2=cns['data']['number_formatted']
            entrada=cns['data']['number']
            print(f'{C}[{Y}i{C}] O CNS gerado foi: '+cns2)
            if anim == 1:
                time.sleep(1)
            print(f'{C}[{G}i{C}] Consultando CNS...')
    if choice == '2' or choice == '02':
        entrada = input('===>')
    if anim == 1:
        time.sleep(1)
    clear()
    cns_data = requests.get('http://geradorapp.com/api/v1/cns/validate/{}?token={}'.format(entrada,token)).json()
    try:
        print('Numero: {}'.format(cns_data["data"]["number"]))
        print('Mensagem: {}'.format(cns_data["data"]["message"]))
    except:
        print(f'{C}[{R}*{C}] CNS INVALIDO.')
def cep(anim):
    clear()
    os.system('figlet KINY')
    print(f'{C}[{G}i{C}] Informe o CEP.')
    cep_input = input("===>")
    if len(cep_input) != 8:
        print(f"{C}[{R}ERROR{C}] QUANTIDADE DE DIGITOS INVALIDA")
        time.sleep(3)
        cep(anim)

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    adress_data = request.json()
    clear()
    if 'erro' not in adress_data:
        os.system('figlet KINY')
        print('Cep: {}'.format(adress_data['cep']))
        print('Logradouro: {}'.format(adress_data['logradouro']))
        print('Complemento: {}'.format(adress_data['complemento']))
        print('Bairro: {}'.format(adress_data['bairro']))
        print('Cidade: {}'.format(adress_data["localidade"]))
        print('Estado: {}'.format(adress_data['uf']))
        print('IBGE: {}'.format(adress_data['ibge']))
        print('GIA: {}'.format(adress_data['gia']))
        print('SIAFI: {}'.format(adress_data['siafi']))
        print('DDD: {}'.format(adress_data['ddd']))
    else:
        print('{C}[{R}ERROR{C}] CEP INVALIDO.')
    print(f"{C}{G}DESEJA REALIZAR UMA NOVA CONSULTA?{C}")
    print(f"{C}[{G}1{C}] Sim")
    print(f"{C}[{G}2{C}] Não")
    option = input('===> ')
    if option == '1':
        cep(anim)

def kiny_infoga():
    os.system("apt install nmap whois")
    clear()
    os.system("figlet KINY")
    print()
    j = input("1 para HTTPS, 2 para HTTP:")
    k = input("Domain: ")
    if j == '1':
        print("URL: ""https://www." + k)
        os.system("nmap " + k)
        os.system("whois " + k)
    print()
    if j == '2':
        print("URL: ""http://www." + k)
        os.system("nmap " + k)
        os.system("whois " + k)
    print ("Pressione enter para voltar.")
    pause = input("====>")

def cnpj(kct,token,anim):
    clear()
    if kct == '1' or kct == '01':
        gen = "1"
    elif kct == '2' or kct == '02':
        os.system('figlet KINY')
        print("DIGITE O CNPJ SEM / . OU -")
        cnpj_input = input("===>")
        gen = 0
    else:
        print('Opção inválida')
        time.sleep(3)
        cnpj(token,anim)
    if gen == "1":
        print(f'{C}[{G}*{C}] Gerando CNPJ...')
        if anim == '1':
            time.sleep(1)
        cnpj_data=requests.get('http://geradorapp.com/api/v1/cnpj/generate?token={}'.format(token)).json()
        cnpj_input = (cnpj_data['data']['number'])
        cnpj_formatted=(cnpj_data['data']['number_formatted'])
        print(f'{C}[{Y}i{C}] O CNPJ gerado foi: {cnpj_formatted}')
    print(f'{C}[{G}i{C}] Consultando CNPJ... ')
    try:
        cnpj_data = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input)).json()
    except:
        print(f'{C}[{R}*{C}]Erro no servidor')
        cnpj_data = "message"

    if 'message' not in cnpj_data:
        tagain = '0'
        print("CNPJ: {}".format(cnpj_data['cnpj']))
        print("Atividade principal: {}".format(cnpj_data['atividade_principal'][0]['text']))
        print("Nome: {}".format(cnpj_data['nome']))
        print("CEP: {}".format(cnpj_data['cep']))
        try:
            print("Telefone: {}".format(cnpj_data['telefone']))
        except:
            pass
        try:
            print("Email: {}".format(cnpj_data['email']))
        except:
            pass
        print("Situação: {}".format(cnpj_data['situacao']))
        print("UF: {}".format(cnpj_data['uf']))
        print("Municipio: {}".format(cnpj_data['municipio']))
        print("Logradouro: {}".format(cnpj_data['logradouro']))
        print("Numero: {}".format(cnpj_data['numero']))
        print("Complemento: {}".format(cnpj_data['complemento']))
        print("Porte: {}".format(cnpj_data['porte']))
        print("Natureza: {}".format(cnpj_data['natureza_juridica']))
        print("Data de abertura: {}".format(cnpj_data['abertura']))
        print("Tipo: {}".format(cnpj_data['tipo']))
        print("Capital: {}".format(cnpj_data['capital_social']))
        try:
            print("===============================")
            print("pessoal: {}".format(cnpj_data['qsa'][0]['nome']))
            print("Cargo: {}".format(cnpj_data['qsa'][0]['qual']))
        except:
            pass
        try:
            print("pessoal: {}".format(cnpj_data['qsa'][1]['nome']))
            print("Cargo: {}".format(cnpj_data['qsa'][1]['qual']))
        except:
            pass
        try:
            print("Pessoal: {}".format(cnpj_data['qsa'][2]['nome']))
            print("Cargo: {}".format(cnpj_data['qsa'][2]['qual']))
        except:
            pass
    else:
        try:
            print(f'{C}[{R}ERROR{C}]'+'{}: CNPJ INVALIDO.'.format(cnpj_formatted))
        except:
            print(f'{C}[{R}ERROR{C}] Sem dados.')
        if gen == '1':
            del cnpj_data
            del cnpj_input
            del cnpj_formatted
            tagain='1'
            print(f'{C}[{Y}i{C}]Tentando novamente...')
            time.sleep(3)
            cnpj(kct,token,anim)
    if tagain == '0':
        print(f"{C}[{Y}i{C}] DESEJA REALIZAR UMA NOVA CONSULTA?")
        print(f"{C}[{G}1{C}] Sim")
        print(f"{C}[{G}2{C}] Não")
        lo = input('===> ')
        if lo == '1' or lo == '01':
            cnpj(kct,token,anim)

def bank(anim):
    clear()
    os.system("figlet KINY")
    print(f"{C}[{G}i{C}] DIGITE O CODIGO BANCARIO")
    print(f"{C}[{G}i{C}] Exemplo: 260")
    bank_input = input("=====>")
    clear()
    try:
        req = requests.get('https://brasilapi.com.br/api/banks/v1/{}'.format(bank_input))

        bank_data = req.json()

        if 'message' not in bank_data:
            os.system("figlet KINY")
            print("Código bancário: {}".format(bank_data['code']))
            print("Nome: {}".format(bank_data['name']))
            print("Nome completo: {}".format(bank_data['fullName']))
            print("ISPB: {}".format(bank_data['ispb']))
        else:
            print('{}: Código bancário inválido.'.format(bank_input))
    except:
         print(f'{C}[{R}ERROR{C}]Erro no servidor')
    print(f"{C}[{Y}i{C}] DESEJA CONSULTAR UM NOVO CODIGO BANCARIO? ")
    print(f"{C}[{G}1{C}] Sim")
    print(f"{C}[{G}2{C}] Não")
    kc = input("===> ")
    if kc == '01' or kc == '1':
        bank(anim)
