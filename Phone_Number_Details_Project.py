############  Python project to get the details of any phone number  ##############

import phonenumbers
from phonenumbers import carrier, geocoder, timezone

Mobile_Number = input("Enter a mobile number with country code:\n")
Mobile_Number = phonenumbers.parse(Mobile_Number)

################  Get TimeZone for a phone number  #################### 
print(timezone.time_zones_for_number(Mobile_Number))

################ Get the carrier of a phone number  ####################
print(carrier.name_for_number(Mobile_Number, "en"))

####################  Getting information of the region ##################
print(geocoder.description_for_number(Mobile_Number, "en"))

##################  Validating a particular phone number ##################
print("Valid Mobile Number : ", phonenumbers.is_valid_number(Mobile_Number)) 

#################  Checking th possibility of the given phone number ################
print("Checking possibility of the number: ", phonenumbers.is_possible_number(Mobile_Number))
