"""
26

Kuopio Birdwatchers needs a new monitoring database software. Your task is to implement class Observation.

class Observation contains following properties:
- species               - string
- number_of_birds       - integer (set 0 if <0)
- observation_time      - datetime
- position              - string
- additional_info       - string

The class contains a constructor, which sets values of all data members of the class.

Create getters and setters for each data members. Each getter prints message "getter", and each setter prints message "setter".

Implement __str__ method. The method outputs string containing class data fields space separated. For example string "crow 32 31.01.2020 Savilahti 'Wind, north 5m/s'" is created with following data:
- species="crow"
- number_of_birds=32
- observation_time=31st Janyary 2020
- position="Savilahti"
- additional_information="Wind, north 5m/s"

There are no requirements for the main program. You can, for example, create a test software to test functionality of the class.



"""

from datetime import datetime

class Observation:
    def __init__(self, species, number_of_birds, observation_time, position, additional_info):
        self._species = species
        self._number_of_birds = max(0, number_of_birds)  # Set to 0 if < 0
        self._observation_time = observation_time
        self._position = position
        self._additional_info = additional_info

    # Getter and setter for species
    @property
    def species(self):
        print("getter")
        return self._species

    @species.setter
    def species(self, value):
        print("setter")
        self._species = value

    # Getter and setter for number_of_birds
    @property
    def number_of_birds(self):
        print("getter")
        return self._number_of_birds

    @number_of_birds.setter
    def number_of_birds(self, value):
        print("setter")
        self._number_of_birds = max(0, value)  # Set to 0 if < 0

    # Getter and setter for observation_time
    @property
    def observation_time(self):
        print("getter")
        return self._observation_time

    @observation_time.setter
    def observation_time(self, value):
        print("setter")
        self._observation_time = value

    # Getter and setter for position
    @property
    def position(self):
        print("getter")
        return self._position

    @position.setter
    def position(self, value):
        print("setter")
        self._position = value

    # Getter and setter for additional_info
    @property
    def additional_info(self):
        print("getter")
        return self._additional_info

    @additional_info.setter
    def additional_info(self, value):
        print("setter")
        self._additional_info = value

    def __str__(self):
        return f"{self.species} {self.number_of_birds} {self.observation_time.strftime('%d.%m.%Y')} {self.position} '{self.additional_info}'"

# Test program
if __name__ == "__main__":
    observation = Observation(
        species="crow",
        number_of_birds=32,
        observation_time=datetime(2020, 1, 31),
        position="Savilahti",
        additional_info="Wind, north 5m/s"
    )

    print(observation)  # Test __str__ method

    # Test getters and setters
    print(observation.species)  # getter
    observation.species = "sparrow"  # setter
    print(observation.species)  # getter

    print(observation.number_of_birds)  # getter
    observation.number_of_birds = -5  # setter (should set to 0)
    print(observation.number_of_birds)  # getter

































#Write class and imports here!

# if __name__ == "__main__":
#     #Write main program below this line
