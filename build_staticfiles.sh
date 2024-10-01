cat /etc/os-release
python3 -m pip install pip==23.0.1

python3 -m pip install "urllib3<2"
python3 -m pip install -r requirements.txt

# Build staticfiles
python3 manage.py collectstatic --no-input
