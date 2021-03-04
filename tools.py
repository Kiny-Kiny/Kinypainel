global R,B,C,Y,G,RT,CY,CO
CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
import os,base64,requests,time,json,re

global a
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
    if ip_api == 0 or ip_api == 2:
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
    if ip_api == 1 or ip_api == 2:
        if mode == 1:
            ip_input = input("===>")
            api=requests.get('http://ipwhois.app/json/'+ip_input).json()
        if mode == 0:
            api=requests.get('http://ipwhois.app/json/').json()
        clear()
        os.system('figlet KINY')
        try:
            if ip_api == 1:
                print('IP: {}'.format(api['ip']))
            print('TIPO: {}'.format(api['type']))
            print('CONTINENTE: {}'.format(api['continent']))
            print('CÓDIGO DO CONTINENTE: {}'.format(api['continent_code']))
            print('PAIS: {}'.format(api['country']))
            print('CÓDIGO DO PAÍS: {}'.format(api['country']))
            print('PAIS: {}'.format(api['country']))
            print('CAPITAL DO PAIS: {}'.format(api['country_capital']))
            print('CÓDIGO TELEFÔNICO DO PAÍS: {}'.format(api['country_phone']))
            print('PAISES VIZINHOS: {}'.format(api['country_neighbours']))
            print('REGIÃO: {}'.format(api['region']))
            print('CIDADE: {}'.format(api['city']))
            print('LATITUDE: {}'.format(api['latitude']))
            print('LONGITUDE: {}'.format(api['longitude']))
            print('ASN: {}'.format(api['asn']))
            print('ORG: {}'.format(api['org']))
            print('ISP: {}'.format(api['isp']))
            print('HORÁRIO PADRÃO: {}'.format(api['timezone']))
            print('NOME DO HORÁRIO PADRÃO: {}'.format(api['timezone_name']))
            print('GMT: {}'.format(api['timezone_gmt']))
            print('MOEDA: {}'.format(api['currency']))
            print('CÓDIGO DA MOEDA: {}'.format(api['currency_code']))
            print('SIMBOLO DA MOEDA: {}'.format(api['currency_symbol']))
        except:
            print(f'{C}[{R}ERROR{C}] IP Inválido ')
            time.sleep(3)
            clear()
            ip(ip_api,mode)

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
        print(f'{C}[{R}ERROR{C}] Ocorreu um erro,tente novamente.')
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
        bin()
    elif choice == '2' or choice == '02':
        pass
    else:
        print(f'{C}[{R}ERROR{C}] Opção inválida')
        time.sleep(3)

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
    print(f'{C}[{G}i{C}] Deseja realizar uma nova consulta?')
    print('1.Sim')
    print('2.Não')
    choice = input("===>")
    if choice == "1" or choice == "01":
        crm()
    if choice == "2" or choice == "02":
        pass
    else:
        print("Opcao invalida.")

def gerar_pessoa(): #####REWORK
    print("refazer")

def consultaplaca():
    #http://api.masterplaca.devplank.com/v2/placa/{placa}/json
            os.system("figlet KINY")
            print(f'{C}[{G}i]{C}Digite o numero da placa.')
            placa_input = input("===>")
            req = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa_input), verify = False) # JSQ7436
            placa_data = req.json()
            clear()
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
                print(f'{C}[{R}ERROR{C}] Placa invalida')
                time.sleep(3)
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
            cns=requests.request('GET','http://geradorapp.com/api/v1/cns/generate?token={}'.format(token[0])).json()
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
    cns_data = requests.get('http://geradorapp.com/api/v1/cns/validate/{}?token={}'.format(entrada,token[0])).json()
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
        cnpj_data=requests.get('http://geradorapp.com/api/v1/cnpj/generate?token={}'.format(token[0])).json()
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
    if anim == '1':
        print(f'{C}[{G}i{C}] Consultando banco.')
        time.sleep(1)
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

