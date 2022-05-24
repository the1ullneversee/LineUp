from src import api
from fastapi import FastAPI
from fastapi.testclient import TestClient
import json
from src.models import user

class TestBase():
    app = TestClient(api.app)

def test_app_create():
    assert TestBase.app

def test_read_home():
    response = TestBase.app.get("/")
    assert response.status_code == 200

def test_read_home_user_check():
    response = TestBase.app.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload != ""
    user = payload[0]
    assert user['id'] != ""

def test_user_retrieval():
    response = TestBase.app.get("/user?user_id=1")
    assert response.status_code == 200
    payload = response.json()
    assert payload != ""
    assert payload['id'] != ""

def test_user_retrieval_not_exist():
    response = TestBase.app.get("/user?user_id=-1")
    assert response.status_code == 404

def test_dual_requests():
    response = TestBase.app.get("/")
    response1 = TestBase.app.get("/")
    assert response.status_code == 200
    assert response1.status_code == 200

def test_multiple_requests():
    requests = 10
    responses = [TestBase.app.get("/") for i in range(0,requests)]
    for response in responses:
        assert response.status_code == 200

def test_different_requests():
    requests = 10
    responses = [TestBase.app.get("/") if i%2==0 else TestBase.app.get(f"/user?user_id={i}") for i in range(0,requests)]
    for response in responses:
        print(response.text)
        assert response.status_code == 200


