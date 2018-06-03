Python 220 Project: Keezer Management

Purpose:

Keep track of my beer fridge.

Measurement
 - temperature
 - weight of components
  - CO2/beer gas tanks
  - kegs

Display
 - LCD screen

Alert
 - send email when thresholds are reached
  - tanks or kegs low
  - temperature too high or low

Retention
 - store values for analysis
  - graphing
  - consumption projection


Design:

The application will run on a small device such as a raspberry pi.  Sensors connected via USB and/or GPIO inside the fridge will feed data to the application.  External displays connected via USB or HDMI will provide output.  Data will be logged over the network to a data sink, likely SQL but possibly an snmp trap sink.

Classes:
 - Driver
  - Main application logic
  - Scheduling

 - Sensor
  - Define interface for concrete sensor subclasses
 
 - Display
  - Accept sensor data
  - Concrete subclasses will display or export data


Deliverables:

The initial implementation of the keezer project will use flat text files for input and output using simple concrete subclasses.  Subsequent iterations will add additional subclasses for actual devices, protocols, etc.
