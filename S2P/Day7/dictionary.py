student = {
    "name": "Chaitanya",
    "age": 22,
    "course": "CSE",
    "skills": ["Python", "Java", "SQL"]
}
print(student)

print(student["name"])   

# Add new key and value 
student["grade"] = "A"

# update the value with help of key
student["age"] = 23

# del used to delete the ele using key
del student["course"]

print(student)
