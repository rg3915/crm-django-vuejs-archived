# crm-django-vuejs

CRM testing using Django and VueJS example.

Como contribuir?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/crm-django-vuejs.git
cd crm-django-vuejs/frontend
npm i
cd ../backend
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python create_data.py
python manage.py runserver
```

Já temos um superuser cadastrado:

```
user: admin
pass: d
```
