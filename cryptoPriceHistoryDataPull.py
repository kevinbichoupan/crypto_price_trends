import cbpro
import pandas as pd
import datetime


def pullHistoricalData(coin, startDate, endDate):
	
	public_client = cbpro.PublicClient()

	historics = pd.DataFrame(public_client.get_product_historic_rates(coin, granularity = 86400, start = startDate, end = endDate))
	historics.columns = ['date', 'low', 'high', 'open', 'close', 'volume']

	return historics








