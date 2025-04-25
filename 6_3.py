class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()
        self.conversions = {
            'inches': 1,
            'feet': 12,
            'yards': 36,
            'miles': 63360,
            'kilometers': 39370.1,
            'meters': 39.3701,
            'centimeters': 2.54,
            'millimeters': 25.4
        }
    def _convert(self, target_unit):
        if self.unit in self.conversions and target_unit in self.conversions:
            conversion_factor = self.conversions[target_unit] / self.conversions[self.unit]
            return self.length * conversion_factor
        else:
            raise ValueError("Invalid unit provided.")
    def inches(self):
        return self._convert('inches')
    def feet(self):
        return self._convert('feet')
    def yards(self):
        return self._convert('yards')
    def miles(self):
        return self._convert('miles')
    def kilometers(self):
        return self._convert('kilometers')
    def meters(self):
        return self._convert('meters')
    def centimeters(self):
        return self._convert('centimeters')
    def millimeters(self):
        return self._convert('millimeters')
while True:
    n = float(input("Give the length: "))
    unit = input("Give the current unit: ").lower()
    c = Converter(n, unit)
    if unit in c.conversions:
        print(f"{n} {unit} in feet: {c.feet()}")
        print(f"{n} {unit} in inches: {c.inches()}")
        print(f"{n} {unit} in yards: {c.yards()}")
        print(f"{n} {unit} in miles: {c.miles()}")
        print(f"{n} {unit} in kilometers: {c.kilometers()}")
        print(f"{n} {unit} in meters: {c.meters()}")
        print(f"{n} {unit} in centimeters: {c.centimeters()}")
        print(f"{n} {unit} in millimeters: {c.millimeters()}")
    else:
        print("Please enter a valid unit")
    stop = input("If you want to exit, type 'STOP', else press anything to continue: ")
    if stop.upper() == "STOP":
        break