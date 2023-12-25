import sqlite3

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, sender FROM Senders')
senders = {}
for message_row in cur:
    senders[message_row[0]] = message_row[1]

cur.execute('SELECT id, guid, sender_id, subject_id, sent_at FROM Messages')
messages = {}
for message_row in cur:
    messages[message_row[0]] = (message_row[1], message_row[2], message_row[3], message_row[4])

print('Loaded messages', len(messages), 'senders =', len(senders))

send_orgs = {}
for (message_id, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split('@')
    if len(pieces) != 2:
        continue
    dns = pieces[1]
    send_orgs[dns] = send_orgs.get(dns, 0) + 1

orgs = sorted(send_orgs, key=send_orgs.get, reverse=True)
orgs = orgs[:10]
print('Top 10 Organizations')
print(orgs)

counts = {}
years = []
for (message_id, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split('@')
    if len(pieces) != 2:
        continue
    dns = pieces[1]
    if dns not in orgs:
        continue
    year = message[3][:4]

    if year not in years:
        years.append(year)
    key = (year, dns)
    counts[key] = counts.get(key, 0) + 1

years.sort()
print(years)

fhand = open('gline.js', 'w')
fhand.write("gline = [ ['Year'")
for org in orgs:
    fhand.write(",'" + org + "'")
fhand.write("]")

for year in years:
    fhand.write(",\n['" + year + "'")
    for org in orgs:
        key = (year, org)
        val = counts.get(key, 0)
        fhand.write("," + str(val))
    fhand.write("]")

fhand.write("\n];\n")

print('Output written to gline.js')
print('Open gline.htm in a browser to see the visualization')
