# Use random module with a seed of 2020 to generate 
# 20 INTs between 100 and 120 (inclusive). 
# #Then write code to calculate the median and mode.  
# The median is the 10th largest number. 
# The mode is the number that occurs the most. 
# If two or more number have the same frequency, list them all

# random module
import random

#2020 seed
random.seed(2020)

#this will be 20 numbers
INT = 20

#create list of 20 INTs between 100 and 120 (inclusive). 
random_number = [random.randrange(100, 121) for _ in range(INT)]
print(f'\nList of random numbers: {random_number}\n')

#Calculate median 
def median_value(values):
    random_number_sorted = sorted(random_number)
    if len(random_number) % 2 == 0:
        median_index1 = int((len(random_number) / 2) - 1) #since index value starts from 0 and not 1
        median_index2 = int(len(random_number) / 2)
        median = (random_number_sorted[median_index1] + random_number_sorted[median_index2]) / 2        
    else: 
        median_index = int((len(random_number) / 2) - 1)
        median = (random_number_sorted[median_index])        
    print(f'The median for the list of random numbers is {median}\n')
    

def mode_value(values):
    mode_dict = {}
    for i in values:
        mode_dict[i] = mode_dict.get(i, 0) + 1
    mode_numbers = 0
    for _ , frequency in mode_dict.items():
        if frequency > mode_numbers:
            mode_numbers = frequency            
        else: pass
    
    print('This is the mode for the numbers with the frequency: ')
    print(f'{"Number":>5} {"Frequency":>10}')
    for key, value in mode_dict.items():
        if value == mode_numbers:
            print(f'{key:>5} {value:>8}')
    
median_value(random_number)

mode_value(random_number)

