class Myclass(object):
    def method_1(self, param_tuple):
        self.local_list = []
        for element in param_tuple:
            if element > 10:
                self.local_list.append(element)

    def method_2(self):
        self.int_sum = 0
        for element in self.local_list:
            self.int_sum += element
        return  self.int_sum

inst1 = Myclass()
inst2 = Myclass()
inst1.method_1([1, 2, 3])
print(inst1.local_list)
inst1.method_1([10, 1, 12])
print(inst1.local_list)
print(inst1.method_2())
inst2.method_2()
