# Q2 : write a python script to get the last digit from a given number , number entered by user
# test case : input 2089 , output 9
take_num = int ( input ( "enter any number :" ) )
last_digit = take_num % 10
print ( "the last digit of {} is {}". format ( take_num , last_digit ) )