# division and square
def divide_or_square(number):
    if number % 5 == 0:
        square_root = number ** 0.5
        print(f"The square root of {number} is: {round(square_root,2)}")
    else:
        num_remainder = number % 5
        print(f"The remainder of {number} after dividing by 5 is: {num_remainder}")

number = int(input("Enter a number here: "))       
divide_or_square(number)

# strings to integers
def convert_add(nums):
    sum = 0
    for x in nums:
        sum += int(x)
    print('The sum of {} is: {}'.format(nums,sum))
    
# num1 = input("Enter your first number here: ")
# num2 = input("Enter your second number here: ")
# num3 = input("Enter your third number here: ")

# nums = [num1 , num2 , num3]
nums = ['1', '3', '5']
convert_add(nums)

# register
def register_check(register):
    return len([register.values() for v in register.values() if v == 'yes'])

register = {
    'Michael': 'yes',
    'John': 'no',
    'Peter': 'yes',
    'Mary': 'yes'
}
print(f'The number of students in class are {register_check(register)}')

# only floats
def only_floats(a,b):
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0
    
print(only_floats(12.1, 23))

# discount
def my_discount():
    price = int(input("Enter your price here: "))
    discount = input("Enter the discount percentage here: ")
    discount = discount.replace('%', '')
    new_discount = float(discount)
    price_after_discount = price * (100-new_discount)/ 100
    print(price_after_discount)
    
my_discount()

# user name generator
def user_name():
    email = input('Enter your email address here: ')
    if '@' in email:
        split = email.split('@')
        print(split)
        print(f'Your username is: {split[0]}')
    else:
        print("Enter valid email address!")
    
user_name()

# string range
def string_range(num):
    str_list = []
    for x in range(num):
        str_list.append(x)
        range_str = '{}.{}'.format(str_list[0], str_list[-1])
        str_list[0] = range_str
    print(range_str[2:])
    
string_range(6)

# odd and even
def odd_even(num_list):
    even = list()
    odd = list()
    for x in num_list:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    difference = max(even)-min(odd)
    print(f'{max(even)} - {min(odd)} = {difference}')
           
num_list = [1,2,4,6]
odd_even(num_list)

# biggest odd number
def biggest_odd(num_string):
    num_list = []
    for y in num_string:
        num_list.append(int(y))
    print(num_list)
    odd = [x for x in num_list if x % 2 == 1]
    print(f'The largest odd number in {num_string} is {max(odd)}')

num_string = '23569'
biggest_odd(num_string)

# hide my password
def hide_password():
    password_list = list()
    password = input('Enter your password here: ')
    for x in password:
        x = '*'
        password_list.append(x)
        hidden_password = f'{password_list[0]}{password_list[-1]}'
        password_list[0] = hidden_password
    print(f'Your password is {hidden_password[1:]} and it is {len(hidden_password[1:])} characters long.')

hide_password()

# Strings With a Thousand Separator
def convert_numbers(num_list):
    str_list = list()
    for number in num_list:
        sep_num = str(number)
        
        str_list.append()
    print(str_list)

num_list = [1000000, 2356989, 2354672, 9878098]        
convert_numbers(num_list)
        

    