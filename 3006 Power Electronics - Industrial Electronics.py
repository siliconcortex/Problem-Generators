
from generator import random_handler as ran
import sympy as sym
from sympy import init_printing
from sympy import oo

import math
import random

from electronics import power_electronics as powerelecs

x, y = sym.symbols('x y', real = True)

from generator import constants_conversions as c




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Power Electronics
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
powerelecs.fewson_2_1(),
powerelecs.fewson_2_2(),
powerelecs.fewson_2_3(),
powerelecs.fewson_2_4(),
powerelecs.fewson_2_5(),
powerelecs.fewson_3_1(),
powerelecs.fewson_3_3(),
powerelecs.fewson_3_4(),
powerelecs.fewson_3_5(),
powerelecs.fewson_3_6(),
powerelecs.fewson_3_7(),
powerelecs.fewson_3_8(),
powerelecs.fewson_3_9(),
powerelecs.fewson_3_10()
)


#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(1 * len(questionList)))


print(title_string)
print()
print(items_list)

for i in range (len(items_list)):
    print('-----------------------------------------------------------------------')
    item = questionList[items_list[i]]
    print(item.question)
    print()
    print(item.answer)

stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
