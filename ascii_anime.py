from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.particles import RingFirework,Rocket,SerpentFirework,StarFirework,ExplosionFlames
from asciimatics.renderers import FigletText, ImageFile

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("50th anniversary of APOLLO 11", font='big'),
            screen.height // 2 - 8),

        
        Stars(screen, (screen.width + screen.height) // 2),
        RingFirework(screen,10,10,50),
        StarFirework(screen,40,8,50),
        RingFirework(screen,70,12,50),
        RingFirework(screen,100,10,50),
        StarFirework(screen,130,8,50),
        RingFirework(screen,160,12,50)
    ]
    screen.play([Scene(effects, 100)],ExplosionFlames(screen,44,20,100))
    

Screen.wrapper(demo)