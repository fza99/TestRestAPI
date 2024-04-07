**1.**TestRestAPI****

**REST API Test Cases**
This repository contains test cases for two popular REST APIs: PoetryDB https://github.com/thundercomb/poetrydb#readme and Cat Facts https://github.com/alexwohlbruck/cat-facts. The test cases are written in Python using the requests library for making API requests and assertions for validating responses.

**Validation Approach:**

HTTP Status Codes: We primarily use HTTP status codes to validate the overall success or failure of API requests.
Response Data Structure: For successful responses (2xx), we validate the expected structure of the response data using assertions on key data fields.
Content Types: We verify the content type of responses to ensure they match the expected format (e.g., JSON).

**2.Test Cases: **

| API | Test Case Name | Clear Steps | Expected Result | Validation Method |
| --- | --- | --- |--- |--- |
| PoetryDB|  Get a Random Poem |1.  Import the requests library. 2.  Set the base URL for the PoetryDB API: https://poetrydb.org/api.
                                3.  Send a GET request to the /random endpoint.
                                4.  Extract the status code from the response.
                                5.  Assert that the status code is 200 (OK).
                                6.  Parse the JSON response to extract poem details (author, title, lines, etc.).
                                7.  Validate that the response contains at least one poem.
| Cat Facts|  |
