import turtle as t
import math 


def cc(v):
    tmp = str(hex(v)).replace("0x","")
    if len(tmp) == 1:
        return "0{}".format(tmp)
    else:
        return tmp

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
def getm(x1,y1,x2,y2):
    if x1 == x2:
        if y1 > y2:
            return 270
        else:
            return 90
    else:
        tmp = math.degrees(math.atan((y1-y2)/(x1-x2)))
        if x1 > x2:
            return tmp + 180
        else:
            return tmp
    
def getcolor(d):
    r = int(d*0.7)
    g = int(d*0.2)
    b = int(d*0.3)
    return "#{}{}{}".format(cc(r),cc(g),cc(b))
    
r = 100
#molt = 240
#mod = 7417
molt = 2
mod = 100
sp = 0
dots = True
step = 360/mod
coors = list()


t.tracer(0, 0)

t.pu()
t.rt(90)
t.fd(r)
t.lt(90)
t.pd()


t.speed(sp)
t.shapesize(1,1,1)
t.color("#FFFFFF")
t.circle(r)

t.pu()

th = 90
while(th > -270):
    c = (r * math.cos(math.radians(th)), r * math.sin(math.radians(th)))
    coors.append(c)
    th -= step
    if dots:
        t.goto(c)
        t.dot(7)
    

map = {}
n = 1
for n in range(1,mod):
    
    if n not in map:
        t.penup()
        t.goto(coors[n])
        t.pendown()
     
    nold = n
    n = n*molt%mod
    
    while nold not in map:
        
        map[nold] = nold
        d = int(dist(t.xcor(), t.ycor(), coors[n][0], coors[n][1]))
        
        #r*2:255=d:x x = d*255/r*2
        
        #print("d:{}".format(d))
        m = getm(t.xcor(), t.ycor(), coors[n][0], coors[n][1])
        #print("m:{}".format(m))
        col = getcolor(int((d*255)/(r*2)))
        #print("col:{}".format(col))
        t.color(col)
        #print()
        t.setheading(m)
        t.goto(coors[n])
        t.stamp()
        n = (n*molt)%mod


wn = t.getscreen()
wn.title("Tesla")
wn.bgcolor("#000000")    
t.update()    
t.done()
