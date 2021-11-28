# POGGERS 2021
The backend serves content from csv files as I'm not interested in exposing a local database which contains my entire chat history.
Instead I generate these csv files so the frontend only knows about minimal necessary data to create graphs and such.
The command for generating the files assumes a connection to a local database following a certain schema. 
All data is fetched from Facebook and inserted into a MySQL database through a different Django app not present in this project (easier to do through Django ORM).

## Project setup
```
pip install virtualenv
source venv/Scripts/activate
pip install -r requirements.txt
```
Run source venv/Scripts/activate in the project root every time you open up a new terminal

## Generate csv files
The csv files should already be generated, otherwise run this command.
```
./generate_csv.sh
```

## Serve
```
./serve.sh
```

## Example usage
The main endpoint for this API is /data/{year}/{file}.
The /data endpoint will give you all possible combinations that can be passed to the {year} and {file} variables.
E.g. calling the main endpoint with:
year = 2017 
file = heildarfjöldi_mynda
or /data/2017/heildarfjöldi_mynda
would give you the data for heildarfjöldi_mynda in the year 2017.
If you want to query for all years, simply put "all" in the year parameter.

## Pushing to Heroku
- git subtree push --prefix backend heroku main
Then the api will be available at https://poggers2021api.herokuapp.com/