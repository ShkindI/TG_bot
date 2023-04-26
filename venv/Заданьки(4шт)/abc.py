s = 'qwerty'
#s = 'abc'

def qwerty(string):
	result = []
	string = list(string)

	
	for x in string:
		index = string.index(x)

		res_str = ''
		res_str +=x
		result.append(res_str)
		index +=1

		for y in range(index,len(string)):
			i = string[index]
			res_str+=i
			result.append(res_str)
			index +=1
	return result
		

# response = qwerty(s)


print(f'Входная строка: {s}\n\nВариант на выходе: {qwerty(s)}\n\n ')


#"a", "ab", "abc", "b", "bc", "c"