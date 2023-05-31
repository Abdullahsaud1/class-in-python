class Student :
    university_name = 'King Saud University' # اذ كان الجميع يملكون في الخاصيه نعرفه  خارج الداله و نطلبه 

    def __init__(self, name , age , iD , grades):
        self.name=name
        self.age=age
        self.iD=iD
        self.grades=grades
    def talk(self):
            print('He name is :',self.name , ' .He is  ',self.age  ,' He is id  and grades',self.iD ,'\n'+ 'grades' , self.grades)
            

std1 = Student('Abdullah', 25 , 201610468 , 93)     
std2 = Student('Saud' , 33 , 20192049 , 99)
std3 = Student('Abdullzaz ' , 23 , 20177657 , 90)
std4 = Student ('Wajdan' , 26 , 20184657 , 99)
std1.talk()
std2.talk()
std3.talk()
std3.talk()
std4.talk()
# #add
# std1.v_hours=55
# std2.v_hours = 44
# print(dir(std1))
# print(dir(std2))
# #del
# del std2.v_hours
# del std1.v_hours
# print(dir(std1))
# print(dir(std2))