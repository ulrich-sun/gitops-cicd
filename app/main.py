from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def read_main():
    return {"msg": "DEBUT  DE LA MC GITOPS DATASCIENTEST du 18/07/2025"}


