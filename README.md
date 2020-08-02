# Message Board System using Python's Observer Behavioural Pattern

Using Python to show how the observer behavioural pattern can be used to implement a dummy message board system.


### Setup
 ```
 python version : 3.7.6
 OS tested  : MacOS
```

``` 
 git clone https://github.com/ashwinichhipa/messageboard.git
 cd messageboard
```

### Applications:
1. User can subscribe to the public board 
2. User can subscribe to the private board (needs password to subscribe the private board)
3. User can choose the notification channel from SMS, Email, Whatsapp
4. Notification sent to users for new message on Public board
5. Notification sent to users for new message on Private board
6. Unsubscribe a user from a board
7. Modify the notification channel for a user for a board*
8. Output has been printed for each case
9. Basic testing is done on user input 

### To run it:

```
 python3 messageboarddriver.py
```

### Assumptions:
1. No external communication is done, all are assumed.
2. User interaction is needed for selection of notification channel and entering password for private board (which can then be hard-corded)
3. Message posting on public/private board is not taken care of here
4. Password to access private board is : "password"
5. Notification channels are dummy and only a message is printed on screen stating user has been notified by X channel
 
### Enhancements:
1. Better unit tests
2. More user interaction for each cases
