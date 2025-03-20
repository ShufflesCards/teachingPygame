# Benjamin Kellman
# 3/13/25
# I am making a class to understand how they work


class Box():
    time = 0
    def __init__ (self, x, y, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        # x pos, y pos, x velocity, y velocity
    
    def __str__(self):
        return f"({self.x}, {self.y})   <{self.dx}, {self.dy}> at {self.time} seconds"
    
    def increaseTime(self, dt):
        self.time+=dt
        self.update(dt)
    
    def update(self, dt):
        self.x += dt*self.dx
        self.y += dt*self.dy

leftMoving = Box(10,0,-1)
rightMoving = Box(0,0,1)
upMoving = Box(0,0,0,1)
downMoving = Box(0,10,0,-1)

leftMoving.increaseTime(1)
print(leftMoving)
rightMoving.increaseTime(1)
print(rightMoving)
upMoving.increaseTime(1)
print(upMoving)
downMoving.increaseTime(1)
print(downMoving)


# class Box():
#     time = 0
#     # describe self as the object, the instance of the class
#     def __init__ (self, x, y, dx=0, dy=0):
#         self.x = x
#         self.y = y
#         self.dx = dx
#         self.dy = dy
#         # x pos, y pos, x velocity, y velocity

#     def __str__(self):
#         return f"({self.x}, {self.y})   <{self.dx}, {self.dy}> at {self.time} seconds"
    
#     def increaseTime(self, dt):
#         self.time+=dt
#         self.update(dt)

#     def update(self, dt):
#         self.x+=dt*self.dx
#         self.y+=dt*self.dy


# thing = Box(1, 2, 2, 4)
# thing.increaseTime(1)
# print(thing)
# thing.increaseTime(1)
# print(thing)
# thing.increaseTime(1)
# print(thing)
