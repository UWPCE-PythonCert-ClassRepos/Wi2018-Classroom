import connnect_redis
import os


class ManipulateDBRedis(object):
	def __init__(self):
		self.redisdb = connnect_redis.login_redis_cloud()

	def add_donor_redis(self, new_first_name, new_last_name, new_email, donation_amount):
		"""
		Ability to add a new donor to the mongo database or if the donor exists, we can still add a new donation
		"""
		transaction_id = new_email + '_1'
		if not self.donor_exists_redis(new_email):
			try:
				full_name = new_first_name + ' ' + new_last_name
				self.redisdb.rpush(new_email, full_name)
				self.redisdb.rpush(new_email, donation_amount) 
			except Exception as e:
				print(f'Error creating = {new_email}')
				print(e)
		else:
			self.add_donation_redis(new_email, donation_amount)

	def add_donation_redis(self, email, donation_amount):
		"""
		Adds a new donation to database
		"""
		try:
			self.redisdb.rpush(email, donation_amount)
		except Exception as e:
			print(f'Error adding donation to: {email}')
			print(e)

	def thank_you_message(self, name, donation_amount):
		"""
		Creates thank you message for donor
		"""
		thank_you_message = "\nThank you {0:s} for you generous donation of ${1:.2f}.\n".format(name, round(donation_amount,2))
		return thank_you_message

	def delete_donation_redis(self, del_email):
		"""
		Ability to delete donors and their donations
		"""
		try:
			self.redisdb.delete(del_email)
			print("{} has been removed from the database\n".format(del_email))
		except Exception as e:
			print(f'Error deleting = {email}')
			print(e)

	def donor_exists_redis(self, find_email):
		"""
		Determines if donor already exists in database
		"""
		current_donor = False
		try:
			for key in self.redisdb.keys():
				if key == find_email:
					current_donor = True
		except Exception as e:
			print(f'Error occurred. See below')
			print(e)
		return current_donor

	def create_report(self):
		"""
		Create Report using Mongo queries
		"""
		str_build = ""
		try:
			for donor in self.redisdb.keys():
				num_donation = self.num_donations(donor)
				sum_donation = self.sum_donations(donor)
				str_build += "{:25s}   {:25s}   {:11.2f}   {:9.2f}   {:12.2f}\n".format(self.redisdb.lindex(donor, 0), donor, num_donation, sum_donation , (sum_donation / num_donation))
		except Exception as e:
			print('Error occurred. See Below.')
			print(e)
			print('\n')
		return str_build

	def sum_donations(self, donor_email):
		"""
		Sums a donors donations
		"""
		sum_list = 0
		element = None
		for index in range(1, self.redisdb.llen(donor_email)):
			element = self.redisdb.lindex(donor_email, index)
			element = str(element)
			element = float(element.strip())
			sum_list += element
		return sum_list

	def num_donations(self, donor_email):
		"""
		Returns the number of donations a donor has given
		"""
		return self.redisdb.llen(donor_email) - 1

	def write_to_file(self):
		"""
		Writes to a file.  The donors name and total donations will be stored in the contents of the file, while the file name will be the donors email address
		"""
		try:
			file_name = None
			donor_file_name = None
			full_file_name = None
			complete_file_name = None
			for donor in self.redisdb.keys():
				donor_file_name = donor
				total_donations = self.sum_donations(donor)
				donor_full_name = self.redisdb.lindex(donor, 0)
				full_file_name = "{}.txt".format(donor_file_name)
				complete_file_name = os.path.join(os.getcwd(), full_file_name)
				letter = self.letter_to_file(donor_full_name,total_donations)
				with open(complete_file_name, 'w+') as f:
					f.write(letter)
		except Exception as e:
			print("Error occurred. See below")
			print(e)
			print('\n')

	def letter_to_file(self, donor, donations):
		str_letter = "Dear {},\n\tThank you for your kind donation(s) of {}.\n\tIt will be put to very good use.\n\t\tSincerely,\n\t\t\t-The Team".format(donor, str(donations))
		return str_letter

	def show_donors(self):
		"""
		Lists the donor names
		"""
		str_build = ""
		try:
			for donor_email in self.redisdb.keys():
				str_build += self.redisdb.lindex(donor_email, 0) + ' -- ' + donor_email  +'\n'
		except Exception as e:
			print()
		return str_build




