python3 --version
pip --version 

cat /etc/os-release
python3 -m pip install pip==23.0.1

pip install "urllib3<2"
pip install -r requirements.txt

python3 manage.py collectstatic --no-input
