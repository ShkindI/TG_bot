import random

# mass = [500,1300,1800,4000,7000,16000,25000]
mass = []


for x in range(0,97):#Тут задается количество чисeл в списке, можно указать чет\нечет
	mass.append(random.randint(1,20))


mass = sorted(mass)


def mediana(mass_of_counts):
	if len(mass_of_counts)%2 == 0:
		index1 = int(len(mass_of_counts)/2)
		index2 = index1 - 1
		mediana = (mass_of_counts[index1] + mass_of_counts[index2])/2
		return mediana
	
	else:
		index = int(len(mass_of_counts)/2)
		mediana = mass_of_counts[index]
		return mediana


fff = mediana(mass)


print(f'Длинна заполненного массива: {len(mass)}')
print(f'Сам массив: {mass}')
print(f'Медиана чисел: {fff}')



