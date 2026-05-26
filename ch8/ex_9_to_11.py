# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.
messages = ["hello world", "good morning", "i'll be back"]

def show_messages(messages):
    for message in messages:
        print(message)

show_messages(messages)



# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
def send_messages(messages):
    sent_messages = []

    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

    return sent_messages

print(send_messages(messages))
print(messages)



# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.
messages = ["hello world", "good morning", "i'll be back"]

sent_messages = send_messages(messages[:])
print(messages)
print(sent_messages)