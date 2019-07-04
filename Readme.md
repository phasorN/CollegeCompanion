# CollegeCompanion

A simple REST API (a backend) to create applications to manage:
* *day to day expenses* 
* *attendance*

#### How is the user authenticated?
- User creates an account
- User sends their username and password to the API to get an access-token
- The access-token is used in all further requests to the API for authorization(tell the API the identity of the user).

`django-oauth-toolkit` is used to provide token based authentication and authorisation.

## Resources:
- User:
  - first_name
  - last_name
  - username *
  - password *
  - email
- Expense:
  - title *
  - amount *
  - date *
  - description
- Subject:
  - title *
  - user *
- Period:
  - subject *
  - time *
  - day *
  - venue
  - period_number
- Attendance:
  - period *
  - date *
  - value_int *
  - value_str


## Endpoints:
### Type 1
GET: Get the list of all the instances of resource owned by the user.

POST: Create a new instance of the resource.
#### `/users/`
`POST`
#### `/expenses/` _Login Required_
`GET` `POST`
#### `/subjects/` _Login Required_
`GET` `POST`
#### `/periods/` _Login Required_
`GET` `POST`
#### `/attendances/` _Login Required_
`GET` `POST`

### Type 2
GET: Get the details of the resource.

PUT: Update all the fields of the resource.

PATCH: Update some fields of the resource.

DELETE: Delete the resource. 

#### `/users/{userId}` _Login Required_
`GET` `PUT` `PATCH` `DELETE`
#### `/expenses/{expenseId}` _Login Required_
`GET` `PUT` `PATCH` `DELETE`
#### `subjects/{subjectId}` _Login Required_
`GET` `PUT` `PATCH` `DELETE`
#### `/periods/{periodId}` _Login Required_
`GET` `PUT` `PATCH` `DELETE`
#### `/attendances/{attendanceId}` _Login Required_
`GET` `PUT` `PATCH` `DELETE`

## A Sample Run

### Creating the client application credentials:
- Open terminal in your working directory and create a superuser using the command `python manage.py createsuperuser`
- Go to [site_url]/admin and login using the superuser.
- After logging in, go to [site_url]/o/applications/ and add a new application.
- Enter an application name and select **Client Type** as _**Confidential**_ and **Authorisation Grant Type** as **Resource Owner Password Base**_.
- Save the application.
- Note down the Client Id and Client Secret.

### Registration:
The user sends a POST request to /users/ with the user details (Given in the Resources chapter)

### Login(Getting the access token):

TODO

### Expenses:

TODO

### Attendances:
#### Add Subjects
#### Add Periods
#### Mark Attendances