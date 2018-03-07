Report Distribution Utility
---------------------------------
Python Flask application that runs as a service responding to POST requests. When the application recieves a valid request, the application will:

    * Retrieve the report details from the SQL Server database
    * Identify the files to include in the report using the output location and regex pattern defined in the database
    * Create a zip archive of those files
    * Distribute an email message from the attributes defined in the database (e.g. to, from , subject, body) with the zip file attached

Application Architecture
++++++++++++++++++++++++++++++++++++

  .. image:: /_static/mailer.png
