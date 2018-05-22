from flask import Flask
from flask import request
import os
import  types
import json
import requests
from requests_ntlm import  HttpNtlmAuth
from formats import Fmt, Format_type,Format_val



app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():

    if request.method=="GET":

        try:

            # path = request.json
            # path = os.path.normpath(path.get("path"))
            #
            # os.makedirs(path)
            # return json.dumps({"msg": f"{path}"})


            fmt_dict = {
                "C2C": ('codedValue', 'codedValue', "Default for zero-fill"),
                "T2N": ('crfDecode', 'crfCodedValue', "CRF text to CRF code"),
                "N2P": ('crfCodedValue', 'codedValue', "CRF code to CDISC preferred term"),
                "P2N": ('codedValue', 'crfCodedValue', "CDISC preferred term to CRF code"),
                "T2P": ('crfDecode', 'codedValue', "CRF text to CDISC preferred term"),
                "P2T": ('codedValue', 'crfDecode', "CDISC preferred term to CRF text"),
                "P2S": ('codedValue', 'stdCrfCodedValue', "CDISC preferred term to TLF code"),
                "P2C": ('codedValue', 'stdCrfDecode', "CDISC preferred term to TLF text"),
                "S2C": ('stdCrfCodedValue', 'stdCrfDecode', "TLF code to TLF text"),
                "C2S": ('stdCrfDecode', 'stdCrfCodedValue', "TLF text to TLF code")}


            r=requests.get("http://sgcandidapp1/Candid/api/v1/1/analysis/1000/controlledterms",auth=HttpNtlmAuth("seagen.com\sas_test","Welcome1"))
            data=json.loads(r.text)

            sasfile=os.path.normpath("\\\\sgsasfsv1\\biometrics\\projects_dev\\junk\\formats.sas")


            format_catalog=[]
            for i in data:
                # Create a new format
                fmt=Fmt(i['sasFormatName'],i['description'],i['isExtensible'])

                ct = i.get('controlledTermItems')

                if ct.__len__() > 0:
                        # crfDecode,crfCodedValue,codedValue,stdCrfCodedValue,stdCrfDecode
                    for k, v in fmt_dict.items():
                        for j in ct:
                            a=j[v[0]]
                            b= j[v[1]]
                            if j[v[0]] and j[v[1]]:
                                fmt.category=k
                                fmt.category_desc=v[2]
                                fmt.add_members(j[v[0]],j[v[1]])

                    if fmt.dictvals.__len__()>0:
                        format_catalog.append(fmt)

                        is_num=all(isinstance(item[0], int) for item in fmt.dictvals)
                        is_inf=all(isinstance(item[1], int) for item in fmt.dictvals)

                        # Identify invalue/value of char or num type
                        if not is_inf:
                            fmt.fmt_value=Format_val.I
                        else:
                            fmt.fmt_value=Format_val.V
                        if not is_num:
                            fmt.fmt_type=Format_type.C
                        else:
                            fmt.fmt_type=Format_type.N


            Fmt.write_catalog(format_catalog,sasfile)

            return ("1")

        except Exception as e:
            return ("0")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010)
#
# arg = [j['crfDecode'], j['crfCodedValue'], j['codedValue'], j['stdCrfCodedValue'], j['stdCrfDecode'], j['decode']]
# if [i for i in arg if i].__len__() >= 1:
#     vals = write_formats(j['crfDecode'], j['crfCodedValue'], j['codedValue'], j['stdCrfCodedValue'], j['stdCrfDecode'],
#                          ['decode'])


