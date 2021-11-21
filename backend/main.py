from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():    
    return {"message": "Hello World"}


@app.get("/fékk_flest_reactions")
def root():    
    f = open("data/parsed/boycott/all/Fékk flest reactions.csv", "r", encoding="utf-8")
    data = []
    for line in f.readlines()[1:]:
        d = line.strip().split(",")
        data.append({"name": d[1], "count": int(d[0])})
    return {"data": data}