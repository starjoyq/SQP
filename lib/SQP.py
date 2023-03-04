class sqStock:
    
    def __init__(self,name,cost):
        self.stock_name = name
        self.stock_acost = cost #acquisition costs:취득가
    
    def info(self):
        print("Stock name is {}, acquisition costs are {}".format(self.stock_name,self.stock_acost))

class sqAccount:
    def __init__(self,initial_money=0):
        self.money = initial_money
        self.stock = []
        
    def input_money(self,money):
        if(self.money + money > 0):
            self.money = self.money + money
            return True
        else:
            return False
        
    def get_money(self):
        return self.money
        
    def input_stocks(self,stock):
        self.stock.extend(stock)
    
    def set_market_price(self, market_prices):
        stocks = {}
        
        for stock_item in self.stock:
            if(stock_item.stock_name not in market_prices.keys()):
                print("ERROR:set_market_price : no market price. {}".format(stock_item.stock_name))
                return False
            
            market_price = market_prices[stock_item.stock_name]
            if(stock_item.stock_name in stocks.keys()):
                itr_stock_count = stocks[stock_item.stock_name]['count'] + 1
                itr_stock_price = stocks[stock_item.stock_name]['price'] + stock_item.stock_acost
                stocks[stock_item.stock_name] = {'count':itr_stock_count,
                                                 'price':itr_stock_price,
                                                 'avg_price':round(itr_stock_price/itr_stock_count,0),
                                                 'market_price':market_price}
            else:
                stocks[stock_item.stock_name] = {'count':1,
                                                 'price':stock_item.stock_acost,
                                                 'avg_price':stock_item.stock_acost,
                                                 'market_price':market_price}
        print(stocks)
        
        return True

    def info(self):
        sizeofstock = len(self.stock)
        print("I have {} of stocks".format(sizeofstock))
        for stock_item in self.stock:
            stock_item.info()

class sqTrader:
    def __init__(self):
        self.account = sqAccount()
        
    def make_account(self,initial_money):
        self.account.input_money(initial_money)

    def add_money(self,money):
        self.account.input_money(money)
    
    def buy_stock(self,stock_name,stock_count,stock_price,fee):
        stocks = []
        cost = 0
        for i in range(stock_count):
            stocks.append(sqStock(stock_name,stock_price))
            cost += stock_price + fee
        
        if(self.account.input_money(cost*-1)):
            self.account.input_stocks(stocks)
        else:
            print("error")       

    def info(self):
        None