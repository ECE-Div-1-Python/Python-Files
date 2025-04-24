class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

w = Weather(["temperature", "humidity", "pressure", "wind", "rainfall"])

print("temperature" in w)
print("snowfall" in w)
