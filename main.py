import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mob = input("enter number: ")
mob = phonenumbers.parse(mob)

print(timezone.time_zones_for_number(mob))
print(carrier.name_for_number(mob, "en"))
print(geocoder.description_for_number(mob, "en"))
print("Valid Mobile Number: ", phonenumbers.is_valid_number(mob))
print("Checking possbility of number: ", phonenumbers.is_possible_number(mob))