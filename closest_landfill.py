import math

class ClosestLandFill:
    def __init__(self, available_landfill, request):
        self.landfills = available_landfill
        self.request = request
        self.lfs = None
        self.dist = 0

    def get_landfill_loc(self):
        """
    Retrieves the location of each landfill object and stores it in a dictionary.

    Parameters:
    - self: The current instance of the class.

    Returns:
    - landfill_loc: A dictionary containing the location of each landfill object.
    """
        self.lfs = {landfill:landfill.location for landfill in self.landfills}
        return self.lfs
    def get_request_loc(self):
        return self.request.location
    def distance(self):
        # distance between latitudes
        # and longitudes
        for landfill,loc in self.lfs:
            dLat = (self.lfs[landfill][0] - self.request.location[0]) * math.pi / 180.0
            dLon = (self.lfs[landfill][1] - self.request.location[1]) * math.pi / 180.0
        
            # convert to radians
            lat1 = (lat1) * math.pi / 180.0
            lat2 = (lat2) * math.pi / 180.0
        
            # apply formulae
            a = (pow(math.sin(dLat / 2), 2) +
                pow(math.sin(dLon / 2), 2) *
                    math.cos(lat1) * math.cos(lat2));
            rad = 6371
            c = 2 * math.asin(math.sqrt(a))
            return rad * c
    
    def landfill(self):
        return
    