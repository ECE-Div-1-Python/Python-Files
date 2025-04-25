class Weather:
    def __init__(self, temp, hmdty, wnd):
        # Store weather parameters in a list
        self.parameters = [temp, hmdty, wnd]

    def __contains__(self, item):
        return item in self.parameters

    def display(self):
        print(f"Weather Parameters - Temperature: {self.parameters[0]}°C, Humidity: {self.parameters[1]}%, Wind Speed: {self.parameters[2]} km/h")

if __name__ == "__main__":
    curr_wea = Weather(25, 80, 15)

    print("Current Weather:")
    curr_wea.display()

    print("\nIs 'Humidity' present in the weather parameters? (80):")
    print(80 in curr_wea)

    print("\nIs 'Rain' present in the weather parameters? ('Rain'):")
    print('Rain' in curr_wea)
