import numbers
import statistics as stat
import csv
import re
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class Donor(object):



    def __init__(self, fnam,lnam,donation=[0]):
        self.fnam = fnam
        self.lnam = lnam
        self.donation = []
        self.add_donation(donation)

    def __str__(self):
        return f"<p>Greetings {self.fnam} {self.lnam},</p>" \
               f"<p>Thank you for the {len([i for i in self.donation if i>0])} donations totalling ${sum([i for i in self.donation])}.</p>" \
               f"<p>Sincerly,<br />Python Class</p>"

    def __repr__(self):
        return f"{'{:<20}'.format(self.fnam + ' ' + self.lnam)}" \
               f"{'{:>20.2f}'.format( sum([i for i in self.donation]))}" \
               f"{'{:>20}'.format(len([i for i in self.donation if i>0]))}" \
               f"{'{:>20.2f}'.format(stat.mean([i for i in self.donation if i>0]))}"

    def __iadd__(self, other):
        self.add_donation(other)
        return  self

    def add_donation(self,donation):

        if type(donation) == list or type(donation) == tuple:
            for i in donation:
                if isinstance(i,numbers.Number):
                    self.donation.append(float("{0:.2f}".format(i)))
        if isinstance(donation,numbers.Number):
            self.donation.append(float("{0:.2f}".format(donation)))

    def write_line(self):
        return f"{self.fnam + ',' + self.lnam}," \
               f"{'{:.2f}'.format( sum([i for i in self.donation]))}," \
               f"{len([i for i in self.donation if i>0])}," \
               f"{'{:.2f}'.format(stat.mean([i for i in self.donation if i>0]))}"

    @property
    def keyval(self):
        return self.fnam.lower().strip() + self.lnam.lower().strip()

    @staticmethod
    def make_key(name):
        pattern=re.compile(r'\s+')
        return re.sub(pattern,'',name).lower()

    def send_message(self):

        testmail = "shopkins@seagen.com"
        msg = MIMEMultipart('alternative')
        msg['From'] = testmail
        msg['To'] = testmail
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = "Thank for your donation"
        msg.attach(MIMEText(self.__str__(),'html'))
        smtp = smtplib.SMTP("sendsmtp.seagen.com")
        smtp.sendmail(testmail, testmail, msg.as_string())
        smtp.close()


class Donors(object):

    def __init__(self):
        self.donors={}

    def new_or_append(self,donor):

        k=donor.keyval
        if k not in self.donors:
            self.donors[k]=donor
        else:
            self.donors[k].add_donation(donor.donation)

    def load(self,in_file):
        with open(in_file,'rU') as file:
            reader=csv.reader(file)
            next(reader)
            [self.new_or_append(d) for d in [Donor(r[0],r[1],float(r[2])) for r in reader]]
            return self

    def get(self,k):
        return self.donors.get(k)

    def send_report(self):
        testmail = "shopkins@seagen.com"
        msg = MIMEMultipart('alternative')
        msg['From'] = testmail
        msg['To'] = testmail
        msg['Date'] = formatdate(localtime=True)

        msg['Subject'] = "Donation report"

        msgtext = "<style>table, th, td {border: 1px solid black;border-collapse: collapse;}</style>"
        msgtext += "<table><caption>Donation Report</caption><tr><th>First Name</th><th>Last Name</th><th>Number of Donations</th><th>Total</th></tr>"
        for i,j in self.donors.items():
            msgtext += f"<tr><td>{j.fnam}</td><td>{j.lnam}</td><td>{len([i for i in j.donation if i>0])}</td><td>{sum([i for i in j.donation])}</td></tr>"
        msgtext += "</table>"

        msg.attach(MIMEText(msgtext, 'html'))

        smtp = smtplib.SMTP("sendsmtp.seagen.com")
        smtp.sendmail(testmail, testmail, msg.as_string())
        smtp.close()




