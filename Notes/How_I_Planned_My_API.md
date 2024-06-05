# API Brain Blast

Ok so you  have classes (aka tables)

## Classes

- Employer
- Employee
- Plan
- Tier
- Carrier
- Dependent
- EmployeePlan

For each of these classes you need to be able to 

ADD a new one (PUT)

CHANGE an existing one (PATCH)

DELETE one (DELETE)

Parts of these functions:

- ADD:
    - Takes: The cascading class Json
    - Does: Adds everything to the class table and cascades to dependencies
    - Returns: The new ID
- CHANGE:
    - Takes: The ID and The new cascading class Json
    - Does: updates info in the class table then cascades to dependencies
    - Returns: Whether or not successful
- DELETE:
    - Takes: ID of object to delete
    - Does: deletes object and all dependencies
    - Returns: success or failure

### Employer

**Cascading Class Json:**

```python
{
        "employer_name": "Test Employer 1",
        "billing_system": "4Tiered",
        "employees": {"Employee_Json_Here"},
        "carriers": {"Carrier_Json_Here"},
        "tiers": {"Tier_Json_Here"},
        "Plans": {"Plan_Json_Here"},    
}
```

- ADD:
    1. Get the Json
    2. Add all info to employer table
    3. Use add carrier to add all the carriers
    4. Use add tier to add all the tiers
    5. Use add plan to add all the plans 
    6. Use add employee to add the employees
    7. Use check employer to ensure all info is there
- CHANGE:
    1. For each value in the Json, set the corresponding value in the table equal to the new value.
    2. Use check employer to ensure the db is consistent.
- DELETE:
    1. Just delete the employer at the id the db will handle the rest

### Carrier

**Cascading Class Json:**

```python
{
     "CarrierID": 1,
     "EmployerID": 1,
     "CarrierName": "Carrier1",
}
```

- ADD:
    1. Get the Json
    2. check if the carrier is already in the db and if not, Add the new carrier to the db
    3. return the id 
- CHANGE:
    1. For each value in the Json, set the corresponding value in the table equal to the new value.
    2. Use check employer to ensure the db is consistent.
    3. Return the result of check employer
- DELETE:
    1. Just delete the carrier at the id and the db will handle the rest

### Tier

**Cascading Class Json:**

```python
{
     "TierID": 1,
     "EmployerID": 1,
     "TierName": "Tier1",
     "MaxAge": 100,
     "MinAge": 0
}
```

- ADD:
    1. Get the Json
    2. check if the tier is already in the db and if not, Add the new tier to the db
    3. return the id 
- CHANGE:
    1. For each value in the Json, set the corresponding value in the table equal to the new value.
- DELETE:
    1. Just delete the tier at the id and the db will handle the rest

### Employee

**Cascading Class Json:**

```python
{
  "EmployeeID": 1,
  "EmployerID": 101,
  "EmployeeFullName": "John Doe",
  "EmployeeFirstName": "John",
  "EmployeeLastName": "Doe",
  "JoinDate": "2000-01-01",
  "TermDate": null,
  "JoinInformDate": "2000-01-01",
  "TermEndDate": null,
  "DOB": "1990-06-25",
  "CobraStatus": true,
  "Notes": "This is a sample note.",
  "GL": "GL12345",
  "Division": "Finance",
  "Location": "New York",
  "Title": "Financial Analyst",
  "Dependents": {"Dependent_Json_here"},
  "EmployeePlans":{"EmlployeePlan_Json_Here"}
  "Carrier": "Carrier1"
  "Tier": "Tier1"
}
```

- ADD:
    1. Get the Json
    2. Add all available employee info to employee table
    3. Use add dependent to add dependents
    4. if employee plans use add employee plan and skip to the end.
    5. Get CarrierID
    6. Get tier id with tier name or DOB if name not available
    7. get plan id
    8. add EmployeePlan
    9. return the id 
- CHANGE:
    1. For each value in the Json, set the corresponding value in the table equal to the new value.
    2. Use check employer to ensure the db is consistent.
    3. Return the result of check employer
- DELETE:
    1. Just delete the Employee at the id and the db will handle the rest

### EmployeePlan

**Cascading Class Json:**

```python
{
  "EmployeePlanID":1,
  "EmployeeID": 1,
  "PlanID": 101,
  "StartDate": DATE,
  "InformStartDate": DATE,
  "EndDate": DATE,
  "InformEndDate": DATE
}
```

- ADD:
    1. Get the Json
    2. Add all available employee info to employee table
    3. return the id 
- CHANGE:
    1. For each value in the Json, set the corresponding value in the table equal to the new value.
    2. Use check employer to ensure the db is consistent.
    3. Return the result of check employer
- DELETE:
    1. Just delete the EmployeePlan at the id and the db will handle the rest
    

### Dependent

**Cascading Class Json:**

```python
{
  "DependentID":1,
  "EmployeeID": 1,
  "DependentName": "Fake Name",
  "Relationship": "Spouce",
  "DOB": DATE,
  "StartDate": DATE,
  "InformStartDate": DATE,
  "EndDate": DATE,
  "InformEndDate": DATE
}
```

- ADD:
    1. Get the Json
    2. Add all available employee info to dependent table
    3. return the id 
- CHANGE:
    1. For each value in the Json, set the corresponding value in the table equal to the new value.
    2. Use check employer to ensure the db is consistent.
    3. Return the result of check employer
- DELETE:
    1. Just delete the Dependent at the id and the db will handle the rest

### Plan

**Cascading Class Json:**

```python
{
  "PlanID":1,
  "EmployerID": 1,
  "CarrierID": 1,
  "TierID"
  "FundingAmount": 12.00,
  "GrenzFee": 2.00,
  "GrenzFeeC": 1.00,
  "GrenzFeeS": 1.00
}
```

- ADD:
    1. Get the Json
    2. Add all available employee info to employee table
    3. return the id 
- CHANGE:
    1. For each value in the Json, set the corresponding value in the table equal to the new value.
    2. Use check employer to ensure the db is consistent.
    3. Return the result of check employer
- DELETE:
    1. Just delete the EmployeePlan at the id and the db will handle the rest