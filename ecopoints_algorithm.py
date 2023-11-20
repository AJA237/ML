import inspect


levels = ["entry", "silver", "gold", "diamond"]

class EcoPoint:
    def __init__(self, rate=100):
        self.service = None
        self.pts = 0
        self.level = 0
        self.rate = rate

    def convert(self, price):
        n_ecopt = price / self.rate
        n_ecopt = round(n_ecopt)
        self.pts = n_ecopt
        return self.pts

    def lvl_check(self):
        """Check the level of the account"""
        if self.pts < 1000:
            self.level = 0
        elif self.pts < 5000:
            self.level = 1
        elif self.pts < 10000:
            self.level = 2
        else:
            self.level = 3
        return self.level

    def redeem(self, service):
        """Redeem reward"""
        if service == "voice":
            base = 10
        elif service == "data":
            base = 5
        elif service == "electricity":
            base = 20
        else:
            return "Invalid service"

        reward = self.pts // (base * self.level)
        self.pts -= reward
        self.level = self.lvl_check()
        return reward, self.level, self.pts


ecopoint = EcoPoint()
print(ecopoint.convert(15000000))
print(ecopoint.lvl_check())
print(ecopoint.redeem("electricity"))