def consultacpf():
    clear()
    cpf = 0
    os.system('figlet KINY')
    print(f"""
{C}[{G}i{C}] Formas de operação:
    1.Consultar CPF
    2.Gerar CPF e consultar
    3.Voltar
{C}[{Y}i{C}] Selecione a forma de operação.
""")
    choice=input(f'===>')
    if choice=='1' or choice == '01':
        cpf=input(f'{C}[{Y}i{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
        clear()
    elif choice=='2' or choice == '02':
        os.system('figlet KINY')
        print(f'{C}[{G}i{C}] Gerando CPF...')
        time.sleep(1)
        cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token={}'.format(token[0])).json()
        cpf2=cpf['data']['number_formatted']
        cpf=cpf['data']['number']
        print(f'{C}[{Y}i{C}] O CPF gerado foi: {B}'+cpf2)
        time.sleep(1)
        print(f'{C}[{G}i{C}] Consultando CPF gerado...')
    elif choice=='3' or choice == '03':
        pass
    else:
        print(f'{C}[{R}ERROR{C}] Opção inválida.')
        time.sleep(3)
    if cpf != '0':
        try:### Agradecemos ao p0is0n por essa parte :)
            h={
        'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
        'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID;                       FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
'Host': "www.juventudeweb.mte.gov.br"
            }
            r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text
            print(f'''
{C}CPF: {B}{re.search('NRCPF="(.*?)"', r).group(1)}
{C}Nome: {B}{re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}
{C}Nascimento: {B}{re.search('DTNASCIMENTO="(.*?)"', r).group(1)}
{C}Nome da Mae: {B}{re.search('NOMAE="(.*?)"', r).group(1).title()}
{C}Endereco: {B}{re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}
{C}Complemento: {B}{re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}
{C}Bairro: {B}{re.search('NOBAIRRO="(.*?)"', r).group(1).title()}
{C}Cidade: {B}{re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}
{C}CEP: {B}{re.search('NRCEP="(.*?)"', r).group(1)}
            ''')
            print(f'{C}[{Y}i{C}] Deseja realizar uma nova consulta?')
            print('1.Sim')
            print('2.Não')
            nova=input(f'===>').lower()
            if nova=='1' or nova=='01':
                consultacpf()
            elif nova=='2' or nova=='02':
                pass
            else:
                print(f'{C}[{R}i{C}]Opção inválida')
                pass
        except(AttributeError):
            print(f'{R}CPF não existe{C}')
            print(f'{R}Tente novamente e pressione enter para retornar{C}')
            lo = input("===>")

def consultaoperadora():
    os.system("figlet KINY")
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

def cc_checker(token):
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

    data = requests.get('https://lookup.binlist.net/{}'.format(cc[0:6])).json()
    pessoa = requests.get('https://randomuser.me/api/?nat={}'.format(data['country']['alpha2'])).json()
    cpf = requests.get('http://geradorapp.com/api/v1/cpf/generate?token={}'.format(token[0])).json()

    email_provider = ["@gmail.com","@outlook.com","@yahoo.com","@terra.com"]

    email = (pessoa['results'][0]['first']) + "." + (pessoa['results'][0]['last']) + random.choice(email_provide)

    print()
    print(f'{C}[{G}i{C}] Consultando cartão')
    print('Cartao: {}'.format(gg))
    print('Bandeira: {}'.format(data['scheme']))
    print('Tipo: {}'.format(data['type']))
    print('Pais: {}'.format(data['country']))
    print('Banco: {}'.format(data['bank']))
    print('Nivel: {}'.format(data['brand']))
    print()
    print(f'{C}[{G}i{C}] Gerando pessoa aleatoria')
    print('Nome: {} {}'.format(pessoa['results'][0]['first'],pessoa['results'][0]['last']))
    print('Genero: {}'.format(pessoa['results'][0]['gender']))
    print('Nascimento: {}'.format(pessoa['results'][0]['dob']['date'][0:10]))
    print('CPF: {}'.format(cpf['number_formatted']))
    print('CPF sem formatação: {}'.format(cpf['number']))
    print('E-mail: {}'.format(email))
    print('CEP: {}{}'.format(pessoa['results'][0]['location']['postcode'],'-000'))
    print('Endereço: {}'.format(pessoa['results'][0]['location']['street']['name']))
    print('Cidade: {}'.format(pessoa['results'][0]['location']['city']))
    print('Estado: {}'.format(pessoa['results'][0]['location']['state']))
    print()

    header = {
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

    if pessoa['results'][0]['gender'] == 'female':
        gender = 'F'
    if pessoa['results'][0]['gender'] == 'male':
        gender = 'M'
    if data['type'] == 'credit':
        tipo = 'C'
    if data['type'] == 'debit':
        tipo = 'D'
    nome = pessoa['results'][0]['first'] + pessoa['results'][0]['last']

    donate='successUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Fagradecimento.html%3Fd%3DBRPT00GD00%2520General%26r%3Dtrue%26a%3D%24%7BconvertedAmount%7D%26t%3D%24%7Btransaction.referenceID%7D%26u%3D%24%7Btransaction.nativeResponse%7D%26m%3DcreditCard%26v%3Ddonate&errorUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Ferror.html&pfpsrc=&DESCRIPTION=Com+Os+Refugiados&ONLINE_FORM=BRPT00GD00+General&LANGUAGE=pt&CURRENCY='+pais.get('currency')+'&EXPDATE='+mes+ano[1:3]+'&TAXID='+cpf['number']+'&AMT=35&TYPE='+tipo2+'%2F'+band+'&PAYPERIOD=MONT&X=&FIRSTNAME='+pessoa['results'][0]['name']['first']+'&LASTNAME='+pessoa['results'][0]['name']['last']+'&EMAIL='+email.replace('@','%40')+'&GENDER='+gender+'&CUSTOM_KEY_1=birthdate&CUSTOM_KEY_2=device&CUSTOM_VALUE_1='+pessoa['results'][0]['dob']['date'][0:10].replace('/','%2F')+'&CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_KEY_1=birthdate&GIFT_CUSTOM_KEY_2=device&GIFT_CUSTOM_KEY_3=entrypoint&GIFT_CUSTOM_VALUE_1='+pessoa['results'][0]['dob']['date'][0:10].replace('/','%2F')+'&GIFT_CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_VALUE_3=%2Facnur%2Fdonate.html&STREET='+pessoa['results'][0]['location']['street']['name'].replace(' ','+')+'&STREET2='+Centro+'&CITY='+pessoa['results'][0]['location']['city'].replace(' ','+')+'&STATE='+pessoa(['results'][0]['location']['state'])+'&ZIP='+str(pessoa['results'][0]['location']['postcode'])+'-000'+'&COUNTRY='+data['country']+'&PHONENUM=%2811%29+98765-4321&CCTYPE='+tipo+'%2F'+data['scheme']+'&ACCT='+cc+'&NAME='+nome.replace(' ','+')+'&CVV2='+cvv
    RS=requests.request('POST',donate,headers=h,data=data).url
    if RS=='https://doar.acnur.org/acnur/agradecimento.html':
        print(f'{C}[{G}i{C}] Pagamento autorizado!')
    else:
        RS=RS.split('=')[3]
        if RS=='REFUSED_PAYMENT':
            print(f'{C}[{R}ERROR{C}] Transação recusada.')
        elif RS=='DATA_INVALID':
            print(f'{C}[{R}ERROR{C}] Cartão invalido.')
        elif RS=='FAIL_UNKNOWN':
            print(f'{C}[{R}ERROR{C}] Erro Desconhecido ({R}possivel uso de cartao de Debito{C}).')
        elif RS=='ERROR_NETWORK':
            print(f'{C}[{R}ERROR{C}] Erro de rede.')
        elif RS=='DATA_CARD_NOT_ALLOWED':
            print(f'{C}[{R}ERROR{C}] Pagamento nao autorizado.')
        elif RS=='REFUSED_PROVIDER':
            print(f'{C}[{R}ERROR{C}] Pagamento recusado pela {Y}{band}{C}.')
        elif RS=='REFUSED_BANK':
            print('[{}ERROR{}] Recusado pelo {}{}{}.'.format(R,C,Y,banco.get('name'),C))
        elif RS=='DATA_MISSING':
            print(f'{C}[{R}ERROR{C}] Algum dado faltando.')
        else:
            print(f'{C}[{R}ERROR{C}] Erro não listado.')
