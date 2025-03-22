import os
from time import sleep
f = open('exemplo.text','a')
f.write("Crazy? I was crazy once, they locked me in a room, a rubber room, a rubber room filled with rats, and rats make me crazy\n")
f.write("Crazy? I was craazy once, they locked me in a room, a rubber room, a rubber room filled with rats, and rats make me crazy\n")
f.write("Crazy? I was craaazy once, they locked me in a room, a rubber room, a rubber room filled with rats, and rats make me crazy\n")
f.write("Crazy? I was craaaazy once, they locked me in a room, a rubber room, a rubber room filled with rats, and rats make me crazy\n")

f = open('exemplo.text','r')
content = f.read()
print(content)
os.remove('exemplo.text')
f.close()