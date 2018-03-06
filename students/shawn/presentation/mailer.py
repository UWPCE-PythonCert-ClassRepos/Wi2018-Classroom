import json
import pypyodbc
from zipfile import ZipFile
import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from flask import Flask
from flask import request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json

        report = Report(int(data['val'])).send_mail()

    return json.dumps({'info': "sent"})


class Report:

    def __init__(self
                 ,report_id
                 ,zip_out="attach.zip"
                 ,server='SG6367\SQLEXPRESS;'
                 ,smtp="sendsmtp.seagen.com"):

        conn=pypyodbc.connect( 'Driver={SQL Server};'
                               f'Server={server}'
                               'database=GSDB_Automation;'
                               'Trusted_Connection=yes;')
        cursor=conn.cursor()

        report=cursor.execute(f"select reportTitle,OutputFolder,reportdescription from report where reportId={report_id}").fetchone()
        email=cursor.execute(f"select emailid,emailRegEx,emailLinkPath from email where reportId={report_id}").fetchone()
        recipients=[r[0] for r in cursor.execute(f"select emailToAddress from emailTo where emailId={email[0]}")]

        self.reportId=report_id
        self.server=server
        self.smtp=smtp
        self.send_from=os.getlogin() + "@seagen.com"
        self.send_to=recipients
        self.subject=report[0]
        self.body=report[2]
        self.loc=report[1]
        self.pattern=email[1].rstrip()
        self.zip_out=zip_out
        self.attach=self.zip_files()

    def zip_files(self):

        test=self.pattern
        rgx=re.compile(self.pattern,flags=re.IGNORECASE)
        files=[os.path.join(self.loc,f) for f in os.listdir(self.loc) if rgx.search(f)]

        ziploc=os.path.join(self.loc,self.zip_out)
        with ZipFile(ziploc,'w') as zip_file:
            for f in files:
                zip_file.write(f,os.path.basename(f))
        if len(files):
            return ziploc
        else:
            return None


    def send_mail(self):

        msg = MIMEMultipart()
        msg['From'] = self.send_from
        msg['To'] = COMMASPACE.join(self.send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.subject.title()

        msg.attach(MIMEText(self.body))

        if self.attach is not None:
            with open(self.attach, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(self.attach)
                )

            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(self.attach)
            msg.attach(part)

        smtp = smtplib.SMTP(self.smtp)
        smtp.sendmail(self.send_from, self.send_to, msg.as_string())
        smtp.close()
