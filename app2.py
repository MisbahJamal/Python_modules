# def func_name(name):
#     print(name)
# func_name("Jamal")


# def add(num_1, num_2):
#     result = num_1 + num_2
# print(result)
# add = (1,4)

 #arguements and keyword args**
def student(name, **data):
    print(name)
    print(data)
    student('Jamal', roll_no=3812)
    
# student('Jamal', roll_no=3812, age=20)  # Output: