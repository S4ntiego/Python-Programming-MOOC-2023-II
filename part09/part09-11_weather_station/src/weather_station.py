# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        if len(name) < 0:
            raise ValueError("Length of recording cannot be below 0.")
        self.__name = name
        self.__observations = []

    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def latest_observation(self):
        if len(self.__observations) == 0:
            return ""
        else:
            return self.__observations[-1]

    def number_of_observations(self):
        return len(self.__observations)

    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"
