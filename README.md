# covid-local-server

## Descrição geral do projeto

O projeto realizado trata-se de uma aplicação Web, desenvolvida utilizando do framework Django, que implementa um servidor local que armazena o cadastros de imunizações e pacientes utilizados pelo sistema VaciVida, e então realiza a sincronização desses dados com o banco de dados central de maneira assíncrona num momento oportuno (quando a conexão com a Internet está estável, ou então em horários em que o sistema principal está menos ocupado), a fim de diminuir-se a utilização do servidor central do VaciVida (que pode causar atrasos na vacinação durante o dia), aumentando-se a velocidade dos cadastros de imunizações e pacientes, e assim, aumentando-se o ritmo de vacinações neste período de pandemia.
Para a simulação do servidor central do VaciVida, foi utilizada uma API hospedada na plataforma Heroku: https://serverremoto.herokuapp.com/api, sincronizada com o repositório no GitHub: https://github.com/lsantos0142/serverremoto .

## Instruções de Instalação e Execução do Servidor Local

Para rodar o projeto em sua máquina, é necessário, primeiramente ter instalado o GIT, um interpretador de **python 3.9**, o framework **Django** e a ferramenta **pipenv**, de criação de ambientes virtuais em python. 
Tendo essas ferramentas instaladas, clone o repositório GIT (branch main) e siga os seguintes passos: 

* Abra um terminal ou Command Prompt na pasta onde foi clonado o repositório GIT
* Utilize do comando **"pipenv install"**, ou caso não funcione, use **"pipenv install -r -requirements.txt"** para instalar as dependências do projeto. 
* Rode o arquivo **ATUALIZAR_E_RODAR.bat** para gerar o schema do banco de dados local e rodar o aplicativo. A execução deste arquivo irá criar um servidor local com a aplicação. 
* No seu navegador, vá para o endereço **"localhost:8000"**. Lá estará hospedada a aplicação do servidor local. 

Existem dois tipos de usuários na aplicação local, administrador e não administrador, representando vacinadores responsáveis pelo sistema (que também podem utilizar o servidor local para cadastrar pacientes e imunizações) e vacinadores que utilizarão o sistema, respectivamente.
Para criar um administrador, rode o **DJANGO_CREATESUPERUSER.bat**, e escolha um usuário e senha. Para os testes da sincronização com o Heroku funcionarem corretamente, o nome de usuário deve ser **"admin"**. Não há necessidade de informar um email se você não desejar. Para fazer um teste como usuário não administrador, vá para a aba de "Criar Usuário" da aplicação, e para que a sincronização com o Heroku ocorra corretamente, esse usuário deve ser **"teste_usuario_padrao"**.
O usuário administrador irá ter acesso a três principais funções a mais com relação a usuários não administradores, sendo elas as funções de criação de usuários, acesso à pagina do administrador, e efetuar a sincronização do banco de dados local com o banco de dados central do VaciVida.

## Utilização da aplicação Web em dispositivos mobile

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
