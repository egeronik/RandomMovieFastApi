import pytest
from uuid import uuid4
from time import sleep
from datetime import datetime
from main import root, get_list
import json
import asyncio
from fastapi import Query


def test_root_get():
    res = asyncio.run(root())
    pytest.assume('kinopoiskId' in res.keys())
    pytest.assume('posterUrl' in res.keys())
    pytest.assume(type(res['kinopoiskId']) == int)


def test_list_get():
    res = asyncio.run(get_list(q=[2754]))
    res = res[0]
    pytest.assume(res['kinopoiskId']==2754)
    pytest.assume(res['nameRu']=='Сто и одна ночь Симона Синема')
    pytest.assume(res['posterUrl']=="https://kinopoiskapiunofficial.tech/images/posters/kp/2754.jpg")
    

