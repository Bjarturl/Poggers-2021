from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os, csv

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ENDPOINTS

@app.get("/")
def root():    
    return {"message": "POGGERS"}


# Returns all available files and years for data_by_year_and_file
@app.get("/data")
def data():    
    return {
        "years": os.listdir(f"{os.getcwd()}\data"),
        "names": [name.split('.')[0] for name in os.listdir(f"{os.getcwd()}\data\\all")]
    }


# Returns parsed data for specified year and file
@app.get("/data/{year}/{file}")
async def data_by_year_and_file(year, file):    
    data = []
    try:
        f = open(f"data/{year}/{file}.csv", "r", encoding="utf-8")
    except FileNotFoundError:
        return {"data": [], "message": "File not found"}
    csv_reader = csv.reader(f, delimiter=",")    
    line_count = 0
    labels = []
    for line in csv_reader:
        if line_count == 0:
            labels = line
        else:
            data_obj = {}
            for i in range(0, len(line)):
                # Convert to number if possible
                try:
                    data_obj[labels[i]] = float(line[i])
                except ValueError:
                    data_obj[labels[i]] = str(line[i])
            data.append(data_obj)
        line_count += 1
    return {"data": data}