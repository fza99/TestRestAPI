#1.Rest API TEST

##REST API Test Cases
This repository contains test cases for two popular REST APIs: PoetryDB https://github.com/thundercomb/poetrydb#readme and Cat Facts https://github.com/alexwohlbruck/cat-facts. The test cases are written in Python using the requests library for making API requests and assertions for validating responses.

##Validation Approach:

HTTP Status Codes: We primarily use HTTP status codes to validate the overall success or failure of API requests.
Response Data Structure: For successful responses (2xx), we validate the expected structure of the response data using assertions on key data fields.
Content Types: We verify the content type of responses to ensure they match the expected format (e.g., JSON).

#2.Test Cases:

| API | Test Case Name | Clear Steps | Expected Result | Validation Method |
| --- | --- | ---------------------------------------------------------------------------------- |--- |--- |
| PoetryDB|  Get a Random Poem |1. Import requests.  2. Set base URL: https://poetrydb.org/api.  3. Send GET request to /random.  4. Extract status code.  5. Assert status code is 200 (OK).  6. Parse JSON for poem details.  7. Validate at least one poem exists. | - Status code: 200 (OK).  -JSON response contains a random poem with author, title, lines, etc. | - Assert statements to verify status code and presence of at least one poem in the response.|
|PoetryDB| Search for Poems by Author | 1. Import the requests library. 2.Set the base URL for the PoetryDB API: https://poetrydb.org/api. 3.Define the search term (author name). 4.Build the URL with the search parameter: /author?author=<author_name>. 5.Send a GET request to the constructed URL. 6.Extract the status code from the response. 7. Assert that the status code is 200 (OK) or 404 (Not Found) depending on the existence of poems by the author. 8.Parse the JSON response to validate the number of poems or an empty list if none are found. | Status code: 200 (OK) if the author exists and poems are found, or 404 (Not Found) if the author doesn't exist. JSON response containing an array of poems by the specified author or an empty array if no poems are found.| Assert statements to compare the actual status code to expected values based on the search scenario. We also assert the length of the poems list in the response to ensure it matches the expected number of poems found.|
|Cat Facts API |  Get a Random Cat Fact | 1.Import the requests library. 2.Set the base URL for the Cat Facts API: https://catfact.ninja/fact. 3.Send a GET request to the base URL. 3.Extract the status code from the response. 4.Assert that the status code is 200 (OK). 5.Parse the JSON response to extract the cat fact. 6.Validate that the response contains a fact about cats.| -Status code: 200 (OK)  -JSON response containing a string representing a cat fact.| -Assert statements to verify the expected status code and the presence of a fact in the response. Also perform additional checks on the fact content using regular expressions or string comparisons if desired.|
|Cat Facts API | Retrieve Multiple Cat Facts | 1.Import the requests library. 2.Set the base URL for the Cat Facts API: https://catfact.ninja/facts. 3.Send a GET request to the cat-facts API endpoint to retrieve multiple cat facts. 4.Parse the response to extract the cat facts. 4.Verify that the response contains an array of cat facts with the specified count.| - The response should contain an array of cat facts with the specified count.-Each cat fact should be unique.| - Assert statements to Validate that the response status code is 200. -Validate that the response body contains an array of cat facts with the specified count.-Validate that each cat fact in the array is unique.|
