# covid-local-server

O projeto consiste em uma aplicação web, desenvolvida utilizando do framework Django, feita para criar um servidor que armazenasse os dados de aplicação de vacinações do sistema vacivida para enviar para o banco de dados central de maneira assíncrona, a fim de evitar que o usuário do sistema vacivida precisasse esperar muito tempo durante o uso do sistema caso estivesse em um local com conexão ruim com a internet. Para simular o servidor remoto do vacivida, foi utilizado um servidor hospedado na plataforma Heroku: https://serverremoto.herokuapp.com/api, sincronizada com o repositório GIT: https://github.com/lsantos0142/serverremoto

Para rodar o projeto em sua máquina, é necessário, primeiramente ter instalado o GIT, um interpretador de python, o framework Django e a ferramenta pipenv, de criação de ambientes virtuais em python. 
Tendo essas ferrametnas instaladas, clone o repositório GIT e siga os seguitnes passos: 

* Utilize do comando "pipenv install", ou caso não funcione, use "pipenv install -r -requirements.txt" para instalar as dependências. 
* Rode o arquivo ATUALIZAR_E_RODAR.bat para gerar o schema do banco de dados local e rodar o aplicativo. Isso deverá criar um servidor local com a aplicação. 
* No seu navegador então, vá para o endereço "localhost:8000". Lá deve estar hospedada a aplicação. 

Para logar como um administrador, rode o DJANGO_CREATESUPERUSER.bat, e escolha um usuário e senha. Para os testes da sincronização com o Heroku funcionarem corretamente, o nome de usuário deve ser "admin". Não há necessidade de informar um email se você não desejar. Para fazer um teste como usuário não administrador, vá para a aba de "Criar Usuário" da aplicação, e para que a sincronização com o Heroku ocorra corretamente, esse usuário deve ser "teste_usuario_padrao". 
 
