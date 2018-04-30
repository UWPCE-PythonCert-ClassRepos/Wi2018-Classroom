

# Summary
The IPAVe IP Address VisualizEr provides a useful and exciting way to build
predict and visualize current and future IP addres utilization in global IP networks.

- Real world problems.
- Discover IP addressing
- Suggest additional available subnets
- show used IP allocaton
- predict future IP usuage and when to deploy
- provide capacity planning information
- pretty charts and graphs?


### IPAddres Visualizer

### autodiscovery


### Subnet enumeration

Can use:
 - aws cli
 - boto3
 - snmp
 - pexpect

#### If enumerating cloud
- use boto3

#### If enumerating network gear
- snmp
- pexpect cli scraping
- REST API query

### data storage
- initally in flat files/ csv
- can be stored in a SQL database if the support is needed

### Web display
- uses flask
- Initially shows a list of in use IPs and available IPAddres
  - Point and click adds for AWS boto3
  - pexpect integration with a partcular platfrom to add more interfaces and subnets


### IP calcuation
- uses Python subnetting library
- subnets VPC sized defaults (/16's into /22's and /24's)
-

### utilization based prediction
- based on time over usage calculation
  - indicates expected time to have a full subnet (30 day rolling avg)
  - indicates expected time for needing additional subnets in 1 yr.
