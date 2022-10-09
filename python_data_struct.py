#In this example, there's a list of employees that work in a restaurant. 
# You need to be able to find an employee by their employee ID - 
#an integer-based numeric ID. The function get_employee contains a for loop to iterate over the list of 
#employees and returns an employee object if the ID matches.

employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]

def get_employee(id): 
    for employee in employee_list:
        if employee['id'] == id:
            return employee

print(get_employee(12458));
## OUTPUT
{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}

#OR using the dict data structure it is able to scale and handle more data.

employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id];


print(get_employee_from_dict(12458));
## OUTPUT
{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}