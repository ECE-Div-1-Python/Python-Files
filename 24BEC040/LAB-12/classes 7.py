class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

weather = Weather(["Rain", "Humidity", "Wind"])
print("Rain in Weather:", "Rain" in weather)
print("Snow in Weather:", "Snow" in weather)