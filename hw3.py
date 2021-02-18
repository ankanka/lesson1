

for number in range(10):
	print(number + 1)
print('----')

name = input("Как тебя зовут? ")

for letters in name:
	print(letters)
print('----')


student_scores = [
	{'school_class': '4a', 'scores': [1,5,5,3,4]}, 
	{'school_class': '4b', 'scores': [5,5,5,3,4]},
	{'school_class': '4c', 'scores': [4,5,5,3,4]},
	{'school_class': '4d', 'scores': [4,2,3,4,5]}
	]

class_len = 0
class_sum = 0
for school in student_scores:
	class_sum += sum(school['scores'])
	class_len += len(school['scores'])


avg_scores_school = class_sum / class_len 
print(f'Среднее по школе: {avg_scores_school}')

for school in student_scores:
	class_sum1 = sum(school['scores'])
	avg = class_sum1 / len(school['scores'])
	class_name = school['school_class']
	print(f'Среднее в классе {class_name}: {avg}')

