# Q7 : write a python script which takes a three digit number from user and displays only its last digit
take_num =  int ( input ( 'enter any three digit number :' ) )
print ( 'the last digit is {}' . format ( take_num % 10 ) )