"""
Populate the department that each
job falls under.
"""
import logging
from peewee import *
from v00_personjob_model import Job, Department

def populate_department():
	"""
	add department data to database
	"""

	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger(__name__)

	database = SqliteDatabase('personjob.db')
	logger.info('Working with Department class')
	job_name = 0
	department_number = 1
	department_name = 2
	department_manager = 3
	
	depts = [('Analyst', 'A123','Analytics', 'Navdeep'),
	         ('Senior analyst', 'A123','Analytics', 'Navdeep'),
	         ('Senior business analyst', 'A123','Analytics', 'Navdeep'),
	         ('Admin manager','B123', 'Administrative', 'Kaleb'),
	         ('Admin supervisor','B123', 'Administrative', 'Kaleb')]

	try:
		database.connect()
		database.execute_sql('PRAGMA foreign_keys = ON;')
		for dept in depts:
			with database.transaction():
				new_dept = Department.create(
					job_title = dept[job_name],
					department_number = dept[department_number], 
					department_name = dept[department_name], 
					department_manager = dept[department_manager])
				new_dept.save()
		for saved_dept in Department:
			logger.info(f'{saved_dept.department_number}, {saved_dept.department_name}, {saved_dept.department_manager}')
	except Exception as e:
		logger.info(f'Error creating = {dept[department_number]}')
		logger.info(e)
	finally:
		database.close()

if __name__ == '__main__':
	populate_department()





