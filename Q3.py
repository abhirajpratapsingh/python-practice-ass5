# Q3 : write a python script to swap data of two variables
print ( 'enter two number :' )
take_num1 , take_num2 = int ( input ('first :') ) , int ( input ('second :') )
print ( 'before swapping \nfirst = {} , second = {}' . format ( take_num1 , take_num2 ) )
take_num1 , take_num2 = take_num2 , take_num1
print ( 'after swapping \nfirst = {} , second = {}' . format ( take_num1 , take_num2 ) )