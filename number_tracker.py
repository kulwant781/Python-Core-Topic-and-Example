import phonenumbers
from phonenumbers import geocoder
from geopy.geocoders import Nominatim

# Enter the phone number with country code
number = "+14155552671"  # Example: US number

# Get location info
parsed_number = phonenumbers.parse(number)
location = geocoder.description_for_number(parsed_number, "en")

# Convert location to coordinates
geolocator = Nominatim(user_agent="geoapiExercises")
location_info = geolocator.geocode(location)

if location_info:
    print(f"Approximate Location: {location}")
    print(f"Coordinates: {location_info.latitude}, {location_info.longitude}")
else:
    print("Location not found!")
