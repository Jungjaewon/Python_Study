from builtins import print
"""
Ref 1 : https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3
Ref 2 : https://www.python-course.eu/python3_dictionaries.php
Ref 3 : 

zip -> iterator
"""

def dict_counting(input_list):
    print('-' * 5 + 'dict_counting' + '-' * 5)
    print('input_list : ',input_list)
    count_dict = dict()
    """
    :param input_list: input_list
    :return: dict {value : #of the value}
    """
    for item in input_list:
        if item in count_dict:
            count_dict[item] = count_dict.get(item) + 1
        else:
            count_dict[item] = count_dict.get(item, 0)

    print('count_list : ',count_dict)
    return count_dict


def dict_reverse(input_dict):
    print('-' * 5 + 'dict_reverse' + '-' * 5)
    print('intput_dict : ', input_dict)
    reverse_dict = dict()
    """
    For {input_dict[key] : key for key in input_dict}
    {k: v for k, v in indict.items() } is used for reversing
    {input_dict[key] : key for key in input_dict if key % 2 == 0}
    if statement can be added
    
    :param input_dict: input_dict
    :return: reversed dict
    """
    for key in input_dict:
        reverse_dict[input_dict[key]] = key
    print('{input_dict[key] : key for key in input_dict}', {input_dict[key] : key for key in input_dict})
    print('reverse_dict : ', reverse_dict)
    return reverse_dict


def dict_type(input_dict):
    print('-' * 5 + 'dict_type' + '-' * 5 )
    print('intput_dict : ', input_dict)
    print('type(input_dict.items()) : ', type(input_dict.items()))
    print('type(input_dict.keys()) : ', type(input_dict.keys()))
    print('type(input_dict.values()) : ', type(input_dict.values()))
    """
    keys,items, values are not list dict_keys, items, values etc
    they can not be indexed.
    """

def common_key():
    print('-' * 5 + 'common_key' + '-' * 5)
    sammy = {'username': 'sammy-shark', 'online': True, 'followers': 987}
    jesse = {'username': 'JOctopus', 'online': False, 'points': 723}
    print('sammy.keys() & jesse.keys() : ',sammy.keys() & jesse.keys())

    for common_key in sammy.keys() & jesse.keys():
        print(sammy[common_key], jesse[common_key])

def dict_update():
    """
    :param input_dict:
    :return: updated_dict
    """
    print('-' * 5 + 'dict_update' + '-' * 5)
    input_dict = {'username': 'JOctopus', 'online': False, 'points': 723}
    print('input_dict : ',input_dict)
    input_dict.update({'followers': 481})
    print("input_dict.update({'followers': 481})")
    # input_dict['followers'] = 481 # the same as above line
    input_dict.update({'online': True})
    print("input_dict.update({'online': True})")
    # input_dict ['online'] = True # the same as above line
    print('updated dict : ',input_dict)

def dict_del():
    print('-' * 5 + 'dict_del' + '-' * 5)
    input_dict = {'username': 'JOctopus', 'online': False, 'points': 723}
    print('input_dict : ', input_dict)
    print("del input_dict['online']")
    del input_dict['online']
    # input_dict.pop('online')
    print('input_dict : ', input_dict)
    print('input_dict.clear()')
    input_dict.clear()
    print('input_dict : ', input_dict)
    print('del input_dict This statement makes NameError when refering to input_dict again')
    del input_dict

def dict_zippng():
    dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    countries = ["Italy", "Germany", "Spain", "USA"]
    print('-' * 5 + 'dict_zippng' + '-' * 5)
    print('dishes : ', dishes)
    print('countries : ', countries)
    print('zip(countries, dishes) : ', zip(countries, dishes))
    print('type(zip(countries, dishes)) : ', zip(countries, dishes))
    print('zip(countries, dishes) : ', dict(zip(countries, dishes)))

def dict_mergin():
    knowledge = {"Frank": {"Perl"}, "Monica": {"C", "C++"}}
    knowledge2 = {"Guido": {"Python"}, "Frank": {"Perl", "Python"}}
    print('-' * 5 + 'dict_mergin' + '-' * 5)
    print('knowledge.update(knowledge2) : ', knowledge.update(knowledge2))


def danger_lurking():
    print('-' * 5 + 'danger_lurking' + '-' * 5)
    l1 = ["a", "b", "c"]
    l2 = [1, 2, 3]
    c = zip(l1, l2)

    for i in c:
        print(i)

    for i in c: # This for statement dose not make print because c is a generator!!.
        print(i)
    c = zip(l1, l2)
    z1 = list(c)
    z2 = list(c)
    print('z1 : ', z1)
    print('z2 : ', z2, ' c is a generator') # c is a generator

    dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    countries = ["Italy", "Germany", "Spain", "USA"]
    print('dishes = ["pizza", "sauerkraut", "paella", "hamburger"]')
    print('countries = ["Italy", "Germany", "Spain", "USA"]')
    country_specialities_zip = zip(dishes, countries)
    print(list(country_specialities_zip))
    country_specialities_list = list(country_specialities_zip)
    country_specialities_dict = dict(country_specialities_list)
    print(country_specialities_dict) # because country_specialities_zip is a generator
    # Then statement order is important!


if __name__ == '__main__':
    input_dict = {1:'a', 2 :'b'}
    input_list = ['Person', 'Baseball','Happy','Happy','Person','Person']

    dict_counting(input_list)
    dict_reverse(input_dict)
    dict_type(input_dict)
    common_key()
    dict_update()
    dict_del()
    dict_zippng()
    dict_mergin()
    danger_lurking()


