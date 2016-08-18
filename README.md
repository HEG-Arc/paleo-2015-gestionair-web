for docker dev version

create .env file

```
DBEUG
POSTGRES_USER=gestionairweb
POSTGRES_PASSWORD=password
DATABASE_URL=postgres://gestionairweb:password@db/gestionairweb
STATIC_ROOT
``` 

```
 docker-compose up -d
 docker-compose run web python manage.py migrate
 docker-compose run web python manage.py createsuperuser
```