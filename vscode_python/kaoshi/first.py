
import sys
desiredinput=[]
tempinput=[]
location=0
desirednumber=0
if __name__ == "__main__":
    tempinput = sys.stdin.readline().strip()
    desirednumber = sys.stdin.readline().strip()
    print(ans)

print(tempinput)
for i in range(0,len(tempinput)):
    if tempinput[i]!=',':
        desiredinput.append(tempinput[i])
for i in range(0,len(desiredinput)):
    print(desiredinput[i])
print("printlength")
print(len(desiredinput))


def serach(nlist,desired,start,end):
    global location
    if (end-start)%2:#数组有偶数元素
        rightend=int((end-1+start)/2)
        leftstart=int((end-1+start)/2+1)
    else:#数组有奇数元素
        rightend=int((end+start)/2)
        leftstart=int((end+start)/2+1)
    if end-start!=0:
        serach(nlist,desired,leftstart,end)
        if location!=0:
            print(location)
        else:
            serach(nlist,desired,start,rightend)
            if location==0:
                if(nlist[location]!=desired):
                    print('找不到数字')
                else:
                    print(location)

    #print('开始与结束是')
    #print('开始'+str(start)+'结束:'+str(end))
    for i in range (start,end+1):
        #print(nlist[i])
        if nlist[i]==desired and i>=location:
            location=i
    #print('循环结束')
    #print (location)

serach(desiredinput,desirednumber,0,len(desiredinput)-1)


    