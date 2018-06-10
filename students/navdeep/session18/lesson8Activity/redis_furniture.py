import logging
import redis
from connnect_redis import *


logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)
def main():
    log.info('Step 1: connect to Redis')
    r = connnect_redis.login_redis_cloud()
    log.info('Step 2: cache some data in Redis')
    r.delete('Andy')
    r.delete('Navdeep')
    r.delete('Lorenzo')
    r.delete('Nick')
    r.delete('Kaleb')
    r.delete('Torin')
    r.set('Andy', {'email':'andy@somewhere.com', 'phone': '123-456-7890', 'zip':
        '98102'})
    r.rpush('186675', 'chair')
    r.rpush('186675', 'red')
    r.rpush('186675', 'leather')
    r.rpush('186675', '5.99')
    r.hmset('Navdeep', {'email':'nav@somewhere.com', 'phone':'456-123-7890','zip':'98105'})
    r.hmset('Lorenzo',{'email':'enzo@somewhere.com', 'phone':'789-123-4560', 'zip':'98115'})
    r.hmset('Nick', {'email':':nick@somewhere.com', 'phone':'423-156-7890', 'zip':'98105'})
    r.hmset('Kaleb', {'email':'ksmith@somewhere.com','phone': '178-123-7890', 'zip':'98007'})
    r.hmset('Torin', {'email':'torin@somewhere.com', 'phone':'012-781-4567', 'zip':'98111'}) 
    log.info('Step 2: now I can read it')
    customer_one = r.get('Andy')
    log.info('But I must know the key')
    print(customer_one)
    #element = r.lindex('user2', 0)
    #element = str(element)
    #element = int(element)
    r.delete('Andy')
    Nav_Email = r.hget('Navdeep', 'email')
    Nav_Zip = r.hget('Navdeep', 'zip')
    Nav_Phone = r.hget('Navdeep', 'phone')
    print(Nav_Email)
    print(Nav_Zip)
    print(Nav_Phone)

if __name__ == '__main__':
    main()