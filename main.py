from fastapi import FastAPI, Query
import requests
import random

app = FastAPI()


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

