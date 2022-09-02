# Q6 : write a python script which takes a three digit number from user and displays only its middle digit
take_num =  int ( input ( 'enter any three digit number :' ) )
num = int ( take_num / 10 )
print ( 'the middle digit is {}' . format ( num % 10 ) )