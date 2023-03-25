from twilio.rest import Client
import datetime
import pytz

#account sid, auth token and from phone number has been revoked, new can be attained from Twilio.

account_sid = 'ACd08bed167318af5b3f938481eb55177e'
auth_token = 'df2a6ee535f5c1aa7e7ffcf0425950eb'
client = Client(account_sid, auth_token)

# Send a message immediately
#message = client.messages.create(
 #   body="cricket",
  #  from_='+14754656280',
   # to='+put a phone number',
#)
#print(message.sid)

# Schedule the message to be sent at 21:09 PM every day

uk_time = pytz.timezone('Europe/London') # Set the timezone to UK time
now = datetime.datetime.now(uk_time)
send_time = datetime.datetime(now.year, now.month, now.day, 21, 42, 0, tzinfo=uk_time) # Set the time to 9:42 PM UK time
send_time_str = send_time.astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

# Schedule the message to be sent at 9:42 PM UK time
message = client.messages.create(
    body="Hello",
    messaging_service_sid='SMb89ebdeab04f3a99c7ff5ef77de7446e',
    to='+put a phone number',
    send_at=send_time_str
)

print(message.sid)

