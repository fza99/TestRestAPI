**1.**TestRestAPI****

**REST API Test Cases**
This repository contains test cases for two popular REST APIs: PoetryDB https://github.com/thundercomb/poetrydb#readme and Cat Facts https://github.com/alexwohlbruck/cat-facts. The test cases are written in Python using the requests library for making API requests and assertions for validating responses.

**Validation Approach:**

HTTP Status Codes: We primarily use HTTP status codes to validate the overall success or failure of API requests.
Response Data Structure: For successful responses (2xx), we validate the expected structure of the response data using assertions on key data fields.
Content Types: We verify the content type of responses to ensure they match the expected format (e.g., JSON).

**2.Test Cases: **

| API | Test Case Name | Clear Steps | Expected Result | Validation Method |
| --- | --- | ---------------------------------------------------------------------------------- |--- |--- |
| PoetryDB|  Get a Random Poem |1. Import requests.  2. Set base URL: https://poetrydb.org/api.  3. Send GET request to /random.  4. Extract status code.  5. Assert status code is 200 (OK).  6. Parse JSON for poem details.  7. Validate at least one poem exists. | - Status code: 200 (OK).  -JSON response contains a random poem with author, title, lines, etc. | - Assert statements to verify status code and presence of at least one poem in the response.|
| Cat Facts|  |
