import numbers
import statistics as s
import csv
import re
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import  formatdate
from enum import Enum
import os
import webbrowser

class Stat:
    x=1,
    s=2,
    n=3


class Donor(object):


    def __init__(self, fnam,lnam,donation=[0]):
        """

        :param fnam: First name (str)
        :param lnam:  Last name (str)
        :param donation: int,float, or list/tuple of int/float
        """
        self.fnam = fnam
        self.lnam = lnam
        self.donation = []
        self.add_donation(donation)



    def __str__(self):
        """

        :return:  HTML for the report generator
        """
        return f"<p>Greetings {self.fnam} {self.lnam},</p>" \
               f"<p>Thank you for the {self.get_stats(Stat.n)} donations totalling ${self.get_stats(Stat.s)}.</p>" \
               f"<p>Sincerly,<br />Python Class</p>"

    def __iadd__(self, other):
        """
        Augmented addition
        :param other: int or interable of (int|float) to add to donations for donor
        :return: Donor
        """
        self.add_donation(other)
        return  self

    def get_stats(self,stat):
        if stat == Stat.x:
            return f"{'{0:.2f}'.format(s.mean([i for i in self.donation if i>0]))}"
        elif stat == Stat.s:
            return f"{'{0:.2f}'.format( sum([i for i in self.donation]))}"
        elif stat== Stat.n:
            return str(len([i for i in self.donation if i>0]))

    def add_donation(self,donation):
        """
        Adds a donation to an existing donor
        :param donation: list|tuple of numbers
        :return: None
        """
        if type(donation) in (list,tuple): #== list or type(donation) == tuple:
            for i in donation:
                if isinstance(i,numbers.Number):
                    self.donation.append(float("{0:.2f}".format(i)))
        if isinstance(donation,numbers.Number):
            self.donation.append(float("{0:.2f}".format(donation)))

    @property
    def keyval(self):
        """
        Gets the key that identifies self in Donors
        :return:  str
        """
        return self.fnam.lower().strip() + self.lnam.lower().strip()

    @staticmethod
    def make_key(name):
        """
        Creates a key value from strings
        :param name: (str) full name of donor
        :return: (str) name converted into dictionary key
        """
        pattern=re.compile(r'\s+')
        return re.sub(pattern,'',name).lower()

    def send_message(self):
        """
        Sends an email message to [testmail] or opens an HTML file if SMTP server connection is unavailable
        :return: message (str)
        """
        try:
            testmail = "shopkins@seagen.com"
            msg = MIMEMultipart('alternative')
            msg['From'] = testmail
            msg['To'] = testmail
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = "Thank for your charity"
            msg.attach(MIMEText(self.__str__(),'html'))
            smtp = smtplib.SMTP("sendsmtp.seagen.com")
            smtp.sendmail(testmail, testmail, msg.as_string())
            smtp.close()
            return "Message sent"
        except Exception as e:
            with open("thankyou.html",'w') as f:
                f.write(self.__str__())
            webbrowser.open("thankyou.html")
            return "Report created"

class Donors(object):

    def __init__(self):
        self.donors={}

    def new_or_append(self,donor):
        """
        Create a new donor, or if donor exists, append donation
        :param donor:
        :return: None
        """
        k=donor.keyval
        if k not in self.donors:
            self.donors[k]=donor
        else:
            self.donors[k].add_donation(donor.donation)

    def load(self,in_file):
        """
        Seed the data structure in the app
        :param in_file:
        :return: Donors (dict)
        """
        with open(in_file,'rU') as file:
            reader=csv.reader(file)
            next(reader)
            [self.new_or_append(d) for d in [Donor(r[0],r[1],float(r[2])) for r in reader]]
            return self

    def get(self,k):
        """
        return a Donor object
        :param k: dictionary key (str)
        :return: Donor
        """
        return self.donors.get(k)

    def challenge(self,factor,min_donation=0,max_donaton=10**10):
        """
        Multiply each donation for a donor by factor
        :param factor: factor by which to multipy donation
        :return: Donors
        """


        for i,v in self.donors.items():
            new_donation=list(map(lambda x: x * factor,filter(lambda x : min_donation <= x <= max_donaton   ,v.donation)))
            v.donation=new_donation

        return  self


    def send_report(self,title= f"Donation report for {datetime.date.today().strftime('%d%b%Y')}"):
        """
        Sends an email message to [testmail] or opens an HTML file if SMTP server connection is unavailable
        :return: message (str)
        """

        msgtext = "<style>table, th, td {border: 1px solid black;border-collapse: collapse;} caption{ 	font-family: \"Allerta Stencil\";" \
                  "font-size: bigger;" \
                  "font-style: normal;" \
                  "color:blue; " \
                  "font-variant: small-caps; " \
                  "font-weight: 500;}" \
                  "</style>"
        msgtext += f"<table cellpadding=\"5\"><caption>{title}</caption><tr style=\"color:blue;\"><th>First Name</th><th>Last Name</th><th>Number of\nDonations</th><th>Mean Donation</th><th>Total</th></tr>"
        counter = 0
        for i, j in self.donors.items():
            if counter % 2:
                msgtext += f"<tr><td>{j.fnam}</td><td>{j.lnam}</td><td>{j.get_stats(Stat.n)}</td><td>{j.get_stats(Stat.x)}</td><td>{j.get_stats(Stat.s)}</td></tr>"
            else:
                msgtext += f"<tr style=\"background-color:aliceblue;\"><td>{j.fnam}</td><td>{j.lnam}</td><td>{j.get_stats(Stat.n)}</td><td>{j.get_stats(Stat.x)}</td><td>{j.get_stats(Stat.s)}</td></tr>"
        counter += 1
        msgtext += "</table>"

        try:
            testmail = "shopkins@seagen.com"
            msg = MIMEMultipart('alternative')
            msg['From'] = testmail
            msg['To'] = testmail
            msg['Date'] = formatdate(localtime=True)

            msg['Subject'] = title

            msg.attach(MIMEText(msgtext, 'html'))

            smtp = smtplib.SMTP("sendsmtp.seagen.com")
            smtp.sendmail(testmail, testmail, msg.as_string())
            smtp.close()
            return "Report sent"

        except Exception as e:
            with open("report.html",'w') as f:
                f.write(msgtext)
            webbrowser.open("report.html")
            return "Report created"




