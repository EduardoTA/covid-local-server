# covid-local-server

O projeto consiste em uma aplicação web, desenvolvida utilizando do framework Django, feita para criar um servidor que armazenasse os dados de aplicação de vacinações do sistema VaciVida para enviar para o banco de dados central de maneira assíncrona, a fim de evitar que o usuário do sistema VaciVida precisasse esperar muito tempo durante o uso do sistema caso estivesse em um local com conexão ruim com a internet. Para simular o servidor remoto do VaciVida, foi utilizado um servidor hospedado na plataforma Heroku: https://serverremoto.herokuapp.com/api, sincronizada com o repositório GIT: https://github.com/lsantos0142/serverremoto

Para rodar o projeto em sua máquina, é necessário, primeiramente ter instalado o GIT, um interpretador de **python 3.9**, o framework **Django** e a ferramenta **pipenv**, de criação de ambientes virtuais em python. 
Tendo essas ferramentas instaladas, clone o repositório GIT (branch main) e siga os seguitnes passos: 

* Utilize do comando **"pipenv install"**, ou caso não funcione, use **"pipenv install -r -requirements.txt"** para instalar as dependências. 
* Rode o arquivo **ATUALIZAR_E_RODAR.bat** para gerar o schema do banco de dados local e rodar o aplicativo. Isso deverá criar um servidor local com a aplicação. 
* No seu navegador então, vá para o endereço **"localhost:8000"**. Lá deve estar hospedada a aplicação. 

Para logar como um administrador, rode o **DJANGO_CREATESUPERUSER.bat**, e escolha um usuário e senha. Para os testes da sincronização com o Heroku funcionarem corretamente, o nome de usuário deve ser **"admin"**. Não há necessidade de informar um email se você não desejar. Para fazer um teste como usuário não administrador, vá para a aba de "Criar Usuário" da aplicação, e para que a sincronização com o Heroku ocorra corretamente, esse usuário deve ser **"teste_usuario_padrao"**. 

Para acessar o servidor local de uma outra máquina na mesma rede local, use o comando "ipcofig" para descobrir o endereço IP local do computador que está sendo usado como servidor, então, através de seu navegador, digite o endereço IP desta máquina na barra de pesquisa. 

Para realizar a sincronização com o servidor remoto, basta clicar no botão "Sincronizar", e então, os dados deveriam ir para o servidor hospedado no Heroku.

Abaixo está uma maneira de realizar testes para verificar o funcionamento correto do sistema:

* Primeiro, cadastre um paciente. Um exemplo de valores aceitos no cadastro está abaixo:  
CPF: 20699307937 ,  
CNS: ,  
nome: Emily Lara Brenda Fogaça ,  
Nome da Mae: Maitê Jéssica Letícia ,  
Nome Social: ,  
Data de Nascimento: 1951-08-18 ,  
Telefone: 1147483647 ,  
email: ,  
Sexo: FEMININO ,  
Raça: Nao informada ,  
gestante: ,  
puerpera: ,  
pais: Brasil ,  
UF: BA ,  
Municipio: Salvador ,  
Logradouro: Rua João Moraes ,  
Numero: 250 ,  
Bairro: Fazenda Grande do Retiro ,  
Complemento: ,  
Zona: URBANA 

* Entre então, no menu de administrador, clique para adicionar um lote, e adicione com as informações:  
Lote: tgreye5ry ,  
Imunobiológico: ASTRAZENCA/OXFORD/FIOCRUZ ,  
Data de Validade: 2021-07-27  

* Escolha a opção de registrar uma imunização, e registre com as informações abaixo:  
Paciente: CPF: 20699307937, Nome: Emily Lara Brenda Fogaça  
CNS: ,  
Comorbidades: ,   
CRM_medico_resp: ,  
Numero do BPC: ,  
Dose: 1º DOSE ,  
Imunobiologico: ASTRAZENECA/OXFORD/FIOCRUZ ,  
lote: tgreye5ry ,  
Via de Administração: Endovenosa ,  
Local de Administração: Deltoide Esquerdo ,  
Vacinador: admin ,  
Grupo: Idoso ,  
Estrategia: Campanha Indiscriminada ,  
Dara de Aplicação: 2021-11-11,  
Data de Aprazamento: 2022-02-03,  
Estado 1ªdose: ,  
Pais 1ªdose:   
        
* Aperte então no botão "Sincronizar", e deverá ser possível observar o novo cadastro em: https://serverremoto.herokuapp.com/api
