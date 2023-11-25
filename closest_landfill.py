clear
class ClosestLandFill:
    def __init__(self, available_landfill, request):
        self.landfills = available_landfill
        self.request = request
        self.lf = None
        self.dist = 0

    def get_landfill_loc(self):
        """
    Retrieves the location of each landfill object and stores it in a dictionary.

    Parameters:
    - self: The current instance of the class.

    Returns:
    - landfill_loc: A dictionary containing the location of each landfill object.
    """
        landfill_loc = {landfill:landfill.location for landfill in self.landfills}
        return landfill_loc
    def get_request_loc(self):
        return self.request.location
    def distance(self):

        return
    def landfill(self):
        return
    