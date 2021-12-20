"""BodyTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Body import Body

class BodyTableSeeder(Seeder):
    def run(self):
        Body.create({"name": "Venus", "date_discovered": "2nd millenium bce", "details": "All other planets spin anti-clockwise on their axis and orbit the Sun in an anti-clockwise direction. Venus also orbits the Sun anti-clockwise, but its unusual axis rotation is due to being upside down - it was knocked off its upright position earlier in its history! Astronomers believe that at some point, a colliding celestial body tilted Venus so far off its original position that it is now upside down."})
        Body.create({"name": "Jupiter", "date_discovered":"1610 by Galileo Galilei", "details": "Jupiter's stripes and swirls are actually cold, windy clouds of ammonia and water, floating in an atmosphere of hydrogen and helium. Jupiter’s iconic Great Red Spot is a giant storm bigger than Earth that has raged for hundreds of years."})
        Body.create({"name": "Uranus", "date_discovered": "march 13 1781", "details": "A sidereal day on Uranus (that is, the time it takes for the planet to complete a single oration on its axis) is only about 17 hours long. But the tilt of Uranus is so pronounced that one pole or the other is usually pointed towards the Sun. This means that a day at the north pole of Uranus lasts half of a Uranian year – 84 Earth years"})