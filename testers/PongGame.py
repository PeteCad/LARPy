from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import(
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint



                       
class PongBall(Widget):
    # Velocity of the ball
    vel_x = NumericProperty(0)
    vel_y = NumericProperty(0)
    
    #referencelist property
    #a shorthand like pos for x and y
    
    vel = ReferenceListProperty(vel_x, vel_y)
    
    #move method is current pos + velocity
    
    def move(self):
        self.pos = Vector(*self.vel) + self.pos

class PongPaddle(Widget):
    score = NumericProperty(0)
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speedup=1.1
            offset=0.02 * Vector(0, ball.center_y-self.y)
            ball.vel = speedup * (offset - ball.vel)
        
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    

    def serve_ball(self, velocity=(4,0)):
        self.ball.center=self.center
        self.ball.vel = Vector(velocity).rotate(randint(0,360))
        
    def update(self, dt):
        self.ball.move()
        
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        
        if(self.ball.y <0) or (self.ball.top > self.height):
            self.ball.vel_y *= -1
            
        if self.ball.x <0:
            self.player2.score +=1
            self.serve_ball(velocity=(4,0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(velocity=(-4,0))
            
    def on_touch_move(self,touch):
        if touch.x < self.width /3:
            self.player1.center_y = touch.y
        elif touch.x > self.width *2/3:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

    
if __name__ == '__main__':
    PongApp().run()