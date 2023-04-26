#mass = ['python','rubi','javascript','javacore']
#mass = ['minsk','moscow','washington']
mass = ["hello", "world", "python"]



def fff(mass_of_strs):
	chars_we_have = []

	result_mass = []

	for x in mass_of_strs:
		result_str = ''
		char_str = list(x)
		
		for i in char_str:
			if x.count(i) == 1 and i not in chars_we_have:
				result_str +=i
				chars_we_have.append(i)

		result_mass.append(result_str)
	return result_mass
	



print(f'Входной список: {mass}\n\nВыходной список: {fff(mass)}\n\n')


