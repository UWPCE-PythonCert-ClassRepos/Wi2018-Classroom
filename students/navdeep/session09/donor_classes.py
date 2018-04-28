
import os.path

class Donor(object):
    def __init__(self, first_name, last_name, donation):
        """
        Initializes the donor's first name, last name and creates a new donation list for the donor. Their first donation will be appended to the donation list.
        :param first_name: the donor's first name
        :param last_name: the donor's last name
        :param donation: the donor's first donation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.donation_list = []
        self.append_donation(donation)

    def get_full_name(self, first = None, last = None):
        """
        The donor's full name. Primarily used for printing purposes in the main script. The full name is how the user will see the donor names printed out in the report or when the user just wants to see a list of donor names.
        :param first: the donor's first name, a string
        :param last: the donor's last name, a string
        :return: the donor's full name, a string. Concatenate the first and last name of the donor, which are also strings
        """
        if first == None and last == None:
            return self.first_name + ' ' + self.last_name
        else:
            return first + ' ' + last

    def append_donation(self, donation_amount):
        """
        Appends a new donation to the donor's donation list. There is no limit on the amount of donations a donor can give.
        :param donation_amount: The donation to be appended to the list. A float type
        """
        self.donation_list.append(donation_amount)

    def thank_you_letter(self):
        """
        Returns a thank you message after someone has donated
        :return: The thank you message in string format with the donor's name and most recent donation.
        """
        thank_you_message = "\nThank you {0:s} for you generous donation of ${1:.2f}.\n".format(self.get_full_name(), round(self.donation_list[-1],2))
        return thank_you_message
     
    @property
    def num_donations(self):
        """
        Calculates the total number of donations give for the donor.
        :return: the length of the donor's donation list
        """
        return len(self.donation_list)

    @property
    def sum_donations(self):
        """
        Calculates the sum of all donations given
        :return: the sum of the donations in the donor's donations list.
        """
        return sum(self.donation_list)
     
    @property
    def avg_donations(self):
        """
        Calculates the average of all donations given
        :return: the average donation given in the donor's donations list
        """
        return self.sum_donations / self.num_donations

class DonorCollection(Donor):
    def __init__(self):
        """
        Initializes the dictionary that stores all of the donor objects
        """
        self.donor_dict = {}

    def clean_text(self, name):
        """
        Elimnates whitespace, lowercase each letter except the
        first letter.
        :param name: the text we want cleaned
        :return: the cleaned text
        """
        name = name.strip()
        name = name.lower()
        name = name.title()
        return name

    def create_dict_key(self, first, last):
        """
        Creates the dictionary key as a tuple comprised of the
        first and last name of the donor. There will be two elements
        in the tuple.
        :param first: the first name of the donor
        :param last: the last name of the donor
        :return: the tuple made up of the first and last name of the donor
        """
        key_tup = (first, last)
        return key_tup
    
    def donor_exists(self, first, last):
        """
        This method will test whether or not a donor already exists in the 
        dictionary.
        :param first: the donors first name
        :param last: the donors last name
        :return: True if donor exists in the dictionary as a key, false otherwise
        """
        dict_key = self.create_dict_key(first,last)
        if dict_key in self.donor_dict:
            return True
        else:
            return False

    def new_donor(self,first, last, donation):
        """
        When a new donor is added the the collection, the
        init function in the donor class will be called because
        we want to create a new instance of a Donor 
        """
        if self.donor_exists(first, last):
            donor_key = self.create_dict_key(first, last)
            self.donor_dict[donor_key].append_donation(donation)
        else:
            current_donor = Donor(first, last, donation)
            self.append_collection_dict(current_donor)

    def get_thank_you(self, first, last):
        """
        Retrieves the thank you message for a specific donor
        :param first: the first name of the donor
        :param last: the last name of the donor
        :return: the thank you message for the donor
        """
        donor_key = self.create_dict_key(first, last)
        return self.donor_dict[donor_key].thank_you_letter()

    def append_collection_dict(self, donor_object):
        """
        Appends a new donor object to the collection dictionary
        :param donor_object: The new donor object that will be appended
        to the dictionary
        """
        dict_key = self.create_dict_key(donor_object.first_name, donor_object.last_name)
        self.donor_dict[dict_key] = donor_object

    def letter_to_file(self, donor, donations):
        """
        The letter that will be saved thanking each donor for their contributions
        :param donor: the name of the donor
        :param donations: the donation amounts
        :return: the letter for each individual, a string
        """
        str_letter = "Dear {},\n\tThank you for your kind donation(s) of {}.\n\tIt will be put to very good use.\n\t\tSincerely,\n\t\t\t-The Team".format(donor, str(donations)[1:-1])
        return str_letter

    def write_to_file(self):
        """
        Writes thank you letters for each individual that has donated
        and saves the file in the current working directory.
        """ 
        file_name = None
        donor_file_name = None
        full_file_name = None
        complete_file_name = None
        for donor_object in self.donor_dict.values():
            donor_file_name = donor_object.get_full_name().replace(" ", "_")
            full_file_name = "{}.txt".format(donor_file_name)
            complete_file_name = os.path.join(os.getcwd(), full_file_name)
            letter = self.letter_to_file(donor_object.get_full_name(), donor_object.donation_list)
            with open(complete_file_name, 'w+') as f:
                f.write(letter)

    def report_header(self):
        """
        The header of the report
        """
        str_header = ('\n{:25s} | {:11s} | {:9s} | {:12s}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        str_header = str_header + '\n' + ("-"*66)
        return str_header

    def create_report(self):
        """
        Creates a table for the report that shows the donor names, how many
        times they donated, the average donation and total donations
        """
        str_build = ""
        for donor_object in self.donor_dict.values():
            str_build += "{:25s}   {:11.2f}   {:9d}   {:12.2f}\n".format(donor_object.get_full_name(), 
            donor_object.sum_donations, 
            donor_object.num_donations, 
            donor_object.avg_donations)
        return str_build