class StringSort:

    def __init__(self, string):
        self.string = string

    def delete(self, delete):
        self.delete = delete
        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if list1[i] == str(self.delete):
                list1[i] = ''
        return ''.join(list1)


string = StringSort('a. b. c. d. e. f.')
print(string.delete('.'))