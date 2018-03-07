from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8e887e8e8296aa59c3e1d5715c110792"
# Your Auth Token from twilio.com/console
auth_token = "c44c40d935396b87d1037e56314a8ac0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+2348038910635",
    from_="+16698004905",
    body="Hello from Python!")

print(message.sid)
