tar -xf Apache.zip
tar -xf zf_1c_connect_client.zip

pip install virtualenv
python -m virtualenv env

cmd /U /k "env\Scripts\activate&&pip install -r requirements.txt&&exit"
