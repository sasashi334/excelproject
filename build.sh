set -o errexit
pip install -r requirements.txt
python3 manage.py collectstatic --no-input
python3 manage.py migrate --fake
python3 manage.py superuser