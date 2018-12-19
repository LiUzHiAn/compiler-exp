# -*- coding:UTF-8 -*-
import json


def generate_nfa():
    """
    a NFA with following 5 elements:
        1. all_states
        2. init_state
        3. final_state
        4. alphabet
        5. transform_rules
    :return: the NFA with json format
    """
    # 一个五元组NFA表示为含有五个key的字典
    nfa = {}
    alphabet = ["a", "b"]
    all_states = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10"]
    nfa["states"] = all_states
    nfa["alphabet"] = alphabet
    nfa["init_state"] = "s0"
    nfa["final_state"] = "s10"
    transform_rules = dict()

    # for i in range(len(all_states)):
    # transform_rules[all_states[i]] = {}

    # 每个状态对应额转化函数
    rules_0 = dict()
    rules_0["epsilon"] = ["s1", "s7"]
    transform_rules["s0"] = rules_0

    rules_1 = dict()
    rules_1["epsilon"] = ["s2", "s4"]
    transform_rules["s1"] = rules_1

    rules_2 = dict()
    rules_2["a"] = ["s3"]
    transform_rules["s2"] = rules_2

    rules_3 = dict()
    rules_3["epsilon"] = ["s6"]
    transform_rules["s3"] = rules_3

    rules_4 = dict()
    rules_4["b"] = ["s5"]
    transform_rules["s4"] = rules_4

    rules_5 = dict()
    rules_5["epsilon"] = ["s6"]
    transform_rules["s5"] = rules_5

    rules_6 = dict()
    rules_6["epsilon"] = ["s1", "s7"]
    transform_rules["s6"] = rules_6

    rules_7 = dict()
    rules_7["a"] = ["s8"]
    transform_rules["s7"] = rules_7

    rules_8 = dict()
    rules_8["b"] = ["s9"]
    transform_rules["s8"] = rules_8

    rules_9 = dict()
    rules_9["b"] = ["s10"]
    transform_rules["s9"] = rules_9

    rules_10 = dict()
    transform_rules["s10"] = rules_10

    nfa["transform_rules"] = transform_rules

    return nfa


def save_dfa_to_file(dfa, file_name):
    try:
        with open(file_name, "w") as f:
            json.dump(dfa, f)
    except IOError:
        print("写入文件时失败,请重试!")
    else:
        print("保存DFA到json文件成功！")


def load_dfa_from_file(file_name):
    dfa_json = None
    try:
        with open(file_name, "w") as f:
            dfa_json = json.load(f)
    except IOError:
        print("文件不存在或读取文件失败,请重试")
    return dfa_json


def save_nfa_to_file(nfa, file_name):
    try:
        with open(file_name, "w") as f:
            json.dump(nfa, f)
    except IOError:
        print("写入文件时失败,请重试!")
    else:
        print("保存NFA到json文件成功！")


def load_nfa_from_file(file_name):
    nfa_json = None
    try:
        with open(file_name, "r") as f:
            nfa_json = json.load(f)
    except IOError:
        print("文件不存在或读取文件失败,请重试")
    return nfa_json
