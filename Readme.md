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

##### Use bulma sass from django-bulma

Add `STATICFILES_DIRS` to `settings.py`

```python
STATICFILES_DIRS = (
    BASE_DIR / 'bulma_static',
)
```

Then issue command

```sh
python manage.py copy_bulma_static_into_project
cd bulma_static/bulma/sass && yarn && yarn start
```

##### Or create a bulma_theme app to save the bulma sass files

```sh
python manage.py startapp bulma_theme
mkdir -p bulma_theme/static
cp -r bulma_static/bulma/sass bulma_theme/nodejs_static
rm -r bulma_static
cd bulma_theme/nodejs_static
yarn add font-awesome
yarn add --dev postcss googlefonts-inliner
yarn upgrade node-sass@^6 postcss-cli@^9 clean-css-cli@^5
cp -r node_modules/font-awesome/fonts ../static/
yarn build
yarn start
```
