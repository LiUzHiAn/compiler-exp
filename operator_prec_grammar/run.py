class Grammar(object):
    """
        根据算符优先文法求FIRSTVT()和LASTVT()集合
        @author:Liu Zhian
        @time:2018.12.11
        约定：产生式中，以“->”隔开左右两侧
            默认非终结符为大写字母A-Z，其他全为小写字母
    """

    def __init__(self, filename):
        self.productions = {}
        self.productions_num = 0
        # 终结符集合
        self.terminals = set({})
        # 非终结符集合
        self.unterminals = set({})

        self.init_grammar_from_file(filename)

    def init_grammar_from_file(self, filename):
        with open(filename) as f:
            productions = f.readlines()
        # 去掉换行符
        productions = [p.rstrip("\n") for p in productions]

        for p in productions:
            production = {}
            # 根据“->”分割一条产生式的左右两端
            a = p.split("->")
            production["left"] = a[0]
            production["right"] = a[1]
            self.productions_num += 1
            self.productions[self.productions_num] = production
            # 将产生式左边符号添加到非终结符集合中
            if a[0] not in self.unterminals:
                self.unterminals.add(a[0])
            # 将产生式右边的非终结符添加到非终结符集合中
            for ch in a[1]:
                if (not 'A' <= ch <= 'Z') and (ch not in self.terminals):
                    self.terminals.add(ch)

    def show_info(self):
        print("所有产生式：", self.productions)
        print("所有终结符：", self.terminals)
        print("所有非终结符：", self.unterminals)

    def generate_firstvt(self):
        firstvt = {}
        # 先全初始化为空
        for ch in self.unterminals:
            firstvt[ch] = set({})

        # 第一遍先扫描形如A->a...或A->Ba...的产生式
        for p_i in range(1, self.productions_num + 1):
            # A->a...形式
            if self.productions[p_i]["right"][0] in self.terminals:
                firstvt[self.productions[p_i]["left"]].add(self.productions[p_i]["right"][0])

            # A->Ba...形式
            elif len(self.productions[p_i]["right"]) >= 2 \
                    and self.productions[p_i]["right"][0] in self.unterminals \
                    and self.productions[p_i]["right"][1] in self.terminals:
                firstvt[self.productions[p_i]["left"]].add(self.productions[p_i]["right"][1])

        # 第二遍再扫描形如A->B.. , B->b...或B->Cb...的产生式
        # 这样只要将firstvt(B)加入到firstvt(A)中
        # 如出现E->T , T->F , F->P这样的情况，那么执行的顺序不同可能会产生不同的结果
        # 因此采用一个栈来完成
        stack = []
        # 将当前所有非终结符的firstvt入栈
        for key in firstvt.keys():
            for item in firstvt[key]:
                stack.append((key, item))

        while len(stack) > 0:
            # 弹出当前栈顶，二元组为 ==>（终结符，终结符firstvt中的一个）
            key, item = stack.pop()
            for p_i in range(1, self.productions_num + 1):
                # 如果存在A->B..，并且firstvt(B)又求出来了的情况
                if self.productions[p_i]["right"][0] == key \
                        and self.productions[p_i]["left"] != key \
                        and item not in firstvt[self.productions[p_i]["left"]]:
                    firstvt[self.productions[p_i]["left"]].add(item)
                    stack.append((self.productions[p_i]["left"], item))

        return firstvt

    def generate_lastvt(self):
        lastvt = {}
        # 先全初始化为空
        for ch in self.unterminals:
            lastvt[ch] = set({})

        # 第一遍先扫描形如A->...a或A->...aB的产生式
        for p_i in range(1, self.productions_num + 1):
            # A->...a形式
            if self.productions[p_i]["right"][-1] in self.terminals:
                lastvt[self.productions[p_i]["left"]].add(self.productions[p_i]["right"][-1])

            # A->...aB形式
            elif len(self.productions[p_i]["right"]) >= 2 \
                    and self.productions[p_i]["right"][-1] in self.unterminals \
                    and self.productions[p_i]["right"][-2] in self.terminals:
                lastvt[self.productions[p_i]["left"]].add(self.productions[p_i]["right"][-2])

        # 第二遍再扫描形如A->...B , B->...b或B->...bC的产生式
        # 这样只要将lastvt(B)加入到lastvt(A)中
        # 如出现E->T , T->F , F->P这样的情况，那么执行的顺序不同可能会产生不同的结果
        # 因此采用一个栈来完成
        stack = []
        # 将当前所有非终结符的lastvt入栈
        for key in lastvt.keys():
            for item in lastvt[key]:
                stack.append((key, item))

        while len(stack) > 0:
            # 弹出当前栈顶，二元组为 ==>（终结符，终结符lastvt中的一个）
            key, item = stack.pop()
            for p_i in range(1, self.productions_num + 1):
                # 如果存在A->...B 并且lastvt(B)又求出来了的情况
                if self.productions[p_i]["right"][0] == key \
                        and self.productions[p_i]["left"] != key \
                        and item not in lastvt[self.productions[p_i]["left"]]:
                    lastvt[self.productions[p_i]["left"]].add(item)
                    stack.append((self.productions[p_i]["left"], item))

        return lastvt

    def save_priority_to_file(self, filename, firstvt, lastvt):
        """
        将firstvt和lastv集合保存到文件
        :param filename:
        :param firstvt: dict类型
        :param lastvt: dict类型
        :return:
        """
        with open(filename, "w") as f:
            f.write("firstvt集合如下:")
            for key, value in firstvt.items():
                f.write("\n" + key + ":")
                # 去掉单引号
                f.write("[" + ",".join(value) + "]")


            f.write("\nlastvt集合如下:")
            for key, value in lastvt.items():
                f.write("\n" + key + ":")
                f.write("[" + ",".join(value) + "]")


if __name__ == '__main__':
    grammar = Grammar("grammar.txt")

    # print("该算符优先文法的信息如下：")
    # grammar.show_info()

    print("所有非终结符的firstvt()集合如下：")
    firstvt = grammar.generate_firstvt()
    [print(item) for item in firstvt.items()]

    print("所有非终结符的lastvt()集合如下：")
    lastvt = grammar.generate_lastvt()
    [print(item) for item in lastvt.items()]

    grammar.save_priority_to_file("result.txt", firstvt, lastvt)

