class Subscriber:
    def __init__(self, name):
        self.name = name
        
    def notifyBySMS(self, message):
        print('Sending an SMS to {} : "{}"'.format(self.name, message))

    def notifyByEmail(self, message):
        print('Sending an email to {} : "{}"'.format(self.name, message))

    def notifyByWhatsapp(self, message):
        print('Sending a WhatApp message to {} : "{}"'.format(self.name, message))

class Publisher:
    def __init__(self):
        self.subscribers = dict()
    
    def register(self, who, callback=None):
        if callback == None:
            callback = getattr(who, 'updateByText')

        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def modifyNotification(self, who, callback):
        self.subscribers[who] = callback

    def notifyAllUsers(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message)
