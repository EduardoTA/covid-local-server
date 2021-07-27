git pull
pipenv run python projeto/manage.py makemigrations
pipenv run python projeto/manage.py migrate
pipenv run python projeto/atualiza_data.py
pipenv run python projeto/manage.py loaddata imunobiologicos.json
start RUN_DJANGO.bat
start run_workers.bat