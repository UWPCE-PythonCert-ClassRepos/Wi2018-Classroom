from flask import Flask,jsonify,request
import flask
from models.formats import Format, Format_type,Format_val,Parse_Format
from data.setup_data import fmt_dict




app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    """
    Entry point to Flask API. Writes .SAS file in response to GET/[analysis id]
    :return: Status of execution as JSON
    """

    if request.method=="GET":

        try:

            id = request.args.get('id', 0)
            study= Parse_Format()
            study.read_analysis(id)
            study.read_terms(id)

            format_catalog=[]

            fmts=fmt_dict()

            for k, v in fmts.items():
                for i in study.terms:

                    fmt=Format(i['sasFormatName'], i['description'], i['isExtensible'],k,v[2])

                    ct = i.get('controlledTermItems')

                    if ct.__len__() > 0:
                        # crfDecode,crfCodedValue,codedValue,stdCrfCodedValue,stdCrfDecode

                        for j in ct:
                            a=j[v[0]]
                            b= j[v[1]]
                            if j[v[0]] and j[v[1]]:

                                fmt.add_members(j[v[0]],j[v[1]])

                        format_catalog.append(fmt)



            # Create the .sas file on the network
            fn=Format.write_catalog(format_catalog, study)
            rc={"is_success":True,
                "program":fn}

            return jsonify(rc)

        except Exception as e:

            rc={"is_success":False,
                "error":e.args}
            return jsonify(rc)









