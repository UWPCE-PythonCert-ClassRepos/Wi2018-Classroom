# Enviroment setup

## Coding environment
- use what you have now
- virtualenvs are a good idea

## Network gear
(only set this up if you're working on the network gear portion)
- we'll be using Vyatta as the "hardware" 
- install oracle virtualbox: 
- download VyOs release 1.1.8: [download VyOs](https://downloads.vyos.io/?dir=release/1.1.8)
- install VyOS: [VyOs](https://vyos.io/)

## AWS
(only set this up if you're working on the AWS data pull portion)
- create an aws acccount
- install the aws cli
- install boto3 for your virtual environment

### AWS VPC for data
- VPC will contain the subnet 10.128.0.0/16
- inside the 10.128.0.0/16 VPC subnet:


Add the following IP addresses to the VPC or to the vyatta virtual machine:
-- 10.128.0.0/22
-- 10.128.4.0/22
-- 10.128.8.0/22
-- 10.128.12.0/22
-- 10.128.16.0/22
-- 10.128.128.0/24
-- 10.128.129.0/24
-- 10.128.130.0/24
-- 10.128.131.0/24
-- 10.128.132.0/22


### negative testing addtions / add the conflict IPs
10.128.133.0/24
