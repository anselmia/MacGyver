class Event():
    
    def __init__(self):
        self.subscribers = []
        
    def subscribe(self, fct):
        self.subscribers.append(fct)
        
    def send(self, **kwargs):
        for subscriber in subscriber:
            subscriber(**kwargs)