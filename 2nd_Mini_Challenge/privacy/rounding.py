import math

class Rounding:

    def rounding_age(self, data):

        # round down and concatenate string
        data = int(math.floor(int(data) / 10.0)) * 10
        data = str(data) + '세'
        return data