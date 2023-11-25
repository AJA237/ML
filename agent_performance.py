class AgentPerformance:
    def __init__(self, period, agent):
        self.t = period
        self.agent = agent
        self.req_all = None
        self.hours = None
        self.shifts = None
        self.completed = None
        self.ratings = None
        
    def requests(self, requests):
        self.req_all = [request for request in requests if self.agent.id == request.agent_id]
        
    def info(self, punctuality_weight):
        for request in self.req_all:
            self.rating += request.rating
            self.hours += request.hours
            self.completed += request.completed
            self.shifts += request.shift
            punctuality = self.punctuality(request=request)
            punctuality_score = punctuality * punctuality_weight
        total_score = self.rating + self.hours + self.completed + self.shifts + punctuality_score
        return total_score
    
    def punctuality(self, request):
        time_dif = request.req_time - request.arrival_time
        if time_dif <= 300:
            return 1
        elif time_dif <= 1800:
            return 0.5
        else:
            return 0