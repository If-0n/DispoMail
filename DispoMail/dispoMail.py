from mailtm import Email
import colorama
from colorama import Fore, Back

print("________  .__                         _____         .__.__  ")
print("\______ \ |__| ____________   ____   /     \ _____  |__|  |  ")
print(" |    |  \|  |/  ___/\____ \ /  _ \ /  \ /  \\__  \ |  |  |  ")
print(" |    `   \  |\___ \ |  |_> >  <_> )    Y    \/ __ \|  |  |__")
print("/_______  /__/____  >|   __/ \____/\____|__  (____  /__|____/")
print("        \/        \/ |__|                  \/     \/         ")

def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])

# Get Domains
test = Email()
print("\nDomain: " + test.domain)

# Make new email address
test.register()
print("\nEmail Adress: " + str(test.address))

# Start listening
test.start(listener, interval=4)
print("\nWaiting for an email...")