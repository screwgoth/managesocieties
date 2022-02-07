# ManageSocieties
A Django application for managing Co-operative Housing Societies in India

## Instructions to run
* Checkout this repo
```
git clone git@github.com:screwgoth/managesocieties.git
cd managesocieties
```

* Create a virtual env when developing

* Install the dependencies
```
pip install -r requirements.txt
```

* Run the DB migrations
```
python manage.py makemigrations
python manage.py migrate
```

* Run the development server on poere 8000
```
python manage.py runserver 0.0.0.0:8000
```

* When deploying to a non-development environment, update the `DATABASES` section in `settings.py` to point to a SQL database.

* Steps to run with Docker
```
docker-compose up --build -d
```

* See if anythings gone wrong in the logs
```
docker-compose logs -f
```

* Usually, when you run it for the first time, you will see a Python error of not being able to connect to the MySQL DB. This is because MySQL takes a little longer to be up and running the first time. Just restart the containers
```
docker-compose restart backend
```

* Make and run migrations
```
docker-compose run --rm backend python manage.py makemigrations
docker-compose run --rm backend python manage.py migrate
```

* Once done, Shutdown
```
docker-compose down
```

That's it !! Your application is up and running on `http://localhost:8000`.
But remember, we don't have any UI pages yet.
So, you can test it by using a REST client like Postman or `curl` or any other REST-client you are used to.

---
## Verification
* Create an Admin user
```
python manage.py createsuperuser
```
* Enter details like Username, Email, password, etc.

* Login to Admin dashboard at http://localhost:8000/admin

* You can also verify the RESTful API by visitng: http://localhost:8000/api/v1/

- GET list of societies
	- GET request
	- URL : http://localhost:8000/api/v1/societies/

- Add a Society
	- POST request
	- URL : https://localhost:8000/api/v1/societies/
	- JSON Body : 
	```
	{
		"society_name": "Awesome Co-operative Housing Society",
		"address_1" : "666 Some Colony, Some Road",
		"address_2" : "Some Suburb",
		"city": "Pune",
		"state": "Maharashtra",
		"zip_code": "4110111",
		"country": "India"
	}
	```
* Similar APIs can be used for `users` and `buildings`