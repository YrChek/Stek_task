this_list = ['}{}', '{{[(])]}}', '[[{())}]', '{{[()]}}',
             '[([])((([[[]]])))]{()}', '(((([{}]))))']


class Stack:
    def __init__(self, my_string):
        self.my_string = my_string
        self.stek_list = []
        self.symbol_library = {'(': ')',
                               '[': ']',
                               '{': '}'}

    def isEmpty(self):
        if len(self.stek_list) != 0:
            return True
        else:
            return False

    def push(self, data):
        self.stek_list.insert(0, data)

    def pop(self):
        element = self.stek_list[0]
        self.stek_list.pop(0)
        return element

    def peek(self):
        element = self.stek_list[0]
        return element

    def size(self):
        len_array = len(self.stek_list)
        return len_array

    def checking_balance(self):
        if self.size() % 2 != 0:
            return 'Несбалансированно'
        for i in range(len(self.my_string)):
            el = self.my_string[i]
            if el in self.symbol_library:
                self.push(self.symbol_library[el])
            else:
                if el not in self.stek_list:
                    return 'Несбалансированно'
                else:
                    el_stack = self.peek()
                    if el != el_stack:
                        return 'Несбалансированно'
                    else:
                        self.pop()
        if self.isEmpty():
            return 'Несбалансированно'
        else:
            return 'Сбалансированно'


if __name__ == '__main__':
    for string in this_list:
        start = Stack(string)
        res = start.checking_balance()
        print(res)
