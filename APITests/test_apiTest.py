import requests


def test_get_locations_for_us():
    response = requests.get("http://api.zippopotam.us/us/90210")
    print(response.json())
    assert response.status_code ==200