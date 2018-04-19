SAS Code and Proc HTTP
-------------------------------
A typical SAS program file in Clinical Programming is a script that creates an output (e.g. descriptive/inferential statistics, figures, data) used support a clinical trial submission.

.. code-block:: SAS
    :caption: Calculate Kaplan-Meier Survial Analysis

    ods output Quartiles=col1;
    ods output CensoredSummary=cen;
    ods output ProductLimitEstimates=risk;

    proc lifetest data=surv method=pl outsurv=km;
       %if (&strat ne ) %then %str(strata &strat;);
       time aval*cnsr(1);
    run;

SAS provides a simple yet powerfull analytical framework, and is not as well suited for app devlopment as other languages. Also, SAS programmers are not typically developers. So the solution is to
extend SAS using other languages.

.. code-block:: SAS
    :caption: Example: SAS call to a Python Application

    filename resp temp;

    proc http url="http://sg6367:8010"
      method="POST"
      ct="application/json"
      AUTH_NEGOTIATE
      in='{"val":"14"}'
      out=resp;
    run;

    libname test JSON fileref=resp;

