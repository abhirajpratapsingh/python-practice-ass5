# Q5 : write a python script which takes a three digit number from the user and displays only its first digit 
take_num =  int ( input ( 'enter any three digit number :' ) )
num = int ( take_num / 10 )
print ( 'the first digit is {}' . format ( num // 10 ) )