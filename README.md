<p align="center">
<img src="http://nano.sahaj.ai/logo.png" width="320" height="162" altText="Logo" title="NaN(O) logo">
</p>

# Employee Management - a NaN(O) problem

## What is NaN(O)

At Sahaj, tech consultants operate at the intersection between engineering and art. Simply put, they are artisans who take on complex engineering problems in the software industry across a wide spectrum of domains. Their work is deeply rooted in first principles thinking - asking fundamental questions to dissect and understand a problem which eventually leads to one-of-a-kind solutions, each as distinct as a fingerprint.

Through NaN(O), a hackathon driven by Sahaj across multiple colleges in India, they want to instill a culture of applying first principles thinking to a problem statement.

------

## Problem statement

We need a system to be able to manage data for employees. Requests will be accepted over HTTP ([API contract](#api-contract)). No databases/libraries can be used to store/maintain data.

------

### Technical details
1. Your repository needs to have a `Dockerfile` that starts your HTTP web app
2. Your HTTP app need to expose APIs ([API contract](#api-contract)) on port 8080
3. No existing databases, libraries and services can be used to store the data
4. Application needs to persist data across restarts
5. No limitation on the programming language
6. Do not touch the GitHub actions code. It is used to test your code automatically and score it. Any modifications will lead to immediate disqualification.
7. Maximum time a single request can take is 10 seconds

#### Data to be stored
```
{
    id: string,
    name: string,
    city: string
}
```

#### API contract
##### GET /greeting
  Checks whether the service is available.

###### Response
* Code: 200  
* Content: `Hello world!` 


##### POST /employee
Creates a new Employee and returns the employeeId

###### Request & Response headers
Content-Type: application/json

###### Body
```
{
    name: string,
    city: string
}
```

###### Success Response
* Status code: 201
* Content: `{ "employeeId": "<employee_id>" }` (Note: Employee ID is a `string`)


##### GET /employee/:id
Returns the specified employee.

###### URL Params
`id=[string]` *Required*

###### Success Response
* Status code: 200
* Content: `{ <employee_object> }`

###### Error Response
* Status code: 404
* Content: `{ message : "Employee with <employee_id> was not found" }`


##### GET /employee/all
Returns list of all employees.

###### Success Response
* Status code: 200
* Content: `[{ <employee_object> }]`


##### PUT /employee/:id
Updates fields of the existing employee and returns the new object.

###### URL Params
`id=[string]` *Required*

###### Headers
Content-Type: application/json

###### Body
```
{
    name: string,
    city: string
}
```

###### Success Response
* Code: 201
* Content: `{ <employee_object> }`

###### Error Response
* Code: 404
* Content: `{ message : "Employee with <employee_id> was not found" }`


##### DELETE /employee/:id
  Deletes existing employee record.

###### URL Params
`id=[string]` *Required*

###### Success Response
* Status code: 200
* Content:  `{ <employee_object> }`

###### Error Response
* Status code: 404
* Content: `{ message : "Employee with <employee_id> was not found" }`

----

## Competition rules

Check <a href="http://nano.sahaj.ai/rules.html" target="_blank">rules and scoring</a> pages for details. When in doubt, ask the organizers and we will add clarifications to the page.
