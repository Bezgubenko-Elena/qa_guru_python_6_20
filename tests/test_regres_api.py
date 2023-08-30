import requests
from jsonschema.validators import validate
import json
import os

path_schema = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources'))
base_url = "https://reqres.in"


def test_get_single_user():
    response = requests.get(
        url=f"{base_url}/api/users/2"
    )

    assert response.status_code == 200
    assert response.json()["data"]["first_name"] == "Janet"
    assert response.json()["data"]["last_name"] == "Weaver"
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
    assert len(response.json()) == 2
    assert len(response.json()["data"]) == 5
    assert len(response.json()["support"]) == 2


def test_single_user_schema():
    with open(os.path.join(path_schema, "schema_single_user.json")) as file:
        schema = json.loads(file.read())
        response = requests.get(url=f"{base_url}/api/users/2")

        validate(instance=response.json(), schema=schema)


def test_get_single_user_not_found():
    response = requests.get(
        url=f"{base_url}/api/users/23"
    )

    assert response.status_code == 404
    assert not len(response.json())


def test_create_user():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(
        url=f"{base_url}/api/users",
        data=payload
    )

    assert response.status_code == 201
    assert response.json()["name"] == payload.get("name")
    assert response.json()["job"] == payload.get("job")


def test_update_user_put():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.put(
        url=f"{base_url}/api/users/2",
        data=payload
    )
    assert response.status_code == 200
    assert response.json()["job"] == payload.get("job")


def test_delete_user():
    response = requests.delete(
        url=f"{base_url}/api/users/2"
    )
    assert response.status_code == 204


def test_register_successful():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(
        url=f"{base_url}/api/register",
        data=payload
    )

    assert response.status_code == 200
    assert type(response.json()["token"] == "str")


def test_register_unsuccessful():
    payload = {
        "email": "sydney@fife"
    }

    response = requests.post(
        url=f"{base_url}/api/register",
        data=payload
    )

    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"


def test_login_successful():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(
        url=f"{base_url}/api/login",
        data=payload
    )

    assert response.status_code == 200
    assert "token" in response.json()


def test_login_unsuccessful():
    payload = {
        "email": "peter@klaven"
    }

    response = requests.post(
        url=f"{base_url}/api/login",
        data=payload
    )

    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
