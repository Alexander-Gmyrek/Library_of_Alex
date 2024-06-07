# Database API Overview

Created: June 6, 2024 6:18 PM

## Understanding The API

### What It Does

This API allows you to interact with the billing database.

### How It Does It

The billing database has 7 tables

1. Employer
2. Employee
3. Tier
4. Carrier
5. Plan
6. EmployeePlan
7. Dependent

Each of these is treated like a class. Each class has an associated Json. These Jsons contain all the columns in the table and the sub table’s Jsons.* So an Employer Json would have “employees”: {”employee_json”}, inside of it’s Json. The sub Jsons are mostly used for adding and aren’t included in the returned Jsons unless requested. 

These classes also have default methods 

Setters:

- Add: Adds an item to the database (POST)
    - Takes: Class Json
    - Does: Adds the item and sub items
    - Returns: ID of element
- Change: Changes the item in the database (PATCH)
    - Takes: Item ID and Partial Class Json
    - Does: Changes all the values of the item in the class database to the given values. (Only changes the given values and will set them to null if no value is given)
    - Returns: Item ID
- Delete: Deletes and Item from the database(DELETE)
    - Takes: Item ID
    - Does: Deletes the item and cascades downwards if specified in db set up.
    - Returns: nothing

Getters:

- /TableName: This will get all elements of the table
- /TableName/ID: This will get the element with that id from the table
- /TableName/search: This takes a Partial Class Json and Searches for all elements that match the data in the partial class json
- There are also custom getters that will be discussed later

## Using The API

To use the API follow the read me for set up instructions and send requests to [localhost:5000](http://localhost:5000) (Or whatever it’s location turns out to be if it changes). There are a few helper methods you can use like  [localhost:5000](http://localhost:5000)/api to check if the API is up or  [localhost:5000](http://localhost:5000)/testconnection to test the connection to the database. Then you have all of the default class methods along with some class specific getter methods.

(Assume Class has required method unless otherwise specified. I am going to try to only include unique class requests while still making it understandable so only employer will have all its methods.)

### Employer

**Cascading Class Json:**

```python
{
        "EmployerID": 1,
        "EmployerName": "Test Employer 1",
        "TierStructure": "4Tiered",
		    "UsesGlCode": BOOLEAN,
		    "UsesDivision": BOOLEAN,
		    "UsesLocation": BOOLEAN,
		    "UsesTitle": BOOLEAN,
		    "PerferedBillingDate": DATE,
		    "RenewalDate": DATE,
        "employees": {"Employee_Json_Here"},
        "carriers": {"Carrier_Json_Here"},
        "tiers": {"Tier_Json_Here"},
        "Plans": {"Plan_Json_Here"},    
}
```

**Base Path:**  [localhost:5000](http://localhost:5000)/employer

Setters:

- ADD: Rout: /employer Method: [POST] Request: Complete Employer Json (Employee Sub jsons do not need employeePlans but they will need carrier and tier/dob if it is not included)
- CHANGE: Rout: /employer/<EmployerID> Method: [PATCH] Request: Partial Json
- DELETE: Rout: /employer/<EmployerID> Method: [DELETE]

Getters: 

- Get All Employers: Rout: /employer Method: [GET] Returns: all employers
- Get Employer By ID: Rout: /employer/<EmployerID> Method: [GET] Returns: Employer Json with that ID
- Search Employer By Name: Rout: /employer/<EmployerName> Method: [GET} Returns: All employers with names “like” that name
- Search For Employer: Rout: /employer/search Method: [GET] Request: Partial class Json. Returns: all employers with matching data

### Carrier

**Cascading Class Json:**

```python
{
     "CarrierID": 1,
     "EmployerID": 1,
     "CarrierName": "Carrier1",
}
```

**Base Path:**  [localhost:5000](http://localhost:5000)/carrier

Setters:

- All Default Setters

Getters:

- All Default Getters
- Search Employer For Carrier: Rout: /carrier/<EmployerID>/<CarrierName> Method: [GET] Returns: All carriers with that employer with similar names

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

**Base Path:**  [localhost:5000](http://localhost:5000)/tier

Setters:

- All Default Setters

Getters:

- All Default Getters
- Search Employer For Tier: Rout: /tier/<EmployerID>/<TierName> Method: [GET] Returns: All tiers with that employer with similar names

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

**Base Path:**  [localhost:5000](http://localhost:5000)/employee

Setters:

- ADD: When adding employee an employee you should have wither EmployeePlans or Carrier and Tier. If EmployeePlans is left blank or not included, Then it will use carrier and tier to get the right plan. If the employee is age banded leave the tier blank to automatically calculate age band.
- Change: Don’t try to change the Carrier or Tier with this method you need to change the employee plan or more likely create a new one with the new plan.
- Delete: Cascades to Dependent and EmployeePlan

Getters:

- Search Employer For Employee: Rout: /employee/<EmployerID>/<EmployeeFullName> Method: [GET] Returns: all employees with an employer with a similar name.
- Get Active Employees: Rout: /employee/<EmployerID>/active Method: [Get] Returns: All employees that have not been terminated.

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

**Base Path:**  [localhost:5000](http://localhost:5000)/employeeplan

Setters:

- Delete: In general you want to end an old plan and add a new one not delete but it’s here if you want it.

Getters:

- Get Active Employee Plan: Rout: /employeeplan/<EmployeeID>/active Method: [Get] Returns: Any employee plans that have not been ended

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

**Base Path:**  [localhost:5000](http://localhost:5000)/employeeplan

Setters:

- Delete: In general you want to add an end date not delete but it’s here if you want it.

Getters:

- Search Employer For Dependent: Rout: /dependent/<EmployerID>/<DependentName> Method: [Get] Returns: Any Dependents with employer with a similar name.

### Plan

**Cascading Class Json:**

```python
{
  "PlanID":1,
  "EmployerID": 1,
  "CarrierID": 1,
  "TierID": 1,
  "FundingAmount": 12.00,
  "GrenzFee": 2.00,
  "GrenzFeeC": 1.00,
  "GrenzFeeS": 1.00,
}
```

**Base Path:**  [localhost:5000](http://localhost:5000)/plan

Setters:

- All Default Setters

Getters:

- All Default Getters

## API Blueprint