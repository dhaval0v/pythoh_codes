class Bank:
    bid = 1
    bname = 'sbi'
    add = 'ahmd'
    bphno = 778899
    bemail = 'a@gmaio.com'

ob1 = Bank()
ob1.id = 1
ob1.name = 'aa'
ob1.emt = 10
ob1.code = 1
ob1.add = 'ahm1'

ob2 = Bank()
ob2.id = 2
ob2.name = 'bb'
ob2.emt = 12
ob2.code = 2
ob2.add = 'ahm2'


ob3 = Bank()
ob3.id = 3
ob3.name = 'cc'
ob3.emt = 13
ob3.code = 3
ob3.add = 'ahm3'


ob4 = Bank()
ob4.id = 4
ob4.name = 'dd'
ob4.emt = 9
ob4.code = 4
ob4.add = 'ahm4'


ob5 = Bank()
ob5.id = 5
ob5.name = 'ee'
ob5.emt = 16
ob5.code = 5
ob5.add = 'bj1'


ob6 = Bank()
ob6.id = 6
ob6.name = 'rr'
ob6.emt = 19
ob6.code = 6
ob6.add = 'ahm5'


ob7 = Bank()
ob7.id = 7
ob7.name = 'ss'
ob7.emt = 9
ob7.code = 7
ob7.add = 'bj2'


ob8 = Bank()
ob8.id = 8
ob8.name = 'ss'
ob8.emt = 13
ob8.code = 8
ob8.add = 'ahm6'


ob9 = Bank()
ob9.id = 9
ob9.name = 'gg'
ob9.emt = 13
ob9.code = 9
ob9.add = 'botad1'


ob10 = Bank()
ob10.id = 10
ob10.name = 'vv'
ob10.emt = 16
ob10.code = 10
ob10.add = 'ahm8'

'''Note = to reduce this much of time we use  init constructer
             ANd after creating user create one display function to display it '''



class Student:
    sname = 'a'
    sid = 1
    sphone = 1111

    def __init__(obj,mname,fname,phno):
        obj.mname = mname
        obj.fname = fname
        obj.phno = phno

    def display(obj):
        print(obj.mname,obj.fname,obj.phno)


s1 = Student('aaa','bbb',101010)
s1.display()

#or

Student.display(s1)
