for docker dev version

create .env file

```
POSTGRES_USER=gestionairweb
POSTGRES_PASSWORD=password
DATABASE_URL=postgres://gestionairweb:password@db/gestionairweb
``` 

```
 docker-compose up -d
 docker-compose run web python manage.py migrate
 docker-compose run web python manage.py createsuperuser
```