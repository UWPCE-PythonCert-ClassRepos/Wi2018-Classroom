from flask import Flask,jsonify,request
import flask
from models.formats import Format, Format_type,Format_val,Parse_Format
from data.setup_data import fmt_dict
from functools import reduce




app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    """
    Entry point to Flask API. Writes .SAS file in response to GET/[analysis id]
    :return: Status of execution as JSON
    """

    if request.method=="GET":

        try:

            # Parse the return data from api into format object
            id = request.args.get('id', 0)
            study= Parse_Format()
            study.read_analysis(id)
            study.read_terms(id)

            format_catalog=[]

            fmts=fmt_dict()

            # for each item in the template dictionary
            for k, v in fmts.items():

                # for each codelist item in the data
                for i in study.terms:

                    # create a format
                    fmt=Format(i['sasFormatName'], i['description'], i['isExtensible'],k,v[2])

                    # for each controlled term in the codelist item
                    ct = i.get('controlledTermItems')

                    if ct.__len__() > 0:

                        # add the item to the codelist
                        for j in ct:
                            a=j[v[0]]
                            b= j[v[1]]
                            if j[v[0]] and j[v[1]]:
                                fmt.add_members(j[v[0]],j[v[1]])

                        # Determine the type of the format item
                        is_label_num = all([num[1].isdigit() for num in fmt.listvals])
                        is_start_num = all([num[0].isdigit() for num in fmt.listvals])

                        fmt.fmt_type=Format_type.Numeric if is_start_num else Format_type.Char
                        fmt.fmt_value=Format_val.Invalue if is_label_num else Format_val.Value

                        # add the format to the catalog
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









