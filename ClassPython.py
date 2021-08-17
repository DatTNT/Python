# 1. Class

# Class là gì??
# 	– Các class đều được tạo ra bằng từ khóa class.

# 	– Các thuộc tính chính là các biến thuộc về class.

# 	– Các thuộc tính thường là public, và có thể được truy cập tới bằng cách sử dụng toán tử dấu chấm (.), ví dụ: Myclass.Myattribute.

# # creates a class named MyClass
# class MyClass:
#     # assign the values to the MyClass attributes
#     number = 0
#     name = "noname"


# def Main():
#     # Creating an object of the MyClass.
#     # Here, 'me' is the object
#     me = MyClass()

#     # Accessing the attributes of MyClass
#     # using the dot(.) operator
#     me.number = 1337
#     me.name = "Harssh"

#     # str is an build-in function that
#     # creates an string
#     print(me.name + " " + str(me.number))


# # telling python that there is main in the program.
# if __name__ == '__main__':
#     Main()

# *************************************************************************************************************

# 2. Method
# A Python program to demonstrate working of class
# methods
#   – Hàm mà thuộc về một class cụ thể thì được gọi là Phương thức.

#   – Tất cả các phương thức đều yêu cầu tham số ‘self’. Nếu bạn đã từng code trên các ngôn ngữ OOP khác,
#   thì ‘self’ trong Python chính là ‘this’ ở trong các ngôn ngữ đó. ‘self’ và ‘this’ đều mang ý nghĩa là một đối tượng hiện tại của một class nào đó.

# class Vector2D:
#     x = 0.0
#     y = 0.0

#     # Creating a method named Set
#     def Set(self, x, y):
#         self.x = x
#         self.y = y


# def Main():
#     # vec is an object of class Vector2D
#     vec = Vector2D()

#     # Passing values to the function Set
#     # by using dot(.) operator.
#     vec.Set(5, 6)
#     print("X: " + str(vec.x) + ", Y: " + str(vec.y))


# if __name__ == '__main__':
#     Main()

# X: 5, Y: 6


# *************************************************************************************************************

# 2. KẾ THỪA (INHERITANCE)
# - Cách mà một class cụ thể sẽ kế thừa lại các tính năng từ một base class – tức là lớp cha/lớp cơ sở.
# Base class còn được gọi là ‘Superclass’, và class mà kế thừa từ Superclass thì được gọi là ‘Subclass’ tức là lớp con.

# class derived-classname(superclass-name)

# A Python program to demonstrate working of inheritance


class Pet:
    # __init__ is an constructor in Python
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Class Cat inheriting from the class Pet


class Cat(Pet):
    def __init__(self, name, age):
        # calling the super-class function __init__
        # using the super() function
        super().__init__(name, age)


def Main():
    thePet = Pet("Pet", 1)
    jess = Cat("Jess", 3)

    # isinstance() function to check whether a class is
    # inherited from another class
    print("Is jess a cat? " + str(isinstance(jess, Cat)))
    print("Is jess a pet? " + str(isinstance(jess, Pet)))
    print("Is the pet a cat? "+str(isinstance(thePet, Cat)))
    print("Is thePet a Pet? " + str(isinstance(thePet, Pet)))
    print(jess.name)


if __name__ == '__main__':
    Main()


#  Result:
#     Is jess a cat? True
#     Is jess a pet? True
#     Is the pet a cat? False
#     Is thePet a Pet? True
#     Jess


# *************************************************************************************************************


# Iterators là các đối tượng mà chúng ta có thể thực hiện các phép lặp/duyệt trên chúng.

#   – Python sử dụng phương thức __iter__() để trả về một đối tượng iterator của class

#   – Đối tượng iterator sau đó sẽ sử dụng phương thức __next__() để lấy được next item – phần tử tiếp theo.

#   – Vòng lặp for sẽ dừng lại khi ngoại lệ StopIteration Exception được kích hoạt.

# # This program will reverse the string that is passed
# # to it from the main function
# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index-= 1
#         return self.data[self.index]

# def Main():
#     rev = Reverse('Drapsicle')
#     for char in rev:
#         print(char)

# if __name__=='__main__':
#     Main()

# e
# l
# c
# i
# s
# p
# a
# r
# D


# *************************************************************************************************************


# 5. Generators

#   – Sử dụng generator là một cách khác để tạo ra các iterators.

#   – Thay vì phải sử dụng một class riêng biệt, ta chỉ cần sử dụng tới một hàm.

#   – Tạo ra phần code cơ sở dành cho phương thức/hàm next() và iter()

#   – Sử dụng một câu lệnh đặc biệt được gọi là ‘yield’ giúp lưu lại trạng thái (state) của generator và thiết lập một điểm trở về – resume point nhằm dự phòng cho trường hợp hàm next() được gọi lại lần nữa.

#   Dưới đây là đoạn chương trình Python mô tả hoạt động của các Generators


# # A Python program to demonstrate working of Generators
# def Reverse(data):
#     # this is like counting from 100 to 1 by taking one(-1)
#     # step backward.
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]


# def Main():
#     rev = Reverse('Harssh')
#     for char in rev:
#         print(char)
#     data = 'Harssh'
#     print(list(data[i] for i in range(len(data)-1, -1, -1)))


# if __name__ == "__main__":
#     Main()


# h
# s
# s
# r
# a
# H
# ['h', 's', 's', 'r', 'a', 'H']
