# Ref 1 : https://dololak.tistory.com/253

import xml.etree.ElementTree as elemTree

"""
This example is a basic final example for XML.

"""
if __name__ == '__main__':
    print('-' * 5 + 'XML_example' + '-' * 5)
    tree = elemTree.parse('./xml_example.xml')

    xmlStr = '''
                <users>
                        <user grade="gold">
                            <name>Kim Cheol Soo</name>
                            <age>25</age>
                            <birthday>19940215</birthday>
                        </user>
                        <user grade="diamond">
                            <name>Kim Yoo Mee</name>
                            <age>21</age>
                            <birthday>19980417</birthday>
                        </user>
                </users>
            '''

    tree1 = elemTree.fromstring(xmlStr)

    user = tree.find('./user')  # 첫번째 user를 검색한 후 마침

    print(user.tag)  # tag name -> user
    print(user.attrib)  # {'grade' : 'gold'}
    print(user.get('grade'))  # attr value -> gold

    userName = user.find('name')  # <name></name> tag
    print(userName.text)  # Kim Cheol Soo

    user = tree.find('./user[2]')  # 두 번째 user

    tree.find('./user[@grade]')  # grade attrib을 가진 첫 번째 user
    tree.find('./user[@grade][2]')  # grade attrib을 가진 두 번째 user

    for user in tree.findall('./user'):
        print('user.tag : ', user.tag)


