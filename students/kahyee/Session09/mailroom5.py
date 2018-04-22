#!/usr/bin/env python3

class Donor():
    
    def __init__(self, name, amount):
        self.name = name
        self.donations = [amount]
    
    def donate(self, amount):
        self.donations.append(amount)
    
    @property
    def donation_count(self):
        return len(self.donations)
    
    @property
    def donation_total(self):
        return sum(self.donations)
        
    @property
    def avg_donation(self):
        return (self.donation_total / self.donation_count)
        
    def email(self):
        return("\nDear " + self.name + "," \
      	    + "\n\n Thank you for your generous donation of $" + '%.2f' % self.donations[-1] \
      	    + " Your kindness knows no bounds. Yada yada yada." \
      	    + "Please send more money soon \n\n Best, \n Kahyee \n")
    
class Donor_group():
    
    def __init__(self, initial_list):
        self.donors = [Donor(k, v) for k, v in initial_list.items()]
        
    def find_donor(self, name):
        try:
            return [donor.name for donor in self.donors].index(name)
        except ValueError:
            return "New Donor"
                
    def add_donor(self, name, amount):
        if self.find_donor(name) == "New Donor":
            self.donors.append(Donor(name, amount))
        else:
            self.donors[self.find_donor(name)].donate(amount)
        
    def create_report(self):
        print("Donor Name          | Total Given | Num Gifts | Average Gift\n" + "-" * 60)
        for donor in self.donors:
        	gift_count = str(donor.donation_count)
        	gift_total = "%.2f" % donor.donation_total
        	gift_avg = "%.2f" % donor.avg_donation
        	print(donor.name \
        		+ " " * (20 - len(donor.name)) \
        		+ " $" + " " * (12 - len(gift_total)) + gift_total \
        		+ " " * 10 + gift_count \
        		+ " $" + " " * (12 - len(gift_avg)) + gift_avg)
        		
    def list(self):
        for donor in self.donors:
            print(donor.name)
            
    def all_email(self):
        for donor in self.donors:
            thank_you_letter = open(os.getcwd() + '/' + donor + '.txt', 'w+')
            thank_you_letter.write(donor.email())
            thank_you_letter.close()