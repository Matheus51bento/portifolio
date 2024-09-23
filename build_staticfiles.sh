sudo apt-get install sqlite3 libsqlite3-dev

python3 -m pip install -r requirements.txt
python3 manage.py collectstatic
python3 manage.py collectstatic --no-input
