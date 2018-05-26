import webbrowser
import psycopg2
import pandas as pd
import logging
import os
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sql_script = os.path.normpath("/Users/jchristo/Desktop/PythonProjects/new_user_query.sql")#for Mac, replace with S3 bucket


class MyDatabase():
    """This class is designed to create one database connection for use in a module"""
    database = ''
    host = ''
    port = ''
    user = '' #username and password can be replaced with amazon secrets in the future
    password = ''

    def __init__(self):
        self.conn = psycopg2.connect(dbname=self.database, host=self.host,
                                     port=self.port, user=self.user, password=self.password)
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


#def create_connection():
"""Establish a database connection for use by the program"""
try:
    logging.info('attempting to connect to the database')
    db = MyDatabase()
    logging.info('successfully connected to the database')
    #return db
except Exception as e:
    logging.error(e)
    logging.info('unable to connect to the database')
    sys.exit(1)


"""Retrieve the query to be executed from an external file"""
try:
    with open(sql_script, 'r') as f:
        logging.info('reading SQL script')
        new_user_query = f.read()
        logging.info('SQL script successfully read from file')
except Exception as e:
    logging.info('unable to locate SQL script')


def get_new_users():
    """Execute new user query to retrieve and read into dataframe"""
    try:
        logging.info(f'executing SQL script : {new_user_query}')
        logging.info('creating dataframe with query results')
        new_users = pd.read_sql(new_user_query, db.conn)
        return new_users
    except Exception as e:
        logging.info(e)
        logging.info('unable to create new user dataset')


def get_new_user_variable_names(query_results):
    """This function may not be needed"""
    try:
        logging.info('generating list of variables for TT')
        new_user_variables = [x for x in query_results]
        #new_user_variables = list(filter(lambda x: x != 'manager_alias_hrbi'and x !='manager_alias_contact', query_results))
        logging.info(new_user_variables)
        return new_user_variables
    except Exception as e:
        logging.info(e)


def generate_new_user_tt(query_results, new_user_variables):
    """Generate new user tt browser windows from new user data"""
    try:
        logging.info('generating tt browser windows')
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
        logging.info(e)
        logging.info('unable to generate tt')


def close_connection():
    """Close the database connection"""
    try:
        logging.info('closing the database connection')
        db.close()
        logging.info('success')
    except Exception as e:
        logging.info(e)
        logging.info('unable to close the database connection')


def the_kick():
    """Run all module functions"""
    query_results = get_new_users()
    new_user_variables = get_new_user_variable_names(query_results)
    generate_new_user_tt(query_results, new_user_variables)
    close_connection()


if __name__ == '__main__':
    #create_connection()
    the_kick()
