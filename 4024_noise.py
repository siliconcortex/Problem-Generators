import random
from est import noise as source
from est import indiabix as source2

print('Generating...')
file_name = 'noise'

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


question_list = [source.jma_1_95(),
source.jma_1_98(),
source.jma_1_99_a(),
source.jma_1_99_b(),
source.jma_1_100(),
source.jma_1_102_a(),
source.jma_1_102_b(),
source.jma_1_104(),
source.jma_1_105(),
source.jma_1_108(),
source.jma_1_109_a(),
source.jma_1_109_b(),
source.jma_1_110(),
source.jma_1_112(),
source.jma_1_113(),
]


concept_list = [
#source2.ece_radio_receivers_section_1_0(),
source2.ece_radio_receivers_section_1_1(),
#source2.ece_radio_receivers_section_1_2(),
# source2.ece_radio_receivers_section_1_3(),
# source2.ece_radio_receivers_section_1_4(),
# source2.ece_radio_receivers_section_1_5(),
# source2.ece_radio_receivers_section_1_6(),
# source2.ece_radio_receivers_section_1_7(),
# source2.ece_radio_receivers_section_1_8(),
# source2.ece_radio_receivers_section_1_9(),

# source2.ece_radio_receivers_section_1_10(),
# source2.ece_radio_receivers_section_1_11(),
# source2.ece_radio_receivers_section_1_12(),
# source2.ece_radio_receivers_section_1_13(),
# source2.ece_radio_receivers_section_1_14(),
# source2.ece_radio_receivers_section_1_15(),
# source2.ece_radio_receivers_section_1_16(),
# source2.ece_radio_receivers_section_1_17(),
# source2.ece_radio_receivers_section_1_18(),
# source2.ece_radio_receivers_section_1_19(),

# source2.ece_radio_receivers_section_1_20(),
# source2.ece_radio_receivers_section_1_21(),
# source2.ece_radio_receivers_section_1_22(),
source2.ece_radio_receivers_section_1_23(),
source2.ece_radio_receivers_section_1_24(),
# source2.ece_radio_receivers_section_1_25(),
# source2.ece_radio_receivers_section_1_26(),
# source2.ece_radio_receivers_section_1_27(),
# source2.ece_radio_receivers_section_1_28(),
# source2.ece_radio_receivers_section_1_29(),

# #source2.ece_radio_receivers_section_1_30(),
# source2.ece_radio_receivers_section_1_31(),
# source2.ece_radio_receivers_section_1_32(),
# source2.ece_radio_receivers_section_1_33(),
# source2.ece_radio_receivers_section_1_34(),
# source2.ece_radio_receivers_section_1_35(),
# source2.ece_radio_receivers_section_1_36(),
# source2.ece_radio_receivers_section_1_37(),
source2.ece_radio_receivers_section_1_38(),
source2.ece_radio_receivers_section_1_39(),

# source2.ece_radio_receivers_section_1_40(),
# source2.ece_radio_receivers_section_1_41(),
# source2.ece_radio_receivers_section_1_42(),
# source2.ece_radio_receivers_section_1_43(),
# source2.ece_radio_receivers_section_1_44(),
# source2.ece_radio_receivers_section_1_45(),
# source2.ece_radio_receivers_section_1_46(),
# source2.ece_radio_receivers_section_1_47(),
# source2.ece_radio_receivers_section_1_48(),
source2.ece_radio_receivers_section_1_49(),

source2.ece_radio_receivers_section_1_50(),

#source2.ece_radio_receivers_section_2_0(),
# source2.ece_radio_receivers_section_2_1(),
#source2.ece_radio_receivers_section_2_2(),
# source2.ece_radio_receivers_section_2_3(),
# source2.ece_radio_receivers_section_2_4(),
# source2.ece_radio_receivers_section_2_5(),
# source2.ece_radio_receivers_section_2_6(),
# source2.ece_radio_receivers_section_2_7(),
# source2.ece_radio_receivers_section_2_8(),
source2.ece_radio_receivers_section_2_9(),

# source2.ece_radio_receivers_section_2_10(),
# source2.ece_radio_receivers_section_2_11(),
# source2.ece_radio_receivers_section_2_12(),
# source2.ece_radio_receivers_section_2_13(),
# source2.ece_radio_receivers_section_2_14(),
# source2.ece_radio_receivers_section_2_15(),
# source2.ece_radio_receivers_section_2_16(),
# source2.ece_radio_receivers_section_2_17(),
# source2.ece_radio_receivers_section_2_18(),
# source2.ece_radio_receivers_section_2_19(),

# source2.ece_radio_receivers_section_2_20(),
# source2.ece_radio_receivers_section_2_21(),
# source2.ece_radio_receivers_section_2_22(),
# source2.ece_radio_receivers_section_2_23(),
# source2.ece_radio_receivers_section_2_24(),
# source2.ece_radio_receivers_section_2_25(),
# source2.ece_radio_receivers_section_2_26(),
# source2.ece_radio_receivers_section_2_27(),
source2.ece_radio_receivers_section_2_28(),
# source2.ece_radio_receivers_section_2_29(),

# #source2.ece_radio_receivers_section_2_30(),
# source2.ece_radio_receivers_section_2_31(),
# source2.ece_radio_receivers_section_2_32(),
# source2.ece_radio_receivers_section_2_33(),
# source2.ece_radio_receivers_section_2_34(),
# source2.ece_radio_receivers_section_2_35(),
# source2.ece_radio_receivers_section_2_36(),
# source2.ece_radio_receivers_section_2_37(),
# source2.ece_radio_receivers_section_2_38(),
# source2.ece_radio_receivers_section_2_39(),

# source2.ece_radio_receivers_section_2_40(),
# source2.ece_radio_receivers_section_2_41(),
# source2.ece_radio_receivers_section_2_42(),
# source2.ece_radio_receivers_section_2_43(),
source2.ece_radio_receivers_section_2_44(),
# source2.ece_radio_receivers_section_2_45(),
# source2.ece_radio_receivers_section_2_46(),
# source2.ece_radio_receivers_section_2_47(),
# source2.ece_radio_receivers_section_2_48(),
# source2.ece_radio_receivers_section_2_49(),

source2.ece_radio_receivers_section_2_50()


]

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
