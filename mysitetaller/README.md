# Instalación

git clone repo
cd library

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# migraciones
python manage.py migrate

# crear admin
python manage.py createsuperuser

# correr servidor
python manage.py runserver

# ejecutar pruebas
python manage.py test