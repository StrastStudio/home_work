class Temperature:
    def __init__(self, celsius):
        self.__Сelsius = celsius

    def ToFahrenheit(self):
        return self.__Сelsius * 9 / 5 + 32

    def GetCelsius(self):
        return self.__Сelsius

temp = Temperature(25)
print(temp.ToFahrenheit())
print(temp.GetCelsius())