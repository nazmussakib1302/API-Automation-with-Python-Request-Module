import requests
import random
import string
import json


#Base_URL:
base_url = "https://gorest.co.in"

#Auth_Token: 
auth_token = "Bearer gorest_9ffdk7M5reBWQj7hRu0SgZ54OO2mBNjeaEkWbg9qEZ839VX7y"

#GET REQUEST:
def get_request():
    url = base_url + "/public/v2/users"
    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    json_data = response.json()
    print(json.dumps(json_data, indent=4))
    
def post_request():
    url = base_url + "/public/v2/users"
    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json"
    }
    data = {      
        "name": "Nazmus Sakib QA",
        "email": "nazmusstryotel@gmail.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201
    json_data = response.json()
    print(json.dumps(json_data, indent=4))
    user_id = json_data['id']
    assert "name" in json_data and json_data["name"] == "Nazmus Sakib QA"
    return user_id
    
#Call
get_request()

#Call
post_request()