class Student():
    def __init__(self,name,math_mrk,sci_mrk,ssc_mrk):
        self.name=name
        self.math_mrk=math_mrk
        self.sci_mrk=sci_mrk
        self.ssc_mrk=ssc_mrk
    def average(self):
        add=self.math_mrk+self.sci_mrk+self.ssc_mrk 
        avr=add/2
        print(self.name,"you marks average is",avr)
        
        
s1=Student("naitik",99,97,89)
s1.average()  