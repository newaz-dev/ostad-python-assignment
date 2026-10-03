import json

student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE"
}

json_string = json.dumps(student)

print(json_string)