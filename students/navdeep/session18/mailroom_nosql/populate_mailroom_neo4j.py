from neo4j.v1 import GraphDatabase, basic_auth
import os


class ManipulateDBNeo(object):
	def __init__(self, user, password, url):
		self.driver = GraphDatabase.driver(url.strip(),
                                  auth=basic_auth(user.strip(), password.strip()))

	def add_donor_neo(self, new_first_name, new_last_name, new_email, donation_amount):
		"""
		Ability to add a new donor to the neo database or if the donor exists, we can still add a new donation
		"""
		with self.driver.session() as session:
			transaction_id = new_email + '_1'
			if not self.donor_exists_neo(new_email, session):
				try:
					full_name = new_first_name + ' ' + new_last_name
					cyph = "CREATE (n:Donor {email:'%s', first_name:'%s',last_name:'%s', full_name:'%s'})" % (new_email, new_first_name, new_last_name, full_name)
					session.run(cyph)
				except Exception as e:
					print(f'Error creating = {new_email}')
					print(e)
			else:
				self.add_donation_neo(new_email, donation_amount)

	def add_donation_neo(self, email, donation_amount):
		"""
		Adds a new donation to database
		"""
		with self.driver.session() as session:
			try:
				cyph = """
				MATCH (d1:Donor {email: '%s'})
				CREATE (d1)-[donate:DONATION]->({donation_amount: '%s'})
				RETURN d1
				""" % (email, donation_amount)
				session.run(cyph)
			except Exception as e:
				print(f'Error adding donation to: {email}')
				print(e)

	def thank_you_message(self, name, donation_amount):
		"""
		Creates thank you message for donor
		"""
		thank_you_message = "\nThank you {0:s} for you generous donation of ${1:.2f}.\n".format(name, round(donation_amount,2))
		return thank_you_message

	def delete_donation_neo(self, del_email):
		"""
		Ability to delete donors and their donations
		"""
		with self.driver.session() as session:
			try:
				cyph = """
				MATCH (d:Donor {email: '%s'})
				DELETE d
				""" % (del_email)
				print("{} has been removed from the database\n".format(del_email))
			except Exception as e:
				print(f'Error deleting = {email}')
				print(e)

	def donor_exists_neo(self, find_email):
		"""
		Determines if donor already exists in database
		"""
		with self.driver.session() as session:
			current_donor = False
			try:
				cyph = "MATCH (d:Donor) RETURN d.email"
				result = session.run(cyph)
				for record in result:
					if record == find_email:
						current_donor = True
			except Exception as e:
				print(f'Error occurred. See below')
				print(e)
		return current_donor
		
	def write_to_file(self):
		"""
		Writes to a file.  The donors name and total donations will be stored in the contents of the file, while the file name will be the donors email address
		"""
		with self.driver.session() as session:
			try:
				file_name = None
				donor_file_name = None
				full_file_name = None
				complete_file_name = None
			cyph = "MATCH (d:Donor) RETURN d.email"
			result = session.run(cyph) 
			
			for donor in result:
				donor_file_name = donor['email']
				full_file_name = "{}.txt".format(donor_file_name)
				complete_file_name = os.path.join(os.getcwd(), full_file_name)
				letter = self.letter_to_file(donor_full_name,total_donations)
				with open(complete_file_name, 'w+') as f:
					f.write(letter)
			
			except Exception as e:
				print("Error occurred. See below")
				print(e)
				print('\n')

	def letter_to_file(self, donor):
		str_letter = "Dear {},\n\tThank you for your kind donation(s).\n\tIt will be put to very good use.\n\t\tSincerely,\n\t\t\t-The Team".format(donor)
		return str_letter

	def show_donors(self):
		"""
		Lists the donor names
		"""
		with self.driver.session() as session:
			str_build = ""
			try:
				cyph = """
				MATCH (d:Donor)
				RETURN d.full_name as full_name, d.email as email
				"""
				result = session.run(cyph)
				for record in result:
					str_build += record['full_name'] + ' -- ' + record['email'] + '\n'
			except Exception as e:
				print("Error occurred. See below.")
				print(e)
		return str_build




