from observer import Publisher, Subscriber
from time import sleep

# Method to set notification for user specified channel
def setNotificationChannel(boardObj, subObj):

    channelList = ["sms", "email", "whatsapp"]
    print("Choose a notification channel:")
    print("\t1. SMS")
    print("\t2. Email")
    print("\t3. WhatsApp")

    choice = input("Enter the number of your choice :")

    if choice == '1':
        number = input("Please enter your mobile number: ")
        print("Registering you for this message board . . .")
        boardObj.register(subObj, subObj.notifyBySMS)
    elif choice == '2':
        email = input("Please enter your email address: ")
        print("Registering you for this message board . . .")
        boardObj.register(subObj, subObj.notifyByEmail)
    elif choice == '3':
        whatsapp = input("Please enter your whatapp number: ")
        print("Registering you for this message board . . .")
        boardObj.register(subObj, subObj.notifyByWhatsapp)
    else:
        print("Wrong choice. Existing!!!")
        exit()
    print("\nCongratulations! You have been successfully subscribed to this board.") 

# Method to subscribe and set notifications
def subscribeAndSetNotifications(userid, mboard):
    if mboard == "Public": 
        if userid in publicUserDict.keys():
            print("User and notification channel already exists for this board!")
        else:
            print("\n**Welcome {} to this Public board, you can choose to select the notification channel for all the future messages**\n".format(userid))
            # Create a subscriber object and add an entry to publicUserDict
            subObj = Subscriber(userid)
            publicUserDict[userid] = subObj
            
            # Add notifications for this userid for Public board 
            setNotificationChannel(mPubObj, subObj)
    else:
       if userid in privateUserDict.keys():
            print("User and notification channel already exists for this board!")
       else:
            count=0
            while count < 3:
                password = input('Please enter the password provided to you for this Private board: ')
                if password=="very$ecuRePa$$worD":
                    print("\n**Welcome {}, to this Private board, you can choose to select the notification channel for all the future messages**".format(userid))
                    subObj = Subscriber(userid)
                    privateUserDict[userid] = subObj

                    # Add notifications for this userid for Public board
                    setNotificationChannel(mPriObj, subObj)
                    break
                else:
                    print("Wrong password. Try again?")
                    count += 1
            if count==3:
                print("Wrong password 3 times, exiting...")

# Method to unsubscribe a user from a board
def unsubscribeNotification(userid, mboard):
    # Remove entry from subscribers and users dictionary
    if mboard == "Public":
        if userid in publicUserDict.keys():
            mPubObj.unregister(publicUserDict[userid])
            del publicUserDict[userid]
            print("You have been successfully unsubscribed from the {} Message Board System!".format(mboard))
        else:
           print("You are not subscribed to this board!")
    else: 
        if userid in privateUserDict.keys():
            mPriObj.unregister(privateUserDict[userid])
            del privateUserDict[userid]
            print("You have been successfully unsubscribed from the {} Message Board System!".format(mboard))
        else:
           print("You are not subscribed to this board!")


print("##################################################")
print("## Hello! Welcome to the Message board System.  ##")
print("## We have Public and Private message boards    ##")
print("## available to you, which you can choose to    ##")
print("## subscribe, unsubscribe and make change to    ##")
print("## the notification channel.                    ##")
print("## For every new message posted on these boards ##")
print("## you'll be notified by the channel you choose.##")
print("##################################################")

# Create Publisher objects for both the boards
mPubObj = Publisher()
mPriObj = Publisher()

# Create dictionary of users for both public and private boards
publicUserDict = {}
privateUserDict = {}

print("\n\n####################################################")
print("## Case 1: New User Subscription to Public board. ##")
print("## Username: ashwini                              ##")
print("## Message Board: Public                          ##")
print("####################################################")

username = "ashwini"
messageBoard = "Public" 

# Call the method to subscribe user ashwini to Public board 
subscribeAndSetNotifications(username, messageBoard)

sleep(5)


print("\n\n####################################################")
print("## Case 2: New User Subscription to Private board.##")
print("## Username: chhipa                               ##")
print("## Message Board: Private                         ##")
print("####################################################")

username = "chhipa"
messageBoard = "Private"

# Call the method to subscribe user chhipa to Private board
subscribeAndSetNotifications(username, messageBoard)

sleep(5)


print("\n\n########################################################")
print("## Case 3: Add few more Subscriptions to Public board.##")
print("## Username: alice, bob, vivian, testuser             ##")
print("## Message Board: Public                              ##")
print("########################################################")

usernames = ["alice", "bob", "vivian", "testuser"]
messageBoard = "Public" 

# Call the method to subscribe user each user to Public board
for uname in usernames:
    subscribeAndSetNotifications(uname, messageBoard)

sleep(5)


print("\n\n##########################################################")
print("## Case 4: Notify users for new message on Public board.##")
print("##########################################################")

# Let's first print the Public board subscribers 
print("List of Public Board subscribers : {}".format(list(publicUserDict)))

# Call the method to notify all the subscribed users of Public board
print("\nNotifying all the subscribers...")
mPubObj.notifyAllUsers("A new message has been posted on the Public board.")

sleep(5)


print("\n\n###########################################################")
print("## Case 5: Notify users for new message on Private board.##")
print("###########################################################")

# Let's first print the Private board subscribers
print("List of Private Board subscribers : {}".format(list(privateUserDict)))

# Call the method to notify all the subscribed users of Private board
print("\nNotifying all the subscribers...")
mPriObj.notifyAllUsers("A new message has been posted on the Private board.")

sleep(5)


print("\n\n####################################################")
print("## Case 6: Unsubscribe testuser from Public board.##")
print("## Username: testuser                             ##")
print("## Message Board: Public                          ##")
print("####################################################")

username = "testuser"
messageBoard = "Public"

# Let's first print the Public board subscribers 
print("List of Public Board subscribers : {}".format(list(publicUserDict)))

# Call the method to unsubscribe testuser to Public board
print("\nUnsubscribing {} from {} board...".format(username, messageBoard))
unsubscribeNotification(username, messageBoard)

# Let's first print again the Public board subscribers
print("\nList of Public Board subscribers after  : {}".format(list(publicUserDict)))

sleep(5)


print("\n\n###########################################################")
print("## Case 7: Notify users for new message on Public board. ##")
print("###########################################################")

# Let's first print the Public board subscribers
print("List of Public Board subscribers : {}".format(list(publicUserDict)))

# Call the method to notify all the subscribed users of Public board
print("\nNotifying all the subscribers...")
mPubObj.notifyAllUsers("A new message has been posted on the Public board.")

sleep(5)


print("\n\n###################################################################")
print("## Case 8: Modify notification channel for alice on Public board.##")
print("## Username: alice                                               ##")
print("## Message Board: Public                                         ##")
print("## New channel: Whatsapp                                         ##")
print("###################################################################")

username = "alice"
messageBoard = "Public"

# Call the method to modify notification channel for alice on Public board and set to Whatsapp
print("Modifying notification channel for {} to Whatsapp...".format(username))
mPubObj.modifyNotification(publicUserDict[username], publicUserDict[username].notifyByWhatsapp)
print("Modification done!")

sleep(5)


print("\n\n###########################################################")
print("## Case 9: Notify users for new message on Public board. ##")
print("###########################################################")

# Let's first print the Public board subscribers
print("List of Public Board subscribers : {}".format(list(publicUserDict)))

# Call the method to notify all the subscribed users of Public board
print("\nNotifying all the subscribers...")
mPubObj.notifyAllUsers("Third message has been posted on the Public board.")

sleep(5)
