frnd_name = input("Enter friend name: ")
file = open(f"files/chat-{frnd_name}.txt", "r")

ls = []
dic = {}
me, frnd = 0, 0
my_name = 'bhargav'

for line in file.readlines():
    if line.lower().__contains__(my_name):
        me += 1
    if line.lower().__contains__(frnd_name):
        frnd += 1

    words = line.split()
    for word in words:
        if word.lower() in dic:
            dic[word.lower()] += 1
        else:
            dic[word.lower()] = 1

for item in dic.keys():
    print(f'{item} : {dic[item]}')

print(f'{my_name} has sent {me} messages')
print(f'{frnd_name} has sent {frnd} messages')
print(f'Found {len(dic)} unique words!')
