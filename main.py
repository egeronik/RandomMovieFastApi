from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import random
import uvicorn
import os

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    r_id = random.randint(298, 10000)
    r = requests.get(f"https://kinopoiskapiunofficial.tech/api/v2.2/films/{r_id}", headers={'X-API-KEY': '700211e1-f970-499f-9957-6bca24e2adb1'})
    return r.json()


@app.get("/list/")
async def get_list(q: list | None = Query()):
    film_list = []
    for id in q:
        r = requests.get(f"https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}",
                         headers={'X-API-KEY': '700211e1-f970-499f-9957-6bca24e2adb1'})
        film_list.append(r.json())
    return film_list

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))

