# -*- coding:UTF-8 -*-
"""
    DFA definition module
    author: ANDY LIU
    time:27/11/2018
    email:andy929910266@gmail.com
"""

import json


class DFA(object):

    def __init__(self, json_dfa):
        """
        init a DFA by json format DFA
        the difference is that:
        :param json_dfa : a json format DFA
        :return:
        """
        self.states = (json_dfa["states"])
        self.alphabet = (json_dfa["alphabet"])
        self.init_state = json_dfa["init_state"]
        self.final_state = json_dfa["final_state"]
        self.transform_rules = json_dfa["transform_rules"]

    def __str__(self):
        return str(self)

    def show_dfa_info(self):
        print("所有状态:", self.states)
        print("字母表:", self.alphabet)
        print("初始状态:", self.init_state)
        print("终止状态:", self.final_state)
        print("状态转移规则:", self.transform_rules)
