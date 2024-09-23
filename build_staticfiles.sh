python3 -m pip install "urllib3<2"
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic
python3 manage.py collectstatic --no-input
