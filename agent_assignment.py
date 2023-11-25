import math


class AgentAssign:
    def __init__(self, request, agents_list):
        self.request = request
        self.agents = agents_list
        self.agent = None
    def closest_agent(self):
        return self.agent
    def distance(self):
        """
        Calculates the distance between the current location and the closest landfill.

        The code iterates through each landfill and calculates the distance using the haversine formula. It then updates the 'dist' variable with the minimum distance found.

        """
        # distance between latitudes
        # and longitudes
        for agent in self.agents:
            dLat = (self.agents[agent.index][0] - self.request.location[0]) * math.pi / 180.0
            dLon = (self.agents[agent.index][1] - self.request.location[1]) * math.pi / 180.0
        
            # convert to radians
            lat1 = (self.request.location[0]) * math.pi / 180.0
            lat2 = (self.agents[agent][0]) * math.pi / 180.0
        
            # apply formulae
            a = (pow(math.sin(dLat / 2), 2) +
                pow(math.sin(dLon / 2), 2) *
                    math.cos(lat1) * math.cos(lat2));
            rad = 6371
            c = 2 * math.asin(math.sqrt(a))
            distance = rad * c
            if distance < self.dist:
                self.dist = distance
                self.agent = self.agents[agent]
    def run(self):
        if self.request.volume < 160:
            return self.agents
        else:
            self.distance()
            print(self.closest_agent())

