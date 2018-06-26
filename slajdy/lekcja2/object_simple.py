class Person:
    """Reprezentuje osobę"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_initials(self):
        """Zwraca inicjały danej osoby"""
        return self.first_name[0] + self.last_name[0]
