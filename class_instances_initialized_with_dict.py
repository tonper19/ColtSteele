"""
Initializing instance attributes of a class
using a dictionary
"""
def feet_to_meters(feet):
    """
    convert feet to meters
    """
    return feet * 0.3048

class Airport:
    """
    Airport class
    example on how to use the class' __dict__ to store the object's
    attributes
    """
    attribute_names = ("id", "name", "city", "country", "iata", "icao", "lat"
                       , "long", "alt", "utc_offset", "dst_rule", "tz", "type"
                       , "source")

    def __init__(self, airport_details):
        try:
            assert len(airport_details) == len(Airport.attribute_names)
        except AssertionError:
            raise AssertionError("Incorrect number of Airport attributes")

        self.__dict__.update(dict(zip(Airport.attribute_names
                                      , airport_details)))
        # additional attribute
        self.alt_meters = feet_to_meters(self.alt)

    def __str__(self):
        return f"{self.iata} ({self.name}) is {self.alt_meters} meters high"

def main():
    """
    main method
    create an Airport object sending all its attribute values in a list
    """
    airport = [1474, "Chania International Airport", "Chania", "Greece", "CHQ"
               , "LGSA", 35.531700134277344, 24.149700164794922, 490, 2, "E"
               , "Europe/Athens", "airport", "OurAirports"]
    chania = Airport(airport_details=airport)
    print(chania)

if __name__ == "__main__":
    main()
