mu_dict = {'Aleks' : 1974 ,'Erik' : 2012 , 'Diana' : 1979 }
print(mu_dict)
print(mu_dict['Aleks'])
print(mu_dict.get('Luntik'))
mu_dict.update({'Luntik' : 2022 , 'Trufel' : 2023 , 'Kiril' : 2000})
print(mu_dict)
del mu_dict['Kiril']
print(mu_dict)
my_set = {1,2,3,4,3,2,1,'Step', True, (1,2,3)}
print(my_set)
print(my_set.add(8))
print(my_set.add(369))
print(my_set)
print(my_set.discard(2))
print(my_set)