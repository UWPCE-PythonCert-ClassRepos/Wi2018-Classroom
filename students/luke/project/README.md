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
  - Display pounds of CO2 remaining
  - Display gallons of beer remaining per keg

Alert
 - send email when thresholds are reached
  - tanks or kegs low
  - temperature too high or low

Retention
 - store values for analysis
  - graphing
  - consumption projection




Use case 1:
Exhaust CO2 cannister, swap with a fresh one, verify refill on LCD.
1. LCD reads 0 pounds CO2 remaining.
2. Open keezer, disconnect CO2 lines, remove tank and regulator
3. LCD reads negative value (tare weight of tank and regulator)
4. Move regulator to new tank, reconnect lines, place in keezer
5. LCD reads approximately 5 pounds CO2 remaining

Use case 2:
Serve a dozen beers.
1. LCD reads 2 gallons remaining
2. Dispense beers
3. LCD reads 0.5 gallons remaining
4. Email alert received warning of imminent keg pop


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
