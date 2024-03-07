from typing import Dict
class data:

    def __init__(self,id: int, name : str, priceweekdays : Dict[str, float], priceweekend : Dict[str, float], distance : float,percentage : str):

        self.name : float = name
        self.distance : float = distance
        self.price = {
            "weekdays": {
                "little": priceweekdays["little"],
                "big": priceweekdays["big"]
            },
            "weekends": {
                "little": priceweekend["little"],
                "big": priceweekend["big"]
            }
        }
        self.percentage = percentage

    def usespercentage(self):

        if self.percentage == "1":
            return True

        return False

class WrongPasswordError(Exception):
    pass