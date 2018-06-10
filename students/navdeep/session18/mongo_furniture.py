"""
Mongodb #1
test and learn mongodb
"""
import pymongo
import logging
#from connect_mongodb import * 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Setup the connection to mongodb')
def main():
	with login_mongodb_cloud() as client:
		
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

def login_mongodb_cloud():
    """
    connect to mongodb and login
    """
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    log.info('Here is where we use the connect to mongodb.')
    log.info('Note use of f string to embed the user & password (from the tuple).')
    client = pymongo.MongoClient('mongodb://navgill:python@cluster0-shard-00-00-r6qke.mongodb.net:27017,cluster0-shard-00-01-r6qke.mongodb.net:27017,cluster0-shard-00-02-r6qke.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')
    	#config.read(config_file)
    return client

if __name__ == '__main__':
    main()
