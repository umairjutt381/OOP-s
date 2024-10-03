class A:
    def __init__(self,sleep,eat) :
        self.sleep = sleep
        self.eat = eat
    def display(self):
        print(f"sleep:{self.sleep}\neat:{self.eat}")
        
class B:
    def __init__(self,age) :
        self.age = age
       
    def display(self):
        print (f"age:{self.age}")
       
class C(A, B):
    def __init__(self,sleep,eat,age,speak):
        A.__init__(self,sleep,eat)
        B.__init__(self,age)
        self.speak = speak
    def display(self):
        print (f"sleep:{self.sleep}\neat:{self.eat}\nage:{self.age}\nspeak:{self.speak}")
class D(C):
    def __init__(self,sleep,eat,age,speak,running,reading):           #constructor
        C.__init__(self,sleep,eat,age,speak)
        self.running = running
        self.reading = reading
    def display(self):
        print (f"sleep:{self.sleep}\neat:{self.eat}\nage:{self.age}\nspeak:{self.speak}\nrunning:{self.running}\nreading:{self.reading}")
       
class E(C):
    def __init__(self,sleep,eat,age,speak,jogging):
        C.__init__(self,sleep,eat,age,speak)
        self.jogging = jogging
    def display(self):
        print (f"sleep:{self.sleep}\neat:{self.eat}\nage:{self.age}\nspeak{self.speak}\njogging:{self.jogging}")
           
class F(D):
    def __init__(self,sleep,eat,age,speak,running,reading,walk):
        D.__init__(self,sleep,eat,age,speak,running,reading)
        self.walk = walk
    def display(self):
        print (f"sleep:{self.sleep}\neat:{self.eat}\nage:{self.age}\nspeak:{self.speak}\nrunning:{self.running}\nreading:{self.reading}\nwalk:{self.walk}")
       
        
c1 = F("6 hours", "meals", 25, "English", "daily", "novels", "evening")       
c1.display()
    
