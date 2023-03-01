from numpy import size


class sqStock:
    
    def __init__(self,name,cost):
        self.stock_name = name
        self.stock_acost = cost #acquisition costs
    
    def info(self):
        print("Stock name is {}, acquisition costs are {}".format(self.stock_name,self.stock_acost))

class sqAccount:
    def __init__(self,initial_money=0):
        self.money = initial_money
        self.stock = []
        
    def input_money(self,money):
        self.money = self.money + money
        
    def input_stocks(self,stock):
        self.stock.extend(stock)

    def info(self):
        sizeofstock = len(self.stock)
        print("I have {} of stocks".format(sizeofstock))
        for stock_item in self.stock:
            stock_item.info()

class sqTrader:
    def __init__(self):
        self.account = sqAccount()
        
    def make_account(self,initial_money):
        self.account.input_money(initial_money))
        
        

myaccount = sqAccount(1000)

astocks = [sqStock("QQQ",100),sqStock("SPY",100),sqStock("GO",100),sqStock("QWE",100)]
myaccount.input_stocks(astocks)
myaccount.info()
