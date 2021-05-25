#coding:utf-8
import os


class Path2Tree(object):
    def __init__(self, path_list):
        self.path_list = path_list
        self.tree_str = ''
        self.build_tree()

    def get_space(self, tree_list):
        if len(tree_list) < 2:
            return "└─"

        end = tree_list[-1]
        front_list = tree_list[0:-1]
        line = ""
        for flag in front_list:
            line += "|   " if flag else "    "

        line += "└─ " if end else "├─ "
        return line

    def get_new_list(self, tree_list, item):
        ret_list = []
        ret_list.extend(tree_list)
        ret_list.append(item)
        return ret_list

    def generate_tree(self, tree, n=0, tree_list=[]):
        if not isinstance(tree, dict) and not isinstance(tree, list):
            self.tree_str += self.get_space(tree_list) + str(tree) + '\n'
        elif isinstance(tree, list) or isinstance(tree, tuple):
            length = len(tree)
            for index, error in enumerate(tree):
                self.tree_str += self.get_space(self.get_new_list(tree_list, length == index + 1)) + str(tree) + '\n'
        elif isinstance(tree, dict):
            length = len(tree)
            keys = list(tree.keys())
            keys.sort()
            for index, key in enumerate(keys):
                value = tree[key]
                self.tree_str += self.get_space(self.get_new_list(tree_list, length == index + 1)) + str(key) + '\n'
                self.generate_tree(value, n + 1, self.get_new_list(tree_list, length != index + 1))

    def build_tree(self):
        tree_dict = {}
        sub_tree_dict = None
        for path in self.path_list:
            path_sub_list = path.split(os.path.sep)
            for index, sub_key in enumerate(path_sub_list):
                if index == 0:
                    tree_dict[sub_key] = tree_dict.get(sub_key, {})
                    sub_tree_dict = tree_dict[sub_key]
                else:
                    sub_tree_dict[sub_key] = sub_tree_dict.get(sub_key, {})
                    sub_tree_dict = sub_tree_dict[sub_key]

        self.tree_str = ''
        self.generate_tree(tree_dict, 0)

    def get_tree(self):
        return self.tree_str
