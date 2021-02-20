# Cheetah Innovation
## Recommended Installation
1. [Mysql](https://www.postgresql.org/download/)
2. [Python](https://www.python.org/downloads/release/python-373/)


## Installation
- Install [pipenv](https://pypi.org/project/pipenv/)
- Clone the repo and `cd cheetah_innovation`
- Run `pip install --user --upgrade pipenv` to get the latest pipenv version.
- Run `pipenv --python 3.7.3`
- Run `pipenv install`
- Run `cp .env.example .env`
- Update .env file `DATABASE_URL` with your `database_name`, `database_user`, `database_password`, if you use Mysql. 
    Can alternatively set it to `sqlite:////tmp/my-tmp-sqlite.db`, if you want to use sqlite for local development.
    
## Getting Started
```
pipenv shell
```

```
python manage.py migrate
```

```
python manage.py runserver
```
