from abc import ABC, abstractmethod
class abc_class:

    def print(self,x):
        print("passed value",x)

    @abstractmethod
    def task(self):
        print("you are in abc_calss task def")


    
class  testlass(abc_class):
    def task(self):
        print("you are in testclass")

obj=testlass()
obj.task()
obj.print(503)

