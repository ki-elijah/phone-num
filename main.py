import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mob = input("enter number: ")
mob = phonenumbers.parse(mob)
