git pull
pipenv run python projeto/manage.py makemigrations
pipenv run python projeto/manage.py migrate
pipenv run python projeto/atualiza_data.py
start RUN_DJANGO.bat
start run_workers.bat