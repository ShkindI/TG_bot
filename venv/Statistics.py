from Storage import stat_dict

# stat_dict['Roll'].append(1)
# stat_dict['Roll'].append(2)
# stat_dict['Roll'].append(3)
# stat_dict['Roll'].append(3)
# stat_dict['Roll'].append(3)
# stat_dict['Sup'].append(4)
# stat_dict['Sup'].append(5)
# stat_dict['Sup'].append(5)
# stat_dict['Sup'].append(5)
# stat_dict['Sup'].append(6)
# stat_dict['Hot'].append(7)
# stat_dict['Hot'].append(8)
# stat_dict['Hot'].append(8)
# stat_dict['Hot'].append(8)
# stat_dict['Hot'].append(9)
def stat(idx, Roll=False, Sup=False, Hot=False):
    if Roll == True:
        stat_dict['Roll'].append(idx)
    elif Sup == True:
        stat_dict['Sup'].append(idx)
    elif Hot == True:
        stat_dict['Hot'].append(idx)



def return_stat(unic=False):
    res_str = ''
    if unic == False:
        for k,v in stat_dict.items():
            if k == 'Roll':
                res_str+=f'Кол-во просмотров категории Роллы: {len(v)}\n\n'
            if k == 'Sup':
                res_str += f'Кол-во просмотров категории Супы: {len(v)}\n\n'
            if k == 'Hot':
                res_str += f'Кол-во просмотров категории Горячее: {len(v)}\n\n'
        return res_str
    else:
        for k,v in stat_dict.items():
            if k == 'Roll':
                res_str+=f'Кол-во просмотров категории Роллы: {len(set(v))}\n\n'
            if k == 'Sup':
                res_str += f'Кол-во просмотров категории Супы: {len(set(v))}\n\n'
            if k == 'Hot':
                res_str += f'Кол-во просмотров категории Горячее: {len(set(v))}\n\n'
        return res_str






