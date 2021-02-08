# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#sample json
userJson='{"fullName":"htin kyaw","email":"htin@gmail.com","age":22}'

print(type(userJson),userJson)

# Parse to dict
user=json.loads(userJson)
print(user)
print(user['fullName'])

car={'make':'ford','model':'ford ma','year':1999}

carJson=json.dumps(car)
print(carJson)