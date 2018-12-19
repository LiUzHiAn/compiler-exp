# -*- coding:UTF-8 -*-

"""
    implementation about converting NFA to DFA
    author: ANDY LAU
    time:27/11/2018
    email:andy929910266@gmail.com
"""
from nfa import NFA
from dfa import DFA
from utils import *


def main():
    # nfa_json = generate_nfa()
    # save_nfa_to_file(nfa_json, "nfa_source.json")

    # input_file = input("输入保存nfa的文件：")

    input_file = "nfa.json"
    nfa_json = load_nfa_from_file(input_file)
    nfa = NFA(nfa_json)
    nfa.show_nfa_info()
    print()
    print("...转换中...")

    # print("对初始状态的epsilon_closure结果为：")
    # print(nfa.epsilon_closure(nfa.init_state))
    dfa_json = nfa.convert_to_dfa()
    # output_file = input("输入保存dfa的文件：")
    output_file = "dfa.json"
    save_dfa_to_file(dfa_json, output_file)
    dfa = DFA(dfa_json)
    dfa.show_dfa_info()


# closure = nfa.epsilon_closure(["s9"])
# print(closure)
# new_states = nfa.move({"s0", "s1", "s2", "s4", "s7"}, "a")
# print(new_states)
# print()


if __name__ == '__main__':
    main()
