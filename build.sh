set -o errexit
pip install -r requirements.txt
python3 manage.py collectstatic
python manage.py migrate sessions
python3 manage.py superuser