## FastAPI 

The following repository deals with an API using FastAPI and a PostgreSQL database.

It is deployed using docker-compose.

To run the container, you have to execute the following command:

```bash 
docker-compose up
```

There are three different endpoints to be used.
The important thing is to perform the /login endpoint first in order to be able to perform the other two requests.

```bash
http://localhost:8000/api/v1/login
```

This endpoint receives the following data in its body:

```bash 
{
    "username": "adminuser",
    "password": "adminpassword",
    "host" : "db",
    "db_name": "postgresdatabase"
}
```

These credentials will allow the user to access the database and perform the other queries.

To extract the schema of the tables:
```bash
http://localhost:8000/api/v1/retrieve-schema
```


To extract the schema of a table:
```bash
http://localhost:8000/api/v1/tables/{table}
```
By default, the application deploy creates 2 tables, users and cars.

To run the test, execute:
```bash
cd app
pytest test.py
```