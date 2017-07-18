# Building a XML diff

import xml.etree.ElementTree as ET
from xml.dom import minidom

file_1 = 'staff.xml'
file_2 = 'staff2.xml'


def get_tree(_file):
    tree = ET.parse(_file)

    return tree


def get_root(tree):
    root = tree.getroot()
    return root


def totally_num_of_nodes(root):
    result = len(root.getchildren())
    return result


def iterate_file(root):
    _list = []
    for i in range(0, totally_num_of_nodes(root)):
        for j in range(0, 100):
            try:
                _list.append(root[i][j].text)
            except IndexError:
                pass

    return _list


def diff(list_a, list_b):
    print (list(set(list_a).symmetric_difference(list_b)))


def main():
    tree_1 = get_tree(file_1)
    tree_2 = get_tree(file_2)

    root_1 = get_root(tree_1)
    root_2 = get_root(tree_2)

    list_1 = iterate_file(root_1)
    list_2 = iterate_file(root_2)

    diff_list = diff(list_1, list_2)

if __name__ == '__main__':
    main()
