"""
Mongodb #1
test and learn mongodb
"""
import pymongo
import logging
from connect_mongodb import *
#from connect_mongodb import * 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Setup the connection to mongodb')
def main():
	with connect_mongodb.login_mongodb_cloud() as client:
		
		logger.info('We are going to use a database called dev')
		db = client['dev']
		logger.info('And in that database create a collection called furniture')
		furniture = db['furniture']
		logger.info('Now we add data from the dictionary')
		results = furniture.insert_many([
			{
			'product': {'product_type': 'couch', 'color': 'red'},
			'in_stock_quantity': 10
			},
			{
			'product': {'product_type': 'couch', 'color':'blue'},
			'in_stock_quantity': 3
			},
			{
			'product':{'product_type': 'table', 'color':'brown'},
			'in_stock_quantity':17
			},
			{
			'product':{'product_type': 'chair', 'color': 'green'},
			'in_stock_quantity': 4
			}])
		
		logger.info('Find the table products and their colors')
		query_couch = {'product.product_type': 'couch'}
		results = furniture.find_one(query_couch, {'product.color': 'red'})
		print(results)

if __name__ == '__main__':
    main()
