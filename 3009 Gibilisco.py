import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c
import gibilisco

x, y = sym.symbols('x y', real = True)



solutions_flag = False

title_string = """Gibilisco
Coded by Leslie Caminade Aug 2019 
www.lesliecaminadecom.wordpress.com"""

questionList = (
gibilisco.gibilisco_1_1(),
gibilisco.gibilisco_1_2(),
gibilisco.gibilisco_1_3(),
gibilisco.gibilisco_1_4(),
gibilisco.gibilisco_1_5(),
gibilisco.gibilisco_1_6(),
gibilisco.gibilisco_1_7(),
gibilisco.gibilisco_1_8(),
gibilisco.gibilisco_1_9(),
gibilisco.gibilisco_1_10(),
gibilisco.gibilisco_1_11(),
gibilisco.gibilisco_1_12(),
gibilisco.gibilisco_1_13(),
gibilisco.gibilisco_1_14(),
gibilisco.gibilisco_1_15(),
gibilisco.gibilisco_1_16(),
gibilisco.gibilisco_1_17(),
gibilisco.gibilisco_1_18(),
gibilisco.gibilisco_1_19(),
gibilisco.gibilisco_1_20(),
gibilisco.gibilisco_2_1(),
gibilisco.gibilisco_2_2(),
gibilisco.gibilisco_2_3(),
gibilisco.gibilisco_2_4(),
gibilisco.gibilisco_2_5(),
gibilisco.gibilisco_2_6(),
gibilisco.gibilisco_2_7(),
gibilisco.gibilisco_2_8(),
gibilisco.gibilisco_2_9(),
gibilisco.gibilisco_2_10(),
gibilisco.gibilisco_2_11(),
gibilisco.gibilisco_2_12(),
gibilisco.gibilisco_2_13(),
gibilisco.gibilisco_2_14(),
gibilisco.gibilisco_2_15(),
gibilisco.gibilisco_2_16(),
gibilisco.gibilisco_2_17(),
gibilisco.gibilisco_2_18(),
gibilisco.gibilisco_2_19(),
gibilisco.gibilisco_2_20(),
gibilisco.gibilisco_3_1(),
gibilisco.gibilisco_3_2(),
gibilisco.gibilisco_3_3(),
gibilisco.gibilisco_3_4(),
gibilisco.gibilisco_3_5(),
gibilisco.gibilisco_3_6(),
gibilisco.gibilisco_3_7(),
gibilisco.gibilisco_3_8(),
gibilisco.gibilisco_3_9(),
gibilisco.gibilisco_3_10(),
gibilisco.gibilisco_3_11(),
gibilisco.gibilisco_3_12(),
gibilisco.gibilisco_3_13(),
gibilisco.gibilisco_3_14(),
gibilisco.gibilisco_3_15(),
gibilisco.gibilisco_3_16(),
gibilisco.gibilisco_3_17(),
gibilisco.gibilisco_3_18(),
gibilisco.gibilisco_3_19(),
gibilisco.gibilisco_3_20(),
gibilisco.gibilisco_4_1(),
gibilisco.gibilisco_4_2(),
gibilisco.gibilisco_4_3(),
gibilisco.gibilisco_4_4(),
gibilisco.gibilisco_4_5(),
gibilisco.gibilisco_4_6(),
gibilisco.gibilisco_4_7(),
gibilisco.gibilisco_4_8(),
gibilisco.gibilisco_4_9(),
gibilisco.gibilisco_4_10(),
gibilisco.gibilisco_4_11(),
gibilisco.gibilisco_4_12(),
gibilisco.gibilisco_4_13(),
gibilisco.gibilisco_4_14(),
gibilisco.gibilisco_4_15(),
gibilisco.gibilisco_4_16(),
gibilisco.gibilisco_4_17(),
gibilisco.gibilisco_4_18(),
gibilisco.gibilisco_4_19(),
gibilisco.gibilisco_4_20(),
gibilisco.gibilisco_5_1(),
gibilisco.gibilisco_5_2(),
gibilisco.gibilisco_5_3(),
gibilisco.gibilisco_5_4(),
gibilisco.gibilisco_5_5(),
gibilisco.gibilisco_5_6(),
gibilisco.gibilisco_5_7(),
gibilisco.gibilisco_5_8(),
gibilisco.gibilisco_5_9(),
gibilisco.gibilisco_5_10(),
gibilisco.gibilisco_5_11(),
gibilisco.gibilisco_5_12(),
gibilisco.gibilisco_5_13(),
gibilisco.gibilisco_5_14(),
gibilisco.gibilisco_5_15(),
gibilisco.gibilisco_5_16(),
gibilisco.gibilisco_5_17(),
gibilisco.gibilisco_5_18(),
gibilisco.gibilisco_5_19(),
gibilisco.gibilisco_5_20(),
gibilisco.gibilisco_6_1(),
gibilisco.gibilisco_6_2(),
gibilisco.gibilisco_6_3(),
gibilisco.gibilisco_6_4(),
gibilisco.gibilisco_6_5(),
gibilisco.gibilisco_6_6(),
gibilisco.gibilisco_6_7(),
gibilisco.gibilisco_6_8(),
gibilisco.gibilisco_6_9(),
gibilisco.gibilisco_6_10(),
gibilisco.gibilisco_6_11(),
gibilisco.gibilisco_6_12(),
gibilisco.gibilisco_6_13(),
gibilisco.gibilisco_6_14(),
gibilisco.gibilisco_6_15(),
gibilisco.gibilisco_6_16(),
gibilisco.gibilisco_6_17(),
gibilisco.gibilisco_6_18(),
gibilisco.gibilisco_6_19(),
gibilisco.gibilisco_6_20(),
gibilisco.gibilisco_7_1(),
gibilisco.gibilisco_7_2(),
gibilisco.gibilisco_7_3(),
gibilisco.gibilisco_7_4(),
gibilisco.gibilisco_7_5(),
gibilisco.gibilisco_7_6(),
gibilisco.gibilisco_7_7(),
gibilisco.gibilisco_7_8(),
gibilisco.gibilisco_7_9(),
gibilisco.gibilisco_7_10(),
gibilisco.gibilisco_7_11(),
gibilisco.gibilisco_7_12(),
gibilisco.gibilisco_7_13(),
gibilisco.gibilisco_7_14(),
gibilisco.gibilisco_7_15(),
gibilisco.gibilisco_7_16(),
gibilisco.gibilisco_7_17(),
gibilisco.gibilisco_7_18(),
gibilisco.gibilisco_7_19(),
gibilisco.gibilisco_7_20(),
gibilisco.gibilisco_8_1(),
gibilisco.gibilisco_8_2(),
gibilisco.gibilisco_8_3(),
gibilisco.gibilisco_8_4(),
gibilisco.gibilisco_8_5(),
gibilisco.gibilisco_8_6(),
gibilisco.gibilisco_8_7(),
gibilisco.gibilisco_8_8(),
gibilisco.gibilisco_8_9(),
gibilisco.gibilisco_8_10(),
gibilisco.gibilisco_8_11(),
gibilisco.gibilisco_8_12(),
gibilisco.gibilisco_8_13(),
gibilisco.gibilisco_8_14(),
gibilisco.gibilisco_8_15(),
gibilisco.gibilisco_8_16(),
gibilisco.gibilisco_8_17(),
gibilisco.gibilisco_8_18(),
gibilisco.gibilisco_8_19(),
gibilisco.gibilisco_8_20(),
gibilisco.gibilisco_9_1(),
gibilisco.gibilisco_9_2(),
gibilisco.gibilisco_9_3(),
gibilisco.gibilisco_9_4(),
gibilisco.gibilisco_9_5(),
gibilisco.gibilisco_9_6(),
gibilisco.gibilisco_9_7(),
gibilisco.gibilisco_9_8(),
gibilisco.gibilisco_9_9(),
gibilisco.gibilisco_9_10(),
gibilisco.gibilisco_9_11(),
gibilisco.gibilisco_9_12(),
gibilisco.gibilisco_9_13(),
gibilisco.gibilisco_9_14(),
gibilisco.gibilisco_9_15(),
gibilisco.gibilisco_9_16(),
gibilisco.gibilisco_9_17(),
gibilisco.gibilisco_9_18(),
gibilisco.gibilisco_9_19(),
gibilisco.gibilisco_9_20(),
gibilisco.gibilisco_10_1(),
gibilisco.gibilisco_10_2(),
gibilisco.gibilisco_10_3(),
gibilisco.gibilisco_10_4(),
gibilisco.gibilisco_10_5(),
gibilisco.gibilisco_10_6(),
gibilisco.gibilisco_10_7(),
gibilisco.gibilisco_10_8(),
gibilisco.gibilisco_10_9(),
gibilisco.gibilisco_10_10(),
gibilisco.gibilisco_10_11(),
gibilisco.gibilisco_10_12(),
gibilisco.gibilisco_10_13(),
gibilisco.gibilisco_10_14(),
gibilisco.gibilisco_10_15(),
gibilisco.gibilisco_10_16(),
gibilisco.gibilisco_10_17(),
gibilisco.gibilisco_10_18(),
gibilisco.gibilisco_10_19(),
gibilisco.gibilisco_10_20(),
gibilisco.gibilisco_11_1(),
gibilisco.gibilisco_11_2(),
gibilisco.gibilisco_11_3(),
gibilisco.gibilisco_11_4(),
gibilisco.gibilisco_11_5(),
gibilisco.gibilisco_11_6(),
gibilisco.gibilisco_11_7(),
gibilisco.gibilisco_11_8(),
gibilisco.gibilisco_11_9(),
gibilisco.gibilisco_11_10(),
gibilisco.gibilisco_11_11(),
gibilisco.gibilisco_11_12(),
gibilisco.gibilisco_11_13(),
gibilisco.gibilisco_11_14(),
gibilisco.gibilisco_11_15(),
gibilisco.gibilisco_11_16(),
gibilisco.gibilisco_11_17(),
gibilisco.gibilisco_11_18(),
gibilisco.gibilisco_11_19(),
gibilisco.gibilisco_11_20(),
gibilisco.gibilisco_12_1(),
gibilisco.gibilisco_12_2(),
gibilisco.gibilisco_12_3(),
gibilisco.gibilisco_12_4(),
gibilisco.gibilisco_12_5(),
gibilisco.gibilisco_12_6(),
gibilisco.gibilisco_12_7(),
gibilisco.gibilisco_12_8(),
gibilisco.gibilisco_12_9(),
gibilisco.gibilisco_12_10(),
gibilisco.gibilisco_12_11(),
gibilisco.gibilisco_12_12(),
gibilisco.gibilisco_12_13(),
gibilisco.gibilisco_12_14(),
gibilisco.gibilisco_12_15(),
gibilisco.gibilisco_12_16(),
gibilisco.gibilisco_12_17(),
gibilisco.gibilisco_12_18(),
gibilisco.gibilisco_12_19(),
gibilisco.gibilisco_12_20(),
gibilisco.gibilisco_13_1(),
gibilisco.gibilisco_13_2(),
gibilisco.gibilisco_13_3(),
gibilisco.gibilisco_13_4(),
gibilisco.gibilisco_13_5(),
gibilisco.gibilisco_13_6(),
gibilisco.gibilisco_13_7(),
gibilisco.gibilisco_13_8(),
gibilisco.gibilisco_13_9(),
gibilisco.gibilisco_13_10(),
gibilisco.gibilisco_13_11(),
gibilisco.gibilisco_13_12(),
gibilisco.gibilisco_13_13(),
gibilisco.gibilisco_13_14(),
gibilisco.gibilisco_13_15(),
gibilisco.gibilisco_13_16(),
gibilisco.gibilisco_13_17(),
gibilisco.gibilisco_13_18(),
gibilisco.gibilisco_13_19(),
gibilisco.gibilisco_13_20(),
gibilisco.gibilisco_14_1(),
gibilisco.gibilisco_14_2(),
gibilisco.gibilisco_14_3(),
gibilisco.gibilisco_14_4(),
gibilisco.gibilisco_14_5(),
gibilisco.gibilisco_14_6(),
gibilisco.gibilisco_14_7(),
gibilisco.gibilisco_14_8(),
gibilisco.gibilisco_14_9(),
gibilisco.gibilisco_14_10(),
gibilisco.gibilisco_14_11(),
gibilisco.gibilisco_14_12(),
gibilisco.gibilisco_14_13(),
gibilisco.gibilisco_14_14(),
gibilisco.gibilisco_14_15(),
gibilisco.gibilisco_14_16(),
gibilisco.gibilisco_14_17(),
gibilisco.gibilisco_14_18(),
gibilisco.gibilisco_14_19(),
gibilisco.gibilisco_14_20(),
gibilisco.gibilisco_15_1(),
gibilisco.gibilisco_15_2(),
gibilisco.gibilisco_15_3(),
gibilisco.gibilisco_15_4(),
gibilisco.gibilisco_15_5(),
gibilisco.gibilisco_15_6(),
gibilisco.gibilisco_15_7(),
gibilisco.gibilisco_15_8(),
gibilisco.gibilisco_15_9(),
gibilisco.gibilisco_15_10(),
gibilisco.gibilisco_15_11(),
gibilisco.gibilisco_15_12(),
gibilisco.gibilisco_15_13(),
gibilisco.gibilisco_15_14(),
gibilisco.gibilisco_15_15(),
gibilisco.gibilisco_15_16(),
gibilisco.gibilisco_15_17(),
gibilisco.gibilisco_15_18(),
gibilisco.gibilisco_15_19(),
gibilisco.gibilisco_15_20(),
gibilisco.gibilisco_16_1(),
gibilisco.gibilisco_16_2(),
gibilisco.gibilisco_16_3(),
gibilisco.gibilisco_16_4(),
gibilisco.gibilisco_16_5(),
gibilisco.gibilisco_16_6(),
gibilisco.gibilisco_16_7(),
gibilisco.gibilisco_16_8(),
gibilisco.gibilisco_16_9(),
gibilisco.gibilisco_16_10(),
gibilisco.gibilisco_16_11(),
gibilisco.gibilisco_16_12(),
gibilisco.gibilisco_16_13(),
gibilisco.gibilisco_16_14(),
gibilisco.gibilisco_16_15(),
gibilisco.gibilisco_16_16(),
gibilisco.gibilisco_16_17(),
gibilisco.gibilisco_16_18(),
gibilisco.gibilisco_16_19(),
gibilisco.gibilisco_16_20(),
gibilisco.gibilisco_17_1(),
gibilisco.gibilisco_17_2(),
gibilisco.gibilisco_17_3(),
gibilisco.gibilisco_17_4(),
gibilisco.gibilisco_17_5(),
gibilisco.gibilisco_17_6(),
gibilisco.gibilisco_17_7(),
gibilisco.gibilisco_17_8(),
gibilisco.gibilisco_17_9(),
gibilisco.gibilisco_17_10(),
gibilisco.gibilisco_17_11(),
gibilisco.gibilisco_17_12(),
gibilisco.gibilisco_17_13(),
gibilisco.gibilisco_17_14(),
gibilisco.gibilisco_17_15(),
gibilisco.gibilisco_17_16(),
gibilisco.gibilisco_17_17(),
gibilisco.gibilisco_17_18(),
gibilisco.gibilisco_17_19(),
gibilisco.gibilisco_17_20(),
gibilisco.gibilisco_18_1(),
gibilisco.gibilisco_18_2(),
gibilisco.gibilisco_18_3(),
gibilisco.gibilisco_18_4(),
gibilisco.gibilisco_18_5(),
gibilisco.gibilisco_18_6(),
gibilisco.gibilisco_18_7(),
gibilisco.gibilisco_18_8(),
gibilisco.gibilisco_18_9(),
gibilisco.gibilisco_18_10(),
gibilisco.gibilisco_18_11(),
gibilisco.gibilisco_18_12(),
gibilisco.gibilisco_18_13(),
gibilisco.gibilisco_18_14(),
gibilisco.gibilisco_18_15(),
gibilisco.gibilisco_18_16(),
gibilisco.gibilisco_18_17(),
gibilisco.gibilisco_18_18(),
gibilisco.gibilisco_18_19(),
gibilisco.gibilisco_18_20(),
gibilisco.gibilisco_19_1(),
gibilisco.gibilisco_19_2(),
gibilisco.gibilisco_19_3(),
gibilisco.gibilisco_19_4(),
gibilisco.gibilisco_19_5(),
gibilisco.gibilisco_19_6(),
gibilisco.gibilisco_19_7(),
gibilisco.gibilisco_19_8(),
gibilisco.gibilisco_19_9(),
gibilisco.gibilisco_19_10(),
gibilisco.gibilisco_19_11(),
gibilisco.gibilisco_19_12(),
gibilisco.gibilisco_19_13(),
gibilisco.gibilisco_19_14(),
gibilisco.gibilisco_19_15(),
gibilisco.gibilisco_19_16(),
gibilisco.gibilisco_19_17(),
gibilisco.gibilisco_19_18(),
gibilisco.gibilisco_19_19(),
gibilisco.gibilisco_19_20(),
gibilisco.gibilisco_20_1(),
gibilisco.gibilisco_20_2(),
gibilisco.gibilisco_20_3(),
gibilisco.gibilisco_20_4(),
gibilisco.gibilisco_20_5(),
gibilisco.gibilisco_20_6(),
gibilisco.gibilisco_20_7(),
gibilisco.gibilisco_20_8(),
gibilisco.gibilisco_20_9(),
gibilisco.gibilisco_20_10(),
gibilisco.gibilisco_20_11(),
gibilisco.gibilisco_20_12(),
gibilisco.gibilisco_20_13(),
gibilisco.gibilisco_20_14(),
gibilisco.gibilisco_20_15(),
gibilisco.gibilisco_20_16(),
gibilisco.gibilisco_20_17(),
gibilisco.gibilisco_20_18(),
gibilisco.gibilisco_20_19(),
gibilisco.gibilisco_20_20(),
gibilisco.gibilisco_21_1(),
gibilisco.gibilisco_21_2(),
gibilisco.gibilisco_21_3(),
gibilisco.gibilisco_21_4(),
gibilisco.gibilisco_21_5(),
gibilisco.gibilisco_21_6(),
gibilisco.gibilisco_21_7(),
gibilisco.gibilisco_21_8(),
gibilisco.gibilisco_21_9(),
gibilisco.gibilisco_21_10(),
gibilisco.gibilisco_21_11(),
gibilisco.gibilisco_21_12(),
gibilisco.gibilisco_21_13(),
gibilisco.gibilisco_21_14(),
gibilisco.gibilisco_21_15(),
gibilisco.gibilisco_21_16(),
gibilisco.gibilisco_21_17(),
gibilisco.gibilisco_21_18(),
gibilisco.gibilisco_21_19(),
gibilisco.gibilisco_21_20(),
gibilisco.gibilisco_22_1(),
gibilisco.gibilisco_22_2(),
gibilisco.gibilisco_22_3(),
gibilisco.gibilisco_22_4(),
gibilisco.gibilisco_22_5(),
gibilisco.gibilisco_22_6(),
gibilisco.gibilisco_22_7(),
gibilisco.gibilisco_22_8(),
gibilisco.gibilisco_22_9(),
gibilisco.gibilisco_22_10(),
gibilisco.gibilisco_22_11(),
gibilisco.gibilisco_22_12(),
gibilisco.gibilisco_22_13(),
gibilisco.gibilisco_22_14(),
gibilisco.gibilisco_22_15(),
gibilisco.gibilisco_22_16(),
gibilisco.gibilisco_22_17(),
gibilisco.gibilisco_22_18(),
gibilisco.gibilisco_22_19(),
gibilisco.gibilisco_22_20(),
gibilisco.gibilisco_23_1(),
gibilisco.gibilisco_23_2(),
gibilisco.gibilisco_23_3(),
gibilisco.gibilisco_23_4(),
gibilisco.gibilisco_23_5(),
gibilisco.gibilisco_23_6(),
gibilisco.gibilisco_23_7(),
gibilisco.gibilisco_23_8(),
gibilisco.gibilisco_23_9(),
gibilisco.gibilisco_23_10(),
gibilisco.gibilisco_23_11(),
gibilisco.gibilisco_23_12(),
gibilisco.gibilisco_23_13(),
gibilisco.gibilisco_23_14(),
gibilisco.gibilisco_23_15(),
gibilisco.gibilisco_23_16(),
gibilisco.gibilisco_23_17(),
gibilisco.gibilisco_23_18(),
gibilisco.gibilisco_23_19(),
gibilisco.gibilisco_23_20(),
gibilisco.gibilisco_24_1(),
gibilisco.gibilisco_24_2(),
gibilisco.gibilisco_24_3(),
gibilisco.gibilisco_24_4(),
gibilisco.gibilisco_24_5(),
gibilisco.gibilisco_24_6(),
gibilisco.gibilisco_24_7(),
gibilisco.gibilisco_24_8(),
gibilisco.gibilisco_24_9(),
gibilisco.gibilisco_24_10(),
gibilisco.gibilisco_24_11(),
gibilisco.gibilisco_24_12(),
gibilisco.gibilisco_24_13(),
gibilisco.gibilisco_24_14(),
gibilisco.gibilisco_24_15(),
gibilisco.gibilisco_24_16(),
gibilisco.gibilisco_24_17(),
gibilisco.gibilisco_24_18(),
gibilisco.gibilisco_24_19(),
gibilisco.gibilisco_24_20(),
gibilisco.gibilisco_25_1(),
gibilisco.gibilisco_25_2(),
gibilisco.gibilisco_25_3(),
gibilisco.gibilisco_25_4(),
gibilisco.gibilisco_25_5(),
gibilisco.gibilisco_25_6(),
gibilisco.gibilisco_25_7(),
gibilisco.gibilisco_25_8(),
gibilisco.gibilisco_25_9(),
gibilisco.gibilisco_25_10(),
gibilisco.gibilisco_25_11(),
gibilisco.gibilisco_25_12(),
gibilisco.gibilisco_25_13(),
gibilisco.gibilisco_25_14(),
gibilisco.gibilisco_25_15(),
gibilisco.gibilisco_25_16(),
gibilisco.gibilisco_25_17(),
gibilisco.gibilisco_25_18(),
gibilisco.gibilisco_25_19(),
gibilisco.gibilisco_25_20()
)



#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(0.25 * len(questionList)))


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
