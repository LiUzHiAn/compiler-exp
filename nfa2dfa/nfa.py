# -*- coding:UTF-8 -*-
"""
    DFA definition module and implementation about converting NFA to DFA
    author: ANDY LIU
    time:27/11/2018
    email:andy929910266@gmail.com
"""


# -*- coding:UTF-8 -*-

class NFA(object):

    def __init__(self, json_nfa):
        """
        init a NFA by json format NFA
        the difference is that:
        :param json_nfa: a json format NFA
        :return:
        """
        self.states = (json_nfa["states"])
        self.alphabet = (json_nfa["alphabet"])
        self.init_state = json_nfa["init_state"]
        self.final_state = json_nfa["final_state"]
        self.transform_rules = json_nfa["transform_rules"]
        # # 将json格式的NFA中的转化规则由list转化为set
        # for state, rules in self.transform_rules.items():
        #     for inner_key, inner_value in rules.items():
        #         self.transform_rules[state][inner_key] = set(inner_value)

    def __str__(self):
        return str(self)

    def show_nfa_info(self):
        print("所有状态:", self.states)
        print("字母表:", self.alphabet)
        print("初始状态:", self.init_state)
        print("终止状态:", self.final_state)
        print("状态转移规则:", self.transform_rules)

    def epsilon_closure(self, states):
        """
        求某个状态集的epsilon闭包
        :param states: 输入状态集(支持list和set两种方式输入)
        :return: epsilon闭包后的状态集合,set类型
        """

        # 状态是字符串，将其包装成list（初始状态就是一个字符串）
        if type(states) == str:
            states = [states]

        closure_dict = dict()
        for state in states:
            # 对某个状态已经做闭包操作的标志位
            closure_dict[state] = False
        return self.epsilon_closure_exe(closure_dict)

    def epsilon_closure_exe(self, closure_dict):
        """
        供epsilon_closure()函数调用
        :param closure_dict: 求闭包时带有标志位的字典
        :return: epsilon闭包后的状态集合,set类型
        """
        for state in list(closure_dict.keys()):
            # 存在通过epsilon到达的状态 && 当前状态没有执行过epsilon操作
            if "epsilon" in self.transform_rules[state].keys() \
                    and closure_dict[state] == False:
                # 将epsilon弧尾的所有新状态加入集合
                for new_state in self.transform_rules[state]["epsilon"]:
                    closure_dict[new_state] = False
                # 并设置当前状态标志位为false
                closure_dict[state] = True

                # 对加入新状态后的集合再求epsilon闭包
                self.epsilon_closure_exe(closure_dict)

        # 如果没有一个状态可以通过epsilon到另一个状态,就返回
        return set(closure_dict.keys())

    def move(self, states, ch):
        """
        某个状态集通过ch字符到达的状态集合
        :param states: 输入状态集(支持list和set两种方式输入)
        :return: 新状态集合 (set类型)
        """
        new_states = []
        for state in list(states):
            # 如果某个状态可以通过ch到达另一个状态：
            if ch in self.transform_rules[state].keys():
                for new_state in self.transform_rules[state][ch]:
                    new_states.append(new_state)

        return set(new_states)

    def generate_subsets(self):
        """
        将NFA转化为DFA过程中的子集构造算法
        :return:返回生成的状态子集集合、状态子集集合之间的转换关系
        """
        # 由NFA可构造出的所有子集
        subsets = {}
        # 每个子集都存在一个标志位
        flags = {}
        # 各状态子集之间的转化关系
        relations = {}

        # 状态子集索引
        index = 0

        subsets[index] = self.epsilon_closure(self.init_state)
        flags[index] = False

        while True:
            indices = list(subsets.keys())
            subsets_num_before_move = len(indices)
            # 如果还存在没用move函数转换的子集
            for i in indices:
                if flags[i] == False:
                    # 把选中用来move的状态集标志位置为True
                    flags[i] = True
                    # 构造两个状态之间的转换关系
                    relations[i] = {}

                    # 对每个字母表里的字母进行状态转换
                    for ch in self.alphabet:
                        new_states = self.epsilon_closure(self.move(subsets[i], ch))

                        # 如果转换后的新状态集已经在subsets里面不存在,才添加,并添加转换关系
                        if new_states not in subsets.values():
                            index += 1
                            subsets[index] = new_states
                            # 并将新状态的标记为设置为False
                            flags[index] = False
                            relations[i][ch] = index
                        # 如果转换后的状态集已经在subsets中存在，不添加集合,但添加转换关系
                        else:
                            # 字典中根据value获得key （因为是一一对应的关系）
                            relations[i][ch] = list(subsets.keys())[list(subsets.values()).index(new_states)]

            # 把indices更新（因为添加了新的子集）
            indices = list(subsets.keys())
            subsets_num_after_move = len(indices)
            if subsets_num_before_move == subsets_num_after_move:
                break

        return subsets, relations

    def convert_to_dfa(self):
        """
        根据状态子集集合和它们之间的转换规则生成dfa（JSON格式）
        :return: dfa_json格式
        """
        subsets, relations = self.generate_subsets()
        dfa = {}  # json格式
        all_states = []
        for i in list(subsets.keys()):
            # 如果得到的状态子集包含NFA的开始状态，则该状态为DFA的初始状态
            if self.init_state in subsets[i]:
                all_states.append("s{}".format(i))
                dfa["init_state"] = "s{}".format(i)
            elif self.final_state in subsets[i]:
                # 如果得到的状态子集包含NFA的末了状态，则该状态为DFA的末了状态
                all_states.append("s{}".format(i))
                dfa["final_state"] = "s{}".format(i)
            else:
                # 其他状态子集各自生成一个新状态
                all_states.append("s{}".format(i))

        dfa["states"] = all_states
        # 字母表和NFA保持一致
        dfa["alphabet"] = self.alphabet

        transform_rules = dict()

        for i in list(relations.keys()):
            rules = {}
            for key, value in relations[i].items():
                # 请注意，这里其实不必要是列表
                # 根据DFA的特性，每一个状态转换后必定只是另一个状态而不多个
                # 否则也就违反了DFA的定义，它就成NFA了

                # 不过我还是保留列表的形式，目的是为了使得NFA和DFA保存为.json文件时格式一致，方便读取
                rules[key] = ["s{}".format(value)]

            transform_rules["s{}".format(i)] = rules

        dfa["transform_rules"] = transform_rules

        return dfa
