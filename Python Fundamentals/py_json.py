# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

#sample json
userJson='{"name":"bob smith","age":22}'
print(type(userJson),userJson)

# Parse to dict
user=json.loads(userJson)
print(user)
print(user['name'])

carJson={'model':'BMW 3T','price':34567}
car=json.dumps(carJson)
print(car)