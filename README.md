# covid-local-server

O projeto consiste em uma aplicação web, desenvolvida utilizando do framework Django, feita para criar um servidor que armazenasse os dados de aplicação de vacinações do sistema vacivida para enviar para o banco de dados central de maneira assíncrona, a fim de evitar que o usuário do sistema vacivida precisasse esperar muito tempo durante o uso do sistema caso estivesse em um local com conexão ruim com a internet.

Para rodar o projeto em sua máquina, é necessário, primeiramente ter instalado o framework Django e a ferramenta pipenv, de criação de ambientes virtuais em python. 
Após clonar o repositório Git, siga as instruções a seguir:

* Utilize do comando "pipenv install" para instalar as dependências 
* Rode o arquivo ATUALIZAR_E_RODAR.bat para gerar o schema do banco de dados local e rodar o aplicativo. Isso deverá criar um servidor local com a aplicação.
* No seu navegador então, vá para o endereço "localhost:8000". Lá deve estar hospedada a aplicação. 
