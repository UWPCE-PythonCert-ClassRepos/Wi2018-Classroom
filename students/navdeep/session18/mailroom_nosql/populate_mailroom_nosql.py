import connect_mongodb
import os


class ManipulateDBMongo(object):
	def __init__(self):
		self.mongodb = connect_mongodb.login_mongodb_cloud()

	def add_donor_mongo(self, new_first_name, new_last_name, new_email, donation_amount):
		"""
		Ability to add a new donor to the mongo database or if the donor exists, we can still add a new donation
		"""
		if not self.donor_exists_mongo(new_email):
			with self.mongodb as client:
				db = client['dev']
				mailroom = db['mailroom']
			try:
				mailroom.insert({'email': new_email, 'first_name': new_first_name, 'last_name': new_last_name, 'full_name': new_first_name + ' ' + new_last_name, 'donations': [donation_amount]})
			except Exception as e:
				print(f'Error creating = {new_email}')
				print(e)
			client.close()
		else:
			self.add_donation_mongo(new_email, donation_amount)

	def add_donation_mongo(self, email, donation_amount):
		"""
		Adds a new donation to database
		"""
		with self.mongodb as client:
			db = client['dev']
			mailroom = db['mailroom']
			try:
				mailroom.update({'email':email}, {'$push':{'donations':donation_amount}})
			except Exception as e:
				print(f'Error creating = {email}')
				print(e)
		client.close()

	def thank_you_message(self, name, donation_amount):
		"""
		Creates thank you message for donor
		"""
		thank_you_message = "\nThank you {0:s} for you generous donation of ${1:.2f}.\n".format(name, round(donation_amount,2))
		return thank_you_message

	def delete_donation_mongo(self, del_email):
		"""
		Ability to delete donors and their donations
		"""
		with self.mongodb as client:
			db = client['dev']
			mailroom = db['mailroom']
			try:
				mailroom.remove({"email": {"$eq": del_email}})
				print("{} has been removed from the database\n".format(del_email))
		except Exception as e:
			print(f'Error deleting = {email}')
			print(e)

	def donor_exists_mongo(self, find_email):
		"""
		Determines if donor already exists in database
		"""
		current_donor = False
		with self.mongodb as client:
			db = client['dev']
			mailroom = db['mailroom']
			try:
				query = {'email': find_email}
				results = mailroom.find_one(query)
				if results:
					current_donor = True
			except Exception as e:
				print(f'Error occurred. See below')
				print(e)
		client.close()
		return current_donor

	def create_report(self):
		"""
		Create Report using Mongo queries
		"""
		str_build = ""
		with self.mongodb as client:
			db = client['dev']
			mailroom = db['mailroom']
			try:
				for donor in mailroom.find():
					num_donations = self.num_donations(donor['donations'])
					sum_donations = self.sum_donations(donor['donations'])
					str_build += "{:25s}   {:25s}   {:11.2f}   {:9.2f}   {:12.2f}\n".format(donor['full_name'], donor['email'], num_donations, sum_donations , (sum_donations / num_donations))
			except Exception as e:
				print('Error occurred. See Below.')
				print(e)
				print('\n')
		client.close()
		return str_build

	def sum_donations(self, donation_list):
		"""
		Sums a donors donations
		"""
		return sum(donation_list)

	def num_donations(self, donation_list):
		"""
		Returns the number of donations a donor has given
		"""
		return len(donation_list)

	def write_to_file(self):
		"""
		Writes to a file.  The donors name and total donations will be stored in the contents of the file, while the file name will be the donors email address
		"""
		with self.mongodb as client:
			db = client['dev']
			mailroom = db['mailroom']
			try:
				file_name = None
				donor_file_name = None
				full_file_name = None
				complete_file_name = None
				for donor in mailroom.find():
					donor_file_name = donor['email']
					total_donations = sum(donor['donations'])
					donor_full_name = donor['full_name']
					full_file_name = "{}.txt".format(donor_file_name)
					complete_file_name = os.path.join(os.getcwd(), full_file_name)
					letter = self.letter_to_file(donor_full_name,total_donations)
					with open(complete_file_name, 'w+') as f:
						f.write(letter)
			except Exception as e:
				print("Error occurred. See below")
				print(e)
				print('\n')
		client.close()

	def letter_to_file(self, donor, donations):
		str_letter = "Dear {},\n\tThank you for your kind donation(s) of {}.\n\tIt will be put to very good use.\n\t\tSincerely,\n\t\t\t-The Team".format(donor, str(donations))
		return str_letter

	def show_donors(self):
		"""
		Lists the donor names
		"""
		with self.mongodb as client:
			db = client['dev']
			mailroom = db['mailroom']
			str_build = ""
			try:
				for donor in mailroom.find():
					str_build += donor['full_name'] + ' -- ' + donor['email']  +'\n'
			except Exception as e:
				print(f'Error occured. See below')
				print(e)
		client.close()
		return str_build




