from lib.SQP import * 


trader = sqTrader()
trader.make_account(10000)
trader.buy_stock("QQQ",10,100,10)
trader.buy_stock("QQQ",10,100,10)
trader.buy_stock("SHY",20,90,10)
trader.buy_stock("QQQ",10,100,10)
trader.info()

account = trader.account
if(account.set_market_price({'QQQ':120,'SHY':91})):
    print("OK")
else:
    print("FAILURE")