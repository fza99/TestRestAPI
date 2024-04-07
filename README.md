**# TestRestAPI**
**#REST API Test Cases**
This repository contains test cases for two popular REST APIs: PoetryDB https://github.com/thundercomb/poetrydb#readme and Cat Facts https://github.com/alexwohlbruck/cat-facts. The test cases are written in Python using the requests library for making API requests and assertions for validating responses.

**Validation Approach:**

HTTP Status Codes: We primarily use HTTP status codes to validate the overall success or failure of API requests.
Response Data Structure: For successful responses (2xx), we validate the expected structure of the response data using assertions on key data fields.
Content Types: We verify the content type of responses to ensure they match the expected format (e.g., JSON).
