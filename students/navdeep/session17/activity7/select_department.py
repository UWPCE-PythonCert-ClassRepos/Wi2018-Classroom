from peewee import *
from v00_personjob_model import Job, Department, Person
import logging

def select_dept():
	"""
	select departments to show they are in database
	"""
	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger(__name__)
	database = SqliteDatabase('personjob.db')

	try:
		database.connect()
		database.execute_sql('PRAGMA foreign_keys = ON;')
		query = (Person
			.select(Person, Job,Department)
			.join(Job, JOIN.INNER)
			.join(Department, JOIN.INNER)
			)
		logger.info('View each department each person has worked in')
		for person in query:
			logger.info(f'Person: {person.person_name}, Job: {person.job.job_name}, Department: {person.job.department.department_name}')
	except Exception as e:
		logger.info(e)
	finally:
		database.close()

if __name__ == '__main__':
	select_dept()