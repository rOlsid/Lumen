# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AC851cdc148416c23c734d1dadaa565374"
auth_token = "bdba3a98e99f7093408ba4b05ba57344"
client = Client(account_sid, auth_token)

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+355683090136",
  from_="+13203728331"
)

print(call.sid)