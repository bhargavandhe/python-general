import json

file = open("files/snap_history.json", "r")
data = json.load(file)
dic1, dic2 = {}, {}
for i in range(len(data['Received Snap History'])):
    if data['Received Snap History'][i]['From'] in dic1:
        dic1[data['Received Snap History'][i]['From']] += 1
    else:
        dic1[data['Received Snap History'][i]['From']] = 1

for i in range(len(data['Sent Snap History'])):
    if data['Sent Snap History'][i]['To'] in dic2:
        dic2[data['Sent Snap History'][i]['To']] += 1
    else:
        dic2[data['Sent Snap History'][i]['To']] = 1

for t1 in dic1:
    print(f'{t1} has sent {dic1[t1]} snaps')
print()
for t2 in dic2:
    print(f"I've sent {dic2[t2]} snap to {t2}")
