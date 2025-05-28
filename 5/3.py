
class India():
    def capital(self):
        print("New Delhi")
        
    
    def language(self):
        print("Hindi")
        
    
class USA():
    def capital(self):
        print("Washington D.C.")
        
    
    def language(self):
        print("English")
        
    
class Japan():
    def capital(self):
        print("Tokyo")
        
    
    def language(self):
        print("Japanese")
        
    
class France():
    def capital(self):
        print("Paris")
        
    
    def language(self):
        print("French")
        
    
class Germany():
    def capital(self):
        print("Berlin")
        
    
    def language(self):
        print("German")
        
    
class Brazil():
    def capital(self):
        print("Brasília")
       
    
    def language(self):
        print("Portuguese")
        
    
class China():
    def capital(self):
        print("Beijing")
        
    
    def language(self):
        print("Chinese")
        
    
class Russia():
    def capital(self):
        print("Moscow")
        
    
    def language(self):
        print("Russian")
        
    
class SouthAfrica():
    def capital(self):
        print("Pretoria")
        
    
    def language(self):
        print("Zulu, Xhosa, Afrikaans, English")
       
    
class Australia():
    def capital(self):
        print("Canberra")
        
    
    def language(self):
        print("English")
        
    

obj_india = India()
obj_usa = USA()
obj_japan = Japan()
obj_france = France()
obj_germany = Germany()
obj_brazil = Brazil()
obj_china = China()

for country in [obj_india, obj_usa, obj_japan, obj_france, obj_germany, obj_brazil, obj_china]:
    country.capital()
    country.language()
