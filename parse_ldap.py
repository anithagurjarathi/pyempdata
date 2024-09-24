class EmployeeData:
    def __init__(self, fullname, hiredate, username,employeestatus, employeeid, managerid):
        self.full_name = fullname
        self.hire_date = hiredate
        self.username = username
        self.status = employeestatus
        self.employee_id = employeeid
        self.manager_id = managerid
        self.manager = None

    def get_management(self):
        chain = []
        current = self
        if current.manager_id==current.employee_id:
            return f"{current.username} -> {current.username}"
        while True:
            chain.append(current.username)
            if current.manager == current: 
                break
            current = current.manager
            if current is None:  
                break
        return ' -> '.join(chain)

    def set_manager(self, manager):
        self.manager = manager

   

def emp_data(filepath):
    employees = {}
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()

    emp_data = {}
    for line in lines:
        if line.strip() == "":
            employee = EmployeeData(
                emp_data['fullname'],
                emp_data['hiredate'],
                emp_data['username'],
                emp_data['employeestatus'],
                emp_data['employeeid'],
                emp_data['managerid']
            )
            employees[employee.employee_id] = employee
            emp_data = {}
        else:
            key, value = line.split(": ", 1)
            emp_data[key.lower()] = value

    return employees

def assign_managers(employees):
    
    for employee in employees.values():
        
        if employee.manager_id == employee.employee_id:
            employee.set_manager(employee)
        elif employee.manager_id in employees:
            employee.set_manager(employees[employee.manager_id])


def print_management(employees):
    for employee in employees.values():
        if employee.status == "Active":
            print(employee.get_management())

if __name__ == '__main__':
    filepath = 'ldap_output.txt'  
    employees = emp_data(filepath)
   
    assign_managers(employees)
    print_management(employees)
