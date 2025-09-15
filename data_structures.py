class Relation:
    def function __init__(self, name, attributes, rows):
        self.name = name
        self.attributes = attributes  
        self.rows = rows  
    def print_tables():
        print(f"Atributes: {self.attributes}")
        for row in self.rows:
            print(f"Value: {row}")    