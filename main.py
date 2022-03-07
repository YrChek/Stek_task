this_list = ['}{}', '{{[(])]}}', '[[{())}]', '{{[()]}}',
             '[([])((([[[]]])))]{()}', '(((([{}]))))']


class Stek:
    def __init__(self, my_string):
        self.my_string = my_string
        self.stek_list = []
        self.symbol_library = {'(': ')',
                               '[': ']',
                               '{': '}'}

    def isEmpty(self, array):
        if len(array) != 0:
            return True
        else:
            return False

    def push(self, array, data):
        array.insert(0, data)

    def pop(self, array):
        element = array[0]
        if isinstance(array, str):
            self.my_string = self.my_string[1:]
        else:
            self.stek_list.pop(0)
        return element

    def peek(self, array):
        element = array[0]
        return element

    def size(self, array):
        len_array = len(array)
        return len_array

    def checking_balance(self):
        if self.size(self.my_string) % 2 != 0:
            return 'Несбалансированно'
        while self.isEmpty(self.my_string):
            el = self.pop(self.my_string)
            if el in self.symbol_library:
                self.push(self.stek_list, self.symbol_library[el])
            else:
                if el not in self.stek_list:
                    return 'Несбалансированно'
                else:
                    el_stek = self.peek(self.stek_list)
                    if el != el_stek:
                        return 'Несбалансированно'
                    else:
                        self.pop(self.stek_list)
        if self.isEmpty(self.stek_list):
            return 'Несбалансированно'
        else:
            return 'Сбалансированно'


if __name__ == '__main__':
    for string in this_list:
        start = Stek(string)
        res = start.checking_balance()
        print(res)
