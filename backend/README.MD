# POGGERS 2021
The backend serves content from csv files as I'm not interested in exposing a local database which contains my entire chat history.
Instead I generate these csv files so the frontend only knows about minimal necessary data to create graphs and such.
The command for generating the files assumes a connection to a local database following a certain schema. 
All data is fetched from Facebook and inserted into a MySQL database through a different Django app not present in this project (easier to do through Django ORM).

## Basic setup
- pip install virtualenv
- source venv/Scripts/activate
- pip install -r requirements.txt

## Generate csv files
The csv files should already be generated, otherwise run this command.
- ./generate_csv.sh

## Serve
- ./serve.sh