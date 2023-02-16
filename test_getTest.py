import requests
import json

def test_users():
    response  = requests.get("https://reqres.in/api/users?page=2")
    print(response.content)
    jsonData = json.loads(response.content.decode('utf-8'))
    assert response.status_code ==200
    assert jsonData['total'] ==12

def test_createUsers():
    body ="""{
    "name": "morpheus",
    "job": "leader"
    }"""
    url ="https://reqres.in/api/users"
    response = requests.post(url=url, json ={"body": body})
    print(response.content)
    assert response.status_code ==201
    jsonData= json.loads(response.content.decode('utf-8'))
    assert isinstance(jsonData['id'], str) ==True

def test_deleteUsers():
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code==204