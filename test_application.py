import requests

# Define endpoints
short_endpoint = "https://ionaapp.com/assignment-magic/dk/short"
long_endpoint = "https://ionaapp.com/assignment-magic/dk/long"

# Define arg values
short_args = ["ab", "12", "a2"]
long_args = ["ab2", "123", "a36"]

def test_short_endpoint():
    """ 
    Tests the `/short/` endpoint with various arg values
    """
    for arg in short_args:
        response = requests.get(f"{short_endpoint}/{arg}")
        assert response.status_code == 200
        data = response.json()
        assert data["uid"] is not None
        assert len(data["uid"]) == 32

def test_long_endpoint():
    """
    Tests the `/long/` endpoint with various arg values
    """
    for arg in long_args:
        response = requests.get(f"{long_endpoint}/{arg}")
        assert response.status_code == 200
        data = response.json()
        assert data["uid"] is not None
        assert len(data["uid"]) == 32

# Run tests
test_short_endpoint()
test_long_endpoint()