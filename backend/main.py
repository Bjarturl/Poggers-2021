from fastapi import FastAPI

app = FastAPI()


@app.get("/heildarfjoldi-skilaboda")
async def root():
    f = open("data/parsed/boycott/2020/Heildarfjöldi skilaboða.csv")
    
    return {"message": "Hello World"}