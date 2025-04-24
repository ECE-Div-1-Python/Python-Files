# 7.	Create a class Weather that has a list containing weather parameters. Define an overloaded in operator that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.)


class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

weather = Weather(["Rain", "Humidity", "Wind"])
print("Rain in Weather:", "Rain" in weather)
print("Snow in Weather:", "Snow" in weather)