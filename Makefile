run:
    docker-compose up --build

makemigrations:
    docker-compose exec web python manage.py makemigrations

migrate:
    docker-compose exec web python manage.py migrate

createsuperuser: 
    docker-compose exec web python manage.py createsuperuser

stop:
    docker-compose down