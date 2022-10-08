class Terminal:
    def _check_card(self,card):
        if len(card)==16 and card.isdigit():
            return True
        else:
            print('invalid Error')


    def _check_pin(self,pin):
        if len(pin)==4 and pin.isdigit():
            return True
        else :
            print('invalid pin')

    def __init__(self,card,pin):

        if self._check_card(card = card) and self._check_pin(pin = pin):
            self.__card = card
            self.__pin = pin
            self.money = 0
        else:
            print('Your card is not inititialize')

    def _validation(self,pin):
        if self.__pin == pin:
            return True
        else:
            return False

    def put(self,pin,money):
        if self._validation(pin=pin):
             self.money +=money
             print(f'There is {self.money}')
        else:
            print('Uncorect pin')



    def _check_money(self,money):
        if money % 10 ==0:
            return True
        else:
            return False

    def _check_balanc(self,money):
        if self.money < money:
                print('low balance')
                return False
        else:
            return True
    
    def get_money(self,pin,money):
        if self._validation(pin=pin):
            if self._check_money (money=money) and self._check_balanc(money=money):
                self.money-=money
                print(f'You have cash {self.money}')


        else:
            print('Not correct pin code')

card = Terminal(card='1212345678123456',pin='1234')
card.put(pin='1234',money=1000)
card.get_money(pin='1234',money =190)
print(card.money)





