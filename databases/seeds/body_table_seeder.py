"""BodyTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Body import Body

class BodyTableSeeder(Seeder):
    def run(self):
        Body.create({"name": "Venus", "date_discovered": "2nd millenium bce", "details": "Venus also orbits the Sun anti-clockwise, but its unusual axis rotation is due to being upside down.Astronomers believe that at some point, a colliding celestial body tilted Venus so far off its original position that it is now upside down."})
        Body.create({"name": "Jupiter", "date_discovered":"1610 by Galileo Galilei", "details": "Jupiter's stripes and swirls are actually cold, windy clouds of ammonia and water, floating in an atmosphere of hydrogen and helium."})
        Body.create({"name": "Uranus", "date_discovered": "march 13 1781", "details": " the tilt of Uranus is so pronounced that one pole or the other is usually pointed towards the Sun. This means that a day at the north pole of Uranus lasts half of a Uranian year – 84 Earth years" })