#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num>0:
        print(num)
        num-=1
    print('Happy New Year!')

def square_integers(int_list):
    sq_list = []
    for num in int_list:
       sq_num = num**2
       sq_list.append(sq_num)
    return sq_list

def fizzbuzz():
    for num in range(1,101):
        if num%3 + num%5 == 0:
            print('FizzBuzz')
        elif num%3 == 0:
            print('Fizz')
        elif num%5 == 0:
            print('Buzz')
        else:
            print(num) 

