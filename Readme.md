mkdir -p django_unicorn_bulma && cd $_

python3 -mvenv env

echo "source env/bin/activate" > load_env.sh

. load_env.sh

pip install django django-unicorn django-bulma

pip freeze -l > requirements.txt

django-admin startproject django_prj

mv django_prj src

echo "cd src" >> load_env.sh

