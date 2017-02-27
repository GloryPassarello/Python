import sqlite3

conn = sqlite3.connect('mailfromtxt.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname= '/home/gloria/Python_material/code/mbox.txt'
fil = open(fname)
for line in fil:
    if not line.startswith('From ') : continue
    l = line.split()
    word= l[1]
    org_find = word.find('@')
    org= word[org_find +1 :]
    cur.execute('''SELECT count FROM Counts WHERE org=?''', (org, ))
    row=cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES ( ?, 1 )''', (org, ))
    else:
        cur.execute('UPDATE Counts SET count = count+1 WHERE org =?', (org, ))
conn.commit()


cur.close()
