from AlphaBot import AlphaBot
from signalrcore.hub_connection_builder import HubConnectionBuilder


Ab = AlphaBot()
Ab.stop()

def input_with_default(input_text, default_value):
    value = input(input_text.format(default_value))
    return default_value if value is None or value.strip() == "" else value

def OnMessage(params):
    if (len(params)==2):
        msg = params[1].lower()
    
        if msg=="left" or msg=="l":
            Ab.left()
        elif msg=="rihjt" or msg=="r":
            Ab.right()
        elif msg=="stop" or msg=="s":
            Ab.stop()
        elif msg=="forward" or msg=="f":
            Ab.forward()
        elif msg=="backward" or msg=="b":
            Ab.backward()
        else:
            print(params)
    else:
        print(params)

### server_url = input_with_default('Enter your server url(default: {0}): ', "wss://meirkr.com/chat")
server_url = "ws://meirkr.com/chat"
username = "Alphabot" #input_with_default('Enter your username (default: {0}): ', "python")

hub_connection = HubConnectionBuilder().with_url(server_url).with_automatic_reconnect({
        "type": "raw",
        "keep_alive_interval": 10,
        "reconnect_interval": 5,
        "max_attempts": 5
    }).build()
hub_connection.on("sendToAll", OnMessage)
hub_connection.start()
message = None
# Do login

while message != "exit()":
    message = input(">> ")
    if message is not None and message is not "exit()":
        hub_connection.send("sendToAll", [username, message])
hub_connection.stop()
