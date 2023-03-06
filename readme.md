# Example for API consumption and save response data to local postgres DB (Windows).

## You gonna need

python 3.10, Docker Desktop

## Instructions

1. Clone this repo to your local machine:
```
git clone https://github.com/belan581/api-consume-save-postgres.git
```
2. Create a virtualenv (python 3)
```
python -m venv venv
```
3. Activate the new virtualenv
```
venv\Scripts\activate.bat
```
4. Install the packages
```
pip install -r requirements.txt
```
5. Create an .env file with your secrets
```
NEWSAPI_API_KEY=apikeystring
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postrgres_password
POSTGRES_DB=newsapi
POSTGREST_HOST=localhost
POSTGREST_PORT=5432
```
6. Create the container of postgres
```
docker compose up --build
```
7. Run main.py
```
python main.py
```
8. You can access to postgres via adminer. Open your browser and copy this url
```
http://127.0.0.1:8080
Database engine: PostgreSQL
Server: db
user: postgres
password: 12345678
```