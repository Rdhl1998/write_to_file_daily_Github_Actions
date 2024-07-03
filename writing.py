'''
Created: 2024/07/03 
last modified: 2024/07/03 
Purpose of the file is to daily append the current day to the --> dates.txt file
The format will be  DD-MM-YYYY HH:MM:SS /n
'''

import datetime
x = datetime.datetime.now()

def write_to_file(filename, text):
    with open(filename,'w') as file:
        file.write(str(x))

filename = 'dates.txt'

write_to_file(filename, x)
print(x)
