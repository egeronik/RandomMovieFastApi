import pytest
import requests
from uuid import UUID, uuid4
from datetime import datetime
import json

base_url = 'http://localhost:80/'

def test_root_get():
    res = requests.get(base_url).json()
    pytest.assume('kinopoiskId' in res.keys())
    pytest.assume('posterUrl' in res.keys())
    pytest.assume(type(res['kinopoiskId']) == int)


def test_list_get():
    res = requests.get(base_url+'list/?q=2754')
    print(res)
    res = json.loads(res.text)[0]
    print(res)
    pytest.assume(res['kinopoiskId']==2754)
    pytest.assume(res['nameRu']=='Сто и одна ночь Симона Синема')
    pytest.assume(res['posterUrl']=="https://kinopoiskapiunofficial.tech/images/posters/kp/2754.jpg")
    
test_list_get()
