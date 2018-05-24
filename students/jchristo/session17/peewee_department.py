"""
    Simple database example with Peewee ORM, sqlite and Python
    Here we define the schema
    Use logging for messages so they can be turned off
"""

import logging
from peewee import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('One off program to build the classes from the model in the database')

logger.info('Here we define our data (the schema)')
logger.info('First name and connect to a database (sqlite here)')

logger.info('The next 3 lines of code are the only database specific code')
logger.info('The database will run in memory for the session')

db = SqliteDatabase(':memory:')
db.connect()
db.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

logger.info('This means we can easily switch to a different database')
logger.info('Enable the Peewee magic! This base class does it all')
logger.info('By inheritance only we keep our model (almost) technology neutral')


class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """

    logger.info('Note how we defined the class')

    logger.info('Specify the fields in our model, their lengths and if mandatory')
    logger.info('Must be a unique identifier for each person')

    person_name = CharField(primary_key = True, max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)
    job_held = ForeignKeyField(Job, related_name='job held', null = False)


class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """

    logger.info('Now the Job class with a similar approach')
    job_name = CharField(primary_key = True, max_length = 30)
    logger.info('Dates')
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    logger.info('Number')

    salary = DecimalField(max_digits = 7, decimal_places = 2)
    logger.info('Which person had the Job')
    #person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)
    #department_id = CharField(max_length = 4)
    job_department = ForeignKeyField(Department, related_name='department id', null = False)


class PersonNumKey(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """

    logger.info('An alternate Person class')
    logger.info("Note: no primary key so we're give one 'for free'")
    person_name = CharField(max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)


class Department(BaseModel):
    """
        This class defines Department, which maintains details of
        which Department a Person held a job.
    """

    logger.info('A Department class')
    logger.info('Adding the relevant information')
    department_number = CharField(primary_key = True, max_length = 4)
    department_name = CharField(max_length = 30)
    #department_manager = ForeignKeyField(Person, person.person_name,related_name='was_filled_by', null = False)
    #department_manager = CharField(max_length = 30)
    logger.info('Done adding the relevant information')


db.create_tables([
        Job,
        Person,
        PersonNumKey,
        Department
    ])


#put some values in the DB
hank = Person.create(person_name='Henry', lives_in_town='Boston', nickname='Hank', job_held='Biz Ops Manager')
steve = Person.create(person_name='Steven', lives_in_town='Boston', nickname='Steve', job_held='Sales Manager')

biz_ops_manager = Job.create(job_name='Biz Ops Manager', start_date='2012-01-10',
                             end_date='2014-05-17', salary='100000',person_employed='Henry',
                             job_department='X123')
sales_manager = Job.create(job_name='Sales Manager', start_date='2012-02-14',
                             end_date='2016-08-10', salary='90000',person_employed='Steven',
                           job_department='X125')

biz_ops_department = Department.create(department_number='X123',
                                       department_name='Global Operations', department_manager='Henry')
sales_department = Department.create(department_number='X125',
                                       department_name='Global Sales', department_manager='Steven')

#generate a few queries to test syntax
query = (Person.select(), Job.select(), Department.select())

query_2 = (Person
           .select(Person.person_name, Job.job_name)
           .join(Job, on=(Person.person_name == Job.person_employed).alias('Employee'))
           )

query_3 = (Person
           .select(Person.person_name, Job.job_name, Department.department_name)
           .join(Job, on=(Person.person_name == Job.person_employed).alias('Employee'))
           .join(Department, on=(Department.department_number == Job.department_id.alias('Dept ID')))
           )

query_4 = (Person
           .select(Person.person_name, Job.job_name, Job.start_date, Job.end_date, Department.department_name)
           .join(Department, on=(Person.person_name == Department.department_manager.alias('Dept Manager')))
           .join(Job, on=(Department.department_number == Job.department_id.alias('Dept ID')))
           )


#running into the error "peewee.IntegrityError: FOREIGN KEY contstraint failed, unsure how to resolve...
for person in query_2:
    print(f'{Person.person_name}, {Job.job_name}')

for person in query_3:
    print(Person.person_name, Job.job_name, Department.department_name)

db.close()
