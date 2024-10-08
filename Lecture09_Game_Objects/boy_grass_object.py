import random
from pico2d import *
from pygame.event import clear
from pygame.examples.cursors import bitmap_cursor1


# Game object class here
class Grass:
    #생성자 함수: 객체의 초기 상태를 측정
    def __init__(self):
        #모양 없는 납작한 붕어빵의 초기 모습을 결정
        self.image = load_image('grass.png')

    def update(self):
        pass
    pass

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')
    def update(self):
        self.y -= random.randint(1,10)
        if self.y< 30:
            self.y = 30
    def draw(self):
        self.image.draw(self.x, self.y)


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')
    def update(self):
        self.y -= random.randint(1,10)
        if self.y< 30:
            self.y = 30
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global boy
    global team
    global smallteam
    global bigteam
    global world

    running =True
    world=[]

    grass = Grass() #잔디를 생성한다(찍어낸다)
    world.append(grass)
    team = [Boy() for i in range(11)]
    smallteam = [SmallBall() for i in range(10)]
    bigteam = [BigBall() for i in range(10)]

running = True


def update_world():
    for o in world : #객체의 상태를 업데이트, 시뮬레이션
        o.update()
    for boy in team:
        boy.update()
    for smallball in smallteam:
        smallball.update()
    for bigball in bigteam:
        bigball.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    for boy in team:
        boy.draw()
    for smallball in smallteam:
        smallball.draw()
    for bigball in bigteam:
        bigball.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()


# game main loop code

while running:
    #game logic
    handle_events()
    update_world() # 상호작용을 시뮬레이션
    render_world() # 그 결과 보여준다
    delay(0.05)

# finalization code

close_canvas()
