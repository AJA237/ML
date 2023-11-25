clear
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
        
        return
    def landfill(self):
        return
    