import requests
import pytest

# Test case 1: Retrieve a Random Cat Fact
def test_random_cat_fact():
    # Send a GET request to the cat-facts API endpoint
    response = requests.get("https://cat-fact.herokuapp.com/facts/random")

    # Validate response status code
    print(response.status_code)
    assert response.status_code == 200

    # Parse the response JSON to extract the cat fact
    cat_fact = response.json()["text"]

    # Validate that the response contains a cat fact
    assert cat_fact is not None
    assert isinstance(cat_fact, str)

# Test case 2: Retrieve Multiple Cat Facts
def test_multiple_cat_facts():
    # Send a GET request to the cat-facts API endpoint to retrieve multiple cat facts
    response = requests.get("https://cat-fact.herokuapp.com/facts/random?amount=5")

    # Validate response status code
    assert response.status_code == 200

    # Parse the response JSON to extract the cat facts
    cat_facts = [fact["text"] for fact in response.json()]

    # Validate that the response contains an array of cat facts with the specified count
    assert len(cat_facts) == 5

    # Validate that each cat fact in the array is unique
    assert len(set(cat_facts)) == 5

# Run the test with pytest
if __name__ == "__main__":
    pytest.main()
