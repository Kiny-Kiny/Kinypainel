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
    pausa = input('Pressione enter para retornar')

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
    else:
        pass
