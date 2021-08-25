class SpaceAge:
    earth_year_in_seconds = 31557600
    earth_year_conversions = {"Earth":   1,
                              "Mercury": 0.2408467,
                              "Venus":   0.61519726,
                              "Mars":    1.8808158,
                              "Jupiter": 11.862615,
                              "Saturn":  29.447498,
                              "Uranus":  84.016846,
                              "Neptune": 164.79132}

    def __init__(self, seconds):
        self.seconds = seconds

    def conversion(self, location):
        return round(self.seconds/self.earth_year_in_seconds \
                     /self.earth_year_conversions[location], 2)

    def on_earth(self):
        return self.conversion("Earth")

    def on_mercury(self):
        return self.conversion("Mercury")

    def on_venus(self):
        return self.conversion("Venus")

    def on_mars(self):
        return self.conversion("Mars")

    def on_jupiter(self):
        return self.conversion("Jupiter")

    def on_saturn(self):
        return self.conversion("Saturn")

    def on_uranus(self):
        return self.conversion("Uranus")

    def on_neptune(self):
        return self.conversion("Neptune")
