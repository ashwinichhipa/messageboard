class Subscriber:
    def __init__(self, name):
        self.name = name
    def notifyUsers(self, message):
        print('Notification sent to {} with message: "{}"'.format(self.name, message))

class Publisher:
    def __init__(self, events):
        self.events = { event : dict()
                          for event in events }

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'notifyUsers')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def modifyNotification(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'notifyUsers')
        self.get_subscribers(event)[who] = callback

    def notifyAllUsers(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)
            
