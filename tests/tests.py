import requests
import jsonschema
from jsonschema.validators import validate

def test_create_user():
    payload = {"name": "morpheus",
    "job": "leader",
    "id": "382",
    "createdAt": "2023-08-24T19:32:15.272Z"
               }

    response = requests.post(
        url="https://reqres.in/api/users",
        data=payload
    )

    assert response.status_code == 201




def test_register_successful():
    pass
'''
    payload = {"name": "morpheus",
    "job": "leader",
    "id": "382",
    "createdAt": "2023-08-24T19:32:15.272Z"
               }

    response = requests.post(
        url="https://reqres.in/api/users",
        data=payload
    )

    assert response.status_code == 201
'''

def test_register_unsuccessful():
    pass
'''
    payload = {"name": "morpheus",
    "job": "leader",
    "id": "382",
    "createdAt": "2023-08-24T19:32:15.272Z"
               }

    response = requests.post(
        url="https://reqres.in/api/users",
        data=payload
    )

    assert response.status_code == 201
'''

def test_create_user_unsuccessful():
    pass
'''
    payload = {"name": "morpheus",
    "job": "leader",
    "id": "382",
    "createdAt": "2023-08-24T19:32:15.272Z"
               }

    response = requests.post(
        url="https://reqres.in/api/users",
        data=payload
    )

    assert response.status_code == 201
'''

def test_update_user():
    pass
'''
    payload = {"name": "morpheus",
    "job": "leader",
    "id": "382",
    "createdAt": "2023-08-24T19:32:15.272Z"
               }

    response = requests.post(
        url="https://reqres.in/api/users",
        data=payload
    )
    assert response.status_code == 201

'''

def test_delete_user():
    pass
'''
    payload = {"name": "morpheus",
    "job": "leader",
    "id": "382",
    "createdAt": "2023-08-24T19:32:15.272Z"
               }

    response = requests.post(
        url="https://reqres.in/api/users",
        data=payload
    )
    assert response.status_code == 201

'''

def test_delete_user_unsuccessful():
    pass
'''
    payload = {"name": "morpheus",
    "job": "leader",
    "id": "382",
    "createdAt": "2023-08-24T19:32:15.272Z"
               }

    response = requests.post(
        url="https://reqres.in/api/users",
        data=payload
    )
    assert response.status_code == 201

'''

+ 3 tests for schema (get, post, put?)