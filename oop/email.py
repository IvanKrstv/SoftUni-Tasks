class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


messages = []
command = input().split()
while command[0] != "Stop":
    send, receive, content = command[0], command[1], command[2]
    email = Email(send, receive, content)
    messages.append(email)

    command = input().split()

indexes = [int(x) for x in input().split(", ")]
for i in range(len(messages)):
    if i in indexes:
        messages[i].send()
    print(messages[i].get_info())
