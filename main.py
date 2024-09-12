first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
result_1 = [len(elem) for elem in first_strings if len(elem) > 5]
result_2 = [(elem ,elem_2) for elem in first_strings for elem_2 in second_strings if len(elem) == len(elem_2)]
third_strings = first_strings + second_strings
result_3 = {elem: len(elem) for elem in third_strings if len(elem) % 2 == 0}
print(result_1)
print(result_2)
print(result_3)