import json

# Retorna choices baseado no json da pasta json
def get_choices(nome_arquivo_json):
    json_data = ''
    lista = []

    # Temos um try-catch dentro de um try-catch pois o caminho do arquivo é baseado no diretório de execução de 'python'
    # Então para poder executar 'python' no diretório base e na pasta de 'manage.py' um dos trys não irá dar erro
    try:
        with open('projeto/covidlocal/json/{0}.json'.format(str(nome_arquivo_json))) as f:
            json_data = json.load(f)
    except:
        try:
            with open('covidlocal/json/{0}.json'.format(str(nome_arquivo_json))) as f:
                json_data = json.load(f)
        except:
            raise Exception("{0}.json não está na pasta json".format(str(nome_arquivo_json)))
            return
    for i in range(0,len(json_data)):
        lista.append(tuple([json_data[i]["value"], json_data[i]["display"]]))
    return tuple(lista)

# Retorna lista de países baseada no em paises.json, mas sem o Brasil
def get_paises_exceto_brasil():
    json_data = ''
    lista = []
    try:
        with open('projeto/covidlocal/json/paises.json') as f:
            json_data = json.load(f)
    except:
        try:
            with open('covidlocal/json/paises.json') as f:
                json_data = json.load(f)
        except:
            raise Exception("paises.json não está na pasta json")
            return
    for i in range(0,len(json_data)):
        if json_data[i]["display"] != "Brasil":
            lista.append(tuple([json_data[i]["value"], json_data[i]["display"]]))
    return tuple(lista)