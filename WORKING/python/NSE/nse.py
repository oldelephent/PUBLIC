import nsetools
from pprint import pprint
import pandas as pd, numpy as np
# import nselib
# from nselib import capital_market
# import nselib.derivatives 
# #data = nselib.trading_holiday_calendar()
# data = capital_market.price_volume_and_deliverable_position_data(symbol='SBIN', period='1M')
# #data = capital_market.bhav_copy_equities()
# print(data)
from nsetools import Nse
q = Nse.get_quote('infy')

pprint(q) 
