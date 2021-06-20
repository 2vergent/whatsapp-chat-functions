name = input("Enter name of chat text file: ")
name = name.strip()
name = name + ".txt"
print("\n")

sender_name = input("Enter sender name as in chat file: ")
sender_name = sender_name.strip()

receiver_name = input("Enter receiver name as in chat file: ")
receiver_name = receiver_name.strip()

searchstr = input("Enter the search string: ")
print("\n")

chat = open(name,"r")
texts = chat.readlines()
sender = []
receiver = []


for x in texts:
    pos = x.find('-')
    texts = x[pos + 2: len(x) - 1]
    if(texts[0:7] == sender_name):
        sender.append(texts[len(sender_name) + 2:])
    else:
        receiver.append(texts[len(receiver_name) + 2: ])

count = 0
for x in sender:
    if x.__contains__(searchstr):
        count += 1

print("The sender has sent this string:", count, "times")
count = 0

for x in receiver:
    if x.__contains__(searchstr):
        count += 1

print("The receiver has sent this string:", count, "times")