import requests
import pytest


def test_poetrydb_get_random_poem():
  """
  Tests retrieving a random poem from the PoetryDB API using requests.
  """

  # Set base URL for PoetryDB API
  base_url = "https://poetrydb.org/api"

  # Send GET request to /random endpoint
  response = requests.get(f"{base_url}/random")

  # Assert status code is 200 (OK)
  assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

  # Parse JSON response (assuming successful response)
  data = response.json()

  # Validate at least one poem is present
  assert len(data) >= 1, "No poems found in the response"


def test_poetrydb_search_by_author(author_name="Edgar Allan Poe"):
  """
  Tests searching for poems by a specific author in the PoetryDB API using requests.
  """

  # Set base URL for PoetryDB API
  base_url = "https://poetrydb.org/api"

  # Define search term (author name)
  search_term = author_name

  # Build URL with author parameter
  url = f"{base_url}/author?author={search_term}"

  # Send GET request to constructed URL
  response = requests.get(url)

  # Assert status code (200 for found, 404 for not found)
  expected_status_code = 200 if search_term else 404
  assert response.status_code == expected_status_code, f"Unexpected status code: {response.status_code}"

  # Parse JSON response (assuming successful response)
  data = response.json()

  # Validate poems or empty list (depending on search result)
  if expected_status_code == 200:
    assert len(data) >= 1, "No poems found for the author"
  else:
    assert len(data) == 0, "Unexpected poems found for non-existent author"

# Run the test with pytest
if __name__ == "__main__":
    pytest.main()
