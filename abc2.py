from abc import ABC, abstractmethod
class animal:
    def sound(self):
        pass

class lion(animal):
    def sound(self):
        print("roar....")

class dog(animal):
    def sound(self):
        print("bark....")

print("lion's sound")
cub=lion()
cub.sound()
print("dog's sound")
puppy=dog()
puppy.sound()
    
