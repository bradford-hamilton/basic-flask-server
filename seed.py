from models import Songs
from app import db

song1 = Songs('Divided Sky', 'Phish', 1989)
song2 = Songs('Brokedown Palace', 'Grateful Dead', 1971)
song3 = Songs('Take Five', 'Dave Brubeck', 1954)

db.session.add(song1)
db.session.add(song2)
db.session.add(song3)

db.session.commit()
