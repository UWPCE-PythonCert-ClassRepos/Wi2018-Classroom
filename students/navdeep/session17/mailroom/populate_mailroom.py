from peewee import *
from mailroom_database import *
import logging


class ManipulateDB(object):
	def __init__(self):
		database = SqliteDatabase('donor_database.db')

	def add_donor(self, first_name, last_name, email, donation_amount):
		"""
		Ability to add a new donor to the database or if the donor exists, we can still add a new donation
		"""
		if not self.donor_exists(email):
			try:
				database.connect()
				database.execute_sql('PRAGMA foreign_keys = ON;')
				with database.transaction():
					new_donor = Donor.create(
						donor_email = email,
						first_name = first_name,
						last_name = last_name,
						combined_name = first_name + ' ' + last_name)
					new_donor.save()
			except Exception as e:
				print(f'Error creating = {email}')
				print(e)
			finally:
				database.close()
		self.add_donation(email, donation_amount)

	def add_donation(self, email, donation_amount):
		"""
		Adds a new donation to database
		"""
		next_invoice_num = self.last_invoice_number() + 1
		try:
			database.connect()
			database.execute_sql('PRAGMA foreign_keys = ON;')
			with database.transaction():
				new_donation = Donation.create(
					invoice = next_invoice_num,
					donor_email = email,
					amount = donation_amount)
				new_donation.save()
		except Exception as e:
			print(f'Error creating = {email}')
			print(e)
		finally:
			database.close()

	def last_invoice_number(self):
		"""
		Will retrieve the most recent invoice number so when we append a new donation to the database, we can ensure we are not duplicating primary keys
		"""
		max_invoice = 0
		try:
			database.connect()
			database.execute_sql('PRAGMA foreign_keys = ON;')
			with database.transaction():
				query = Donation.select(fn.MAX(Donation.invoice).alias('last_invoice'))
				for inv in query:
					max_invoice = inv.last_invoice
		except Exception as e:
			print("Error occurred. See below")
			print(e)
			print('\n')
		finally:
			database.close()
			if not max_invoice:
				return 0
			else:
				return max_invoice

	def thank_you_message(self, name, donation_amount):
		"""
		Creates thank you message for donor
		"""
		thank_you_message = "\nThank you {0:s} for you generous donation of ${1:.2f}.\n".format(name, round(donation_amount,2))
		return thank_you_message

	def delete_donation(self, email):
		"""
		Ability to delete donors and their donations
		"""
		try:
			database.connect()
			database.execute_sql('PRAGMA foreign_keys = ON;')
			query_donations = Donation.delete().where(Donation.donor_email == email)
			query_donor = Donor.delete().where(Donor.donor_email == email)
			query_donations.execute()
			query_donor.execute()
		except Exception as e:
			print(f'Error deleting = {email}')
			print(e)
		finally:
			database.close()

	def donor_exists(self, email):
		"""
		Determines if donor already exists in database
		"""
		current_donor = False
		try:
			database.connect()
			database.execute_sql('PRAGMA foreign_keys = ON;')
			query = Donor.select().where(Donor.donor_email == email)
			if query.exists():
				current_donor = True
		except Exception as e:
			print(f'Error occurred. See below')
			print(e)
		finally:
			database.close()
			return current_donor

	def create_report(self):
		str_build = ""
		try:
			database.connect()
			database.execute_sql('PRAGMA foreign_keys = ON;')
			query = (Donor.select(Donor.combined_name,Donor.donor_email,fn.COUNT(Donation.amount).alias('num_donations'), fn.SUM(Donation.amount).alias('sum_donations'), fn.AVG(Donation.amount).alias('avg_donations'))
				.join(Donation, JOIN.INNER)
				.group_by(Donor.donor_email, Donor.combined_name))
			for user in query:
				str_build += "{:25s}   {:25s}   {:11.2f}   {:9.2f}   {:12.2f}\n".format(user.combined_name, user.donor_email, user.num_donations, user.sum_donations, user.avg_donations)
		except Exception as e:
			print('Error occurred. See Below.')
			print(e)
			print('\n')
		finally:
			database.close()
			return str_build

	def write_to_file(self):
		try:
			database.connect()
			database.execute_sql('PRAGMA foreign_keys = ON;')
			file_name = None
			donor_file_name = None
			full_file_name = None
			complete_file_name = None
			query = (Donor.select(Donor.combined_name,Donor.donor_email, fn.SUM(Donation.amount).alias('sum_donations'))
				.join(Donation, JOIN.INNER)
				.group_by(Donor.donor_email, Donor.combined_name))

			for user in query:
				donor_file_name = user.donor_email
				full_file_name = "{}.txt".format(donor_file_name)
				complete_file_name = os.path.join(os.getcwd(), full_file_name)
				letter = self.letter_to_file(user.combined_name, user.sum_donations)
				with open(complete_file_name, 'w+') as f:
					f.write(letter)
		except Exception as e:
			print("Error occurred. See below")
			print(e)
			print('\n')
		finally:
			database.close()

	def letter_to_file(self, donor, donations):
		str_letter = "Dear {},\n\tThank you for your kind donation(s) of {}.\n\tIt will be put to very good use.\n\t\tSincerely,\n\t\t\t-The Team".format(donor, str(donations))
		return str_letter

	def show_donors(self):
		"""
		Lists the donor names
		"""
		str_build = ""
		try:
			database.connect()
			database.execute_sql('PRAGMA foreign_keys = ON;')
			for name in Donor.select():
				str_build += name.combined_name + '\n'
		except Exception as e:
			print(f'Error occured. See below')
			print(e)
		finally:
			database.close()
			return str_build




