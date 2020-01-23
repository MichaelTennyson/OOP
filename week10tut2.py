class Newclass(object):
    def __init__(self, param_int=1):
        self.the_int = param_int
        if param_int%2 == 0:
            self.parity = 'even'
        else:
            self.parity = 'odd'

    def process(self, instance):
        int_sum = self.the_int + instance.the_int
        if int_sum < 0:
            return 'negative'
        elif int_sum%2 == 0:
            return 'even'
        else:
            return 'odd'

    def __str__(self):
        return 'value {} is {}'.format(self.the_int, self.parity)


inst1 = Newclass(4)
inst2 = Newclass(-5)
inst3 = Newclass()
print(inst1)
print(inst1.parity)
print(inst1.process(inst2))
print(inst3.process(inst1))