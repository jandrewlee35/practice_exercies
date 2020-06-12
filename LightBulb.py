class LightBulb:
    '''
    Lightbulb class that models lightbulb object
    '''
    def __init__(self, switch = False):
        self.switch = switch

    def toggle(self):
        """
        method that changes state of lightbulb
        :param self: self
        :return: true or flase
        """
        if self.switch == False:
            self.switch = True
        else:
            self.switch = False
        return self.switch

L0 = LightBulb()
print(L0.switch)
L0.toggle()
print(L0.switch)
L0.toggle()
print(L0.switch)