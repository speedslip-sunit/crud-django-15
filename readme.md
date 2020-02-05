Since this application is a blueprint for CRUD API example. We are using inbuilt SQLite
datebase. For production uses 

### Create department
```
Request URL:
POST /api/department/add

Request Body:
{
	"name": "Operations"
}


Response:
{
    "department_id": "6f4628ff-11c9-4ba7-98cd-1909383ce578",
    "name": "Operations",
    "created_at": "2020-02-05T05:50:40.610441Z",
    "updated_at": "2020-02-05T05:50:40.610503Z"
}
```

### Get Department List
```
Request URL:
GET /api/department/list

Response:
[
    {
        "department_id": "6f4628ff-11c9-4ba7-98cd-1909383ce578",
        "name": "Operations",
        "created_at": "2020-02-05T05:50:40.610441Z",
        "updated_at": "2020-02-05T05:50:40.610503Z"
    }
]
```


## Update Department object
```
Request URL:
POST /api/department/interact/31e0fe6d-5d51-4aaa-90c4-38287a82c02c

Request Body:
{
	"name": "Sales 2.0"
}

Response Body:
{
    "department_id": "31e0fe6d-5d51-4aaa-90c4-38287a82c02c",
    "name": "Sales 2.0",
    "created_at": "2020-02-04T14:57:53.238086Z",
    "updated_at": "2020-02-05T05:56:31.977592Z"
}
```

### Delete Department object
```
Request URL:
DELETE /api/department/interact/31e0fe6d-5d51-4aaa-90c4-38287a82c02c
```

### Create Employee
```
Request URL:
POST /api/employee/add

Request body
{
	"name": "M James",
	"contract_employee": false,
	"age": 29,
	"address": "52, Jefferson Street, NY"
}

Response:
{
    "employee_id": "0805ffc3-3751-4199-926f-fe5545d2a1b2",
    "name": "M James",
    "contract_employee": false,
    "age": 29,
    "address": "52, Jefferson Street, NY"
}
```

### GET Employee List
```
Request URL
GET /api/employee/list

Response:
[
    {
        "employee_id": "0805ffc3-3751-4199-926f-fe5545d2a1b2",
        "name": "M James",
        "contract_employee": false,
        "age": 29,
        "address": "52, Jefferson Street, NY"
    }
]
```

### Update Employee
```
Request URL
POST /api/employee/interact/385afb36-96b4-4473-8531-7e77113bdb07

Request Body:
{
	"name": "J Thompson",
	"age": 47,
	"contract_employee": true
}

Response:
{
    "employee_id": "385afb36-96b4-4473-8531-7e77113bdb07",
    "name": "J Thompson",
    "contract_employee": true,
    "age": 47,
    "address": "52, Jefferson Street, NY"
}
```

### Delete Employee
```
Request URL
DELETE /api/employee/interact/385afb36-96b4-4473-8531-7e77113bdb07
```

