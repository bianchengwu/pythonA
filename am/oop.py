a=10
b=20
def show(a,b):
    return a+b

#创建一个类 所有类都默认继承object
#类名与Java相同，第一个字母大写（模块、函数都采用下划线命名法）
class Person(object):
#双下划线开始结束的特殊方法，此方法在适当时候会自动调用
#此方法在创建对象时实现赋值功能
#self代表当前对象，默认所有方法的self都不需要自己赋值
    def __init__(self,name,age):
        print('_init_')
#所有的方法默认第一个参数，此参数系统会自动复制
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

class Son(Person):
    def __init__(self,name,age,tel):
        Person.__init__(self,name,age)
        self.tel=tel
    def show(self):
        print(self.name,self.age,self.tel)

#__name__特殊属性，如果

s1=Son('张三',18,177331324)
s1.show()

p1=Person("李四",20)
p1.show()