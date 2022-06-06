def tower(temp):
    if temp==1:
        return temp
    else:
        return tower(temp-1)*2+1
def towerMovement(temp,p1,p2,p3):
    if temp==1:
        print(p1,"to",p3)
    else:
        towerMovement(temp-1,p1,p3,p2)
        towerMovement(1,p1,p2,p3)
        towerMovement(temp-1,p2,p1,p3)

print(tower(3))
towerMovement(3,1,2,3)
