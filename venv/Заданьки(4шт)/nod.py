import math
n1 = 60

n2 = 24

def find_NOD(num1,num2):
	while num1!=0 and num2!=0:
		if num1>num2:
			num1 = num1%num2
		else:
			num2 = num2%num1
	NOD = num1+num2
	return NOD

	
# response = find_NOD(n1,n2)


print(f'\nВходные числа: {n1},{n2}\n\nНОД этих двух чисел: {find_NOD(n1,n2)}\n\nОтвет математического модуля с теми же входными данными: {math.gcd(n1,n2)}\n\n')


