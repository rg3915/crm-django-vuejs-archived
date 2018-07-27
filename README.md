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
cd crm-django-vuejs
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/.env-sample .env
python manage.py migrate
python manage.py runserver
```