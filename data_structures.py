'''
Relation Class
This class represents my database relation
Each relation object stores:
- name: The name of the relation
- attributes: A list of attribute names (columns)
- rows: A list of tuples, where each tuple represents a row of data
Example:
    Employees (EID, Name, Age) = {
        {"EID": "E1", "Name": "John", "Age": 32},
        {"EID": "E2", "Name": "Alice", "Age": 28}
    }
This class also include a print method to display the relation's details
'''
class Relation:
    def __init__(self, name, attributes, rows):     #Constructor (For new relation objects)
        self.name = name                            #Name of the relation
        self.attributes = attributes                #Attributes (columns) of the relation
        self.rows = rows                            #Data rows of the relation

    def print_tables(self):                         #Method to print the relation's details
        print(f"Attributes: {self.attributes}")     #Print attributes
        for row in self.rows:
            print(f"Value: {row}")                  #Print each row's values