import ccxt 
# import dontshareconfig
import os 
import time
import dotenv
dotenv.load_dotenv()
id = os.getenv("id")

secret = os.getenv("secret" )
   
exchange = ccxt.phemex({
    'apiKey': id,
    'secret': secret,
})

balance = exchange.fetch_free_balance()['USDT']
print(balance)
# order = exchange.create_market_order("BTC/USDT", "buy", 0.000018 )
# print(order)
# time.sleep(10)
# order2 = exchange.create_market_order("BTC/USDT", "sell", 0.000018 )
# print(order2)

# time.sleep(10)
# num =0
# while num < 1000 :
#     num+=1
#     print(f"done{num}")
