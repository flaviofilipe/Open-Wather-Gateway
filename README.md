#  Open Weather Gateway

This application collects data from [Open Weather Gateway](https://openweathermap.org/) searching by city and register in historic.

##  Backend
The backend was makes with Flask and use sqlite database.

**Requirements**
- Python > 3.7
- [Python venv](https://docs.python.org/pt-br/3/library/venv.html) 

**Install**
### Create virtualenv
```
python3 -m venv venv
```

### Run virtualenv
Linux
```
source venv/bin/activate
```
Windows
```
venv\Scripts\activate
```

### Install the requirements
```
pip install -r requirements.txt
```

###  Create .env
- Copy .env-example and rename to .env
- Set in `API_KEY` the Open Weather key [?](https://openweathermap.org/appid)

### Create database and run migrations
```
flask db update
```

###  Run
```
flask run
```

###  Run tests
```
pytest
```

## Frontend
The Frontend was makes with ReactJS

**Requirements**
- NodeJS
- Yarn

###  Install requirements
Access the path `frontend` and run
```
yarn install
```

###  Run
```
yarn start
```

## Routes
|Method| Route  | Description  | Params |
|--|--|--|--|
| GET | /weather | List the historic | [int] max |
| GET | /weather/\<city-name> | Find the temperature city | [str] city-name |

