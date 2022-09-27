class Parent:
    food="Yes"
    Shopping="Yes"
    work="No"
    
    def bank(self):
        print("Savings amount")

class fchild(Parent):
    
    def clothes(self):
        print("Clothes of first child")
    
    def phone(self):
        print("Phone of first child")
        
class schild(Parent):
    
    def laptop(self):
        print("Laptop of second child")
    
    def books(self):
        print("Books of second child")        

print("For First child food "+fchild.food)
print("For First child Shopping "+fchild.Shopping)
print("The Work for First Child "+fchild.work)   
fc=fchild()
fc.bank()
fc.clothes()
fc.phone()
print(fc.Shopping)

print("For second child food "+schild.food)
print("For second child Shopping "+schild.Shopping)
print("The Work for First Child "+schild.work)   
sc=schild()
sc.bank()
print(sc.Shopping)
sc.laptop()
sc.books()