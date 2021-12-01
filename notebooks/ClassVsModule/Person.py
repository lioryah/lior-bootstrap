'''
class organism:
  id : int

class person(organism):
 
  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender
    print("in class person")
 
  def person_details(self):
    print(f'Person Name: {self.name} \nPerson Age: {self.age} \nPerson Gender: {self.gender}\n')

'''
