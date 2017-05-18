#def add1(a,b):
#	return (a+b)
class person:
    def setFullName(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    def printFullName(self):
        print(self.firstName," ",self.lastName)
personName=person()
personName.setFullName("vishal","raut")
personName.printFullName()