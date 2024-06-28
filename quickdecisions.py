attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "big ol speakers" if attendees > 100 else "lil tiny speakers"
projector = "yuge projector" if attendees > 100 else "smol projector"
print("You need a " + venue, "with " + audio_system, "and a " + projector)

veg = input("Would you like vegetarian food? ")
if veg == "yes":
    print("We recommend Veggie Delights Caterers")
else:
    print("We recommend Gourmet Meal Caterers")