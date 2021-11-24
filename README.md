  # Advisor_Network_Django
  ```
  Backend Assignment (Python)
  1. Make APIs using Django (or any other Python-based Web framework) for an advisor
  network where users can come and book an advisor for a call.
  a. The following roles should be allowed
  i. Admin
  1. API: Add an advisor
  a. Method:
  i. POST
  b. Authentication
  i. Not needed for this assignment
  c. Endpoint:
  i. /admin/advisor/
  d. Request:
  i. Advisor name
  ii. Advisor Photo URL
  e. Response:
  i. No Response
  ii. Just return 200_OK if the request is successful
  iii. Return 400_BAD_REQUEST if any of the above
  fields are missing
  ii. User
  1. API: Can register as a user
  a. Method:
  i. POST
  b. Endpoint:
  i. /user/register/
  c. Request:
  i. Name
  ii. Email
  iii. Password
  d. Response:
  i. Body:
  1. JWT Authentication Token
  2. User id
  ii. Status
  1. 200_OK if the request is successful
  2. 400_BAD_REQUEST if any of the above
  fields are missing
  2. API: Can log in as a user
  a. Method:
  i. POST
  b. Endpoint:
  i. /user/login/
  c. Request:
  i. Email
  ii. Password
  d. Response:
  i. Body:
  1. JWT Authentication Token
  2. User id
  ii. Status
  1. 200_OK if the request is successful
  2. 400_BAD_REQUEST if any of the above
  fields are missing
  3. Return
  401_AUTHENTICATION_ERROR if the
  email/password combination was wrong
  3. API: Get the list of advisors
  a. Method:
  i. GET
  b. Endpoint:
  i. /user/<user-id>/advisor
  c. Request:
  i. None
  d. Response:
  i. Body:
  1. An array of advisor objects with each
  object having
  a. Advisor Name
  b. Advisor Profile Pic
  c. Advisor Id
  ii. Status
  1. 200_OK if the request is successful
  4. API: Can book call with an advisor
  a. Method:
  i. POST
  b. Endpoint:
  i. /user/<user-id>/advisor/<advisor-id>/
  c. Request:
  i. Booking time (a DateTime string)
  d. Response:
  i. Body:
  1. None
  ii. Status
  1. 200_OK if the request is successful
  5. API: Can get all the booked calls
  a. Method:
  i. GET
  b. Endpoint:
  i. /user/<user-id>/advisor/booking/
  c. Request:
  i. None
  d. Response:
  i. Body:
  1. An array of advisor objects with each
  object having
  a. Advisor Name
  b. Advisor Profile Pic
  c. Advisor Id
  d. Booking time
  e. Booking id
  ii. Status
  1. 200_OK if the request is successful
  ```
