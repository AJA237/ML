class AgentPerformance:
    def __init__(self, period, agent):
        self.t = period
        self.agent = agent
        self.req_all = None
        self.hours = None
        self.shifts = None
        self.completed = None
        self.ratings = None
        # output
        # - average rating - number of hours laboured - number of complete request - number of shifts - puntuality
    def requests(self, requests):
        self.req_all = [request for request in requests if self.agent.id == request.agent_id]
        
    def info(self):
        for request in self.req_all:
            self.rating += request.rating
            self.hours += request.hours
            self.completed += request.completed
            self.shifts += request.shift
    def punctuality(self):
        for request in self.req_all:
            time_dif = request.req_time - request.arrival