"""
This program will automatically generate the trouble tickets to request new SFDC user profiles for submission by one end user
"""

import boto3
import webbrowser
import psycopg2
import pandas as pd
import logging
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
s3 = boto3.resource('s3')
source_bucket = 's3_bucket'
sql_script = 'new_user_query.sql'


class MyDatabase():
    """This class is designed to create one database connection for use in a module"""
    database = 'DATABASE-NAME'
    host = 'HOST_NAME'
    port = 'PORT_NUMBER'
    user = 'DB_USERNAME' #username and password can be replaced with amazon secrets in the future
    password = 'USER_PWD'

    def __init__(self):
        self.conn = psycopg2.connect(dbname=self.database, host=self.host, port=self.port,
                                     user=self.user, password=self.password)
        self.cur = self.conn.cursor()

    def query(self, query):
        if query.lower().startswith('select'):
            logging.info('selecting data')
            self.cur.execute(query)
            return self.cur.fetchall()
        else:
            logging.info('modifying data')
            self.cur.execute(query)
            self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


"""Establish a database connection for use by the program"""
try:
    logging.info('attempting to connect to the database')
    db = MyDatabase()
    logging.info('successfully connected to the database')
except Exception as e:
    logging.info('unable to connect to the database')
    logging.error(e)
    sys.exit(1)


def get_new_user_query():
    """Retrieve the SQL query to be executed by the program from S3"""
    try:
        logging.info('importing SQL script from S3')
        obj = s3.Object(source_bucket, sql_script)
        new_user_query = obj.get()['Body'].read()
        logging.info('successfully imported SQL script from S3')
        return new_user_query
    except Exception as e:
        logging.info('unable to import SQL script from S3')
        logging.info(e)
        sys.exit(1)


def get_new_users(new_user_query):
    """Execute new user query to retrieve and read into dataframe"""
    try:
        logging.info(f'executing SQL script : {new_user_query}')
        logging.info('creating dataframe with query results')
        new_users = pd.read_sql(new_user_query, db.conn)
        return new_users
    except Exception as e:
        logging.info('unable to create new user dataset')
        logging.info(e)


def get_new_user_variable_names(query_results):
    """Retrieve column names from the dataframe for use as variables"""
    try:
        logging.info('generating list of variables for tt from query results')
        new_user_variables = [x for x in query_results]
        #new_user_variables = list(filter(lambda x: x != 'manager_alias_hrbi'and x !='manager_alias_contact', query_results))
        logging.info(f'variables identified : {new_user_variables}')
        return new_user_variables
    except Exception as e:
        logging.info('unable to retrieve new user variable names')
        logging.info(e)


def generate_new_user_tt(query_results, new_user_variables):
    """Generate new user tt browser windows from new user data"""
    try:
        logging.info('generating tt browser windows from query results and new user variables')
        tt_data = query_results[new_user_variables]
        for index, row in tt_data.iterrows():
            new_user_details  = list(row[new_user_variables])
            url = f"https://tt.amazon.com/new?ticket_type=Regular+Ticket&prev_qid=0&impact=5&cti-finder-type=keyword&"\
                  "category=AWS-Global+Business+Operations&type=AWS+Salesforce&item=PSA&"\
                  "assigned_group=GBO+AWS+Salesforce+PSA&assigned_individual=xiaenns&country=United+States&bldg=SEA58&"\
                  "problem_location=Seattle%40%40%40SEA58+-+Kumo&case_type=Trouble+Ticket&quicklink_creator=drewnash&"\
                  "short_description=Salesforce+-+PSA+-+New+User&details=First+Name%3A+{}%0D%0ALast+Name%3A+{}%0D%0"\
                  "AAmazon+Alias%3A+{}%0D%0AProServe+Start+Date%3A+{}%0D%0AReports+to+Alias%3A+{}%0D%0"\
                  "ARegion%3A+{}+%0D%0APractice%3A+{}%0D%0ALevel%3A+L6%0D%0"\
                  "AResource+Role%3A+{}%0D%0ASpecialization%3A+SELECT%20ONE%0D%0ACity%3A+{}%0D%0AState%3A"\
                  "+{}%0D%0ACountry%3A+{}%0D%0ASet+Up+Similar+to+Amazon+Alias%3A+".format(*new_user_details)
            webbrowser.open(url)
        logging.info('done generating tt browser windows')
    except Exception as e:
        logging.info('unable to generate tt')
        logging.info(e)


def close_connection():
    """Close the database connection"""
    try:
        logging.info('closing the database connection')
        db.close()
        logging.info('success')
    except Exception as e:
        logging.info('unable to close the database connection')
        logging.info(e)


def the_kick():
    """Run all module functions"""
    try:
        new_user_query = get_new_user_query()
        query_results = get_new_users(new_user_query)
        new_user_variables = get_new_user_variable_names(query_results)
        generate_new_user_tt(query_results, new_user_variables)
        close_connection()
    except Exception as e:
        logging.info('unable to run module')
        logging.info(e)
        sys.exit(1)


if __name__ == '__main__':
    the_kick()
