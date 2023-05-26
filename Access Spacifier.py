#Access Spacifier :-

#--Access Spacifier is used to restrict access to the variable and methods of the class.
#--There are three forms of access modifiers.

#---1.Public:
#   The members of class are declared public are easily accessible from any part of the program.

#---2.Protected:
#   The members of class are declared protected are only accessible to class derived from it.

#---3.Private:
#   The members of class are declared private are accessible with the class only.


class sample:
    id=100
    _Name='Geeky Shows'
    __Sal=45000
    def m1(self):
        print(sample.id)
        print(sample._Name)
        print(sample.__Sal)

obj=sample()
obj.m1()


class sample:
    id = 100
    _Name = 'Geeky Shows'
    __Sal = 45000

obj = sample()

print(sample.id)
print(sample._Name)
print(obj._sample__Sal)
