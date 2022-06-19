class Employee:
    
    def __init__(self, name, salary, phone_number, start_date):
        self.name = name
        self.salary = salary
        self.start_date = start_date
        self.phone_number = phone_number
    
    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)
    
    def get_contact_details(self):
        return (self.name, self.phone_number)

employee_1 = Employee("Fran", 78000, "0472028842", "1st June 2020")
print(employee_1.get_employment_details())
print(employee_1.get_contact_details())
