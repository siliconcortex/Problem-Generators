import random
from geas import physics as source

print('Generating...')
file_name = 'impulse_momentum'

import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
folderpath = os.path.dirname(os.path.realpath(__file__))

def write_to_file(some_object):   
    if FILEMODE: 
        file.write(some_object.question)
        file.write('\n')
        file.write(some_object.answer)
        file.write('\n\n')

def print_tasks(some_object):
    print(some_object.question)
    print()
    print(some_object.answer)
    print()
    print()

FILEMODE = True
TESTMODE = False

question_list = [
source.Schaums_8_1(),
source.Schaums_8_1(),
source.Schaums_8_2(),
source.Schaums_8_3(),
source.Schaums_8_4(),
#source.Schaums_8_5(),
source.Schaums_8_6(),
#source.Schaums_8_7(),
source.Schaums_8_9(),
source.Schaums_8_10(),
source.Schaums_8_11(),
source.Schaums_8_12(),
source.Schaums_8_13(),
source.Schaums_8_14(),
source.Schaums_8_15(),
source.Schaums_8_16(),
source.Schaums_8_17()
]


total_items_list = question_list
    
if not TESTMODE:
    items_list = random.sample(total_items_list, round(1 * len(question_list)))
else:
    items_list = total_items_list

print(items_list)
file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

for i in range (len(items_list)):

    print('-----------------------------------------------------------------------')
    item = question_list[i]
    print_tasks(item)
    write_to_file(item)


print()
file.close()
print('Finished.')

stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
