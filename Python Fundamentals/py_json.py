# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#sample json
userJson='{"name":"bob","email":"bob@gmail.com","city":"boston","age":22}'
print(type(userJson),userJson)


# Parse to dict
user=json.loads(userJson)
print(user)
print(user["name"])

carJson={"modle":"Ford","price":345,"year":1999}

car=json.dumps(carJson)
print(car)