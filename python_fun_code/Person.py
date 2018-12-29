
class Person:
       def __init__(self, first_name, age):
           self.first_name = first_name
           self._age = age


       def _show_age(self):
           return self._age
