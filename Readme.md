```sh
mkdir -p django_unicorn_bulma && cd $_

python3 -mvenv env

echo "source env/bin/activate" > load_env.sh

. load_env.sh

pip install django django-unicorn django-bulma

pip freeze -l > requirements.txt

django-admin startproject django_prj

mv django_prj src

echo "cd src" >> load_env.sh
```

### Use bulma

Add `STATICFILES_DIRS` to `settings.py`

```python
STATICFILES_DIRS = (
    BASE_DIR / 'bulma_static',
)
```

Then issue command

```sh
python manage.py copy_bulma_static_into_project
python manage.py bulma install
```
