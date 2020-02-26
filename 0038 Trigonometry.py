import random
from mathsub import trigonometry as source

print('Generating...')
file_name = 'trigonometry'

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
TESTMODE = True

question_list = [source.median(),
source.angular_bisector(),
source.altitude(),
source.inradius_SSS(),
source.inradius_SAS(),
source.inradius_ASA(),
source.inradius(),
source.circumradius(),
source.exradius(),
source.area(),
source.airplane(),
source.elevation_person_building(),
source.elevation_two_person_building(),
source.inclined_post(),
]

concept_list = []

# concept_list = [
# source.identity()
# ]


if len(concept_list) == 0:
    CONCEPTS = False
else:
    CONCEPTS = True

if not TESTMODE:
    random.shuffle(question_list)
    random.shuffle(concept_list)

file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

if CONCEPTS:
    for i in range (min(len(question_list), len(concept_list))):
        print('-----------------------------------------------------------------------')
        item = random.choice([question_list[i], concept_list[i]])
        print_tasks(item)
        write_to_file(item)
else:
    for i in range (len(question_list)):
        print('-----------------------------------------------------------------------')
        item = question_list[i]
        print_tasks(item)
        write_to_file(item)

print()
file.close()
print('Finished.')
