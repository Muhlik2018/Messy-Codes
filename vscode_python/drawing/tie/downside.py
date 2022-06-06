from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
print("Hello, world!")
image = Image.open("C:\\Users\\userHu\\Pictures\\Saved Pictures\\test1_1.png")#条纹图
image=image.convert("RGB")
image.show()
truewidth2=2000#2000/1200
trueheight2=2000#2000/1200
truewidth=1800#1920/1080
trueheight=1200#1920/1080
width, height = image.size
rate=trueheight/height
print(width,height)
r1,g1,b1,front,back,total,lengthcounter,lengthcounter2=0,0,0,0,0,0,0,0#基础数据
pictureLength=40#图片总长度（厘米数
precise=2#精度
wordsize=40#调节字体大小
k=pictureLength/height
lr,lg,lb=[0],[0],[0]#基础数据
lpixel,ll,lc,lPrintPosition=[],[],[],[]#基础数据
alphabat=['A','A','B','C','D','E','F','G','H','I','J','K','L','M','N']#以ABCDEFG标注颜色
lpantone=["default",'19-1526 TCX','12-0813 TCX','19-4029 TCX','18-1442 TCX','14-2305 TCX','15-1145 TPX','xx-xxxxTPX'] #色卡序号，default和xx不打印，用于检查是否出错


for i in range(0,height):
    r2,g2,b2=image.getpixel((width*1/100,i))
    if (r2-precise<=r1<=r2+precise and g2-precise<=g1<=g2+precise and b2-precise<=b1<=b2+precise):
        thingtodo=0
    else:
        front=i
        r,g,b=image.getpixel((width/2,i))
        r1=r2
        g1=g2
        b1=b2
        length=front-back
        for j in range(0,len(lr)):
            if(lr[j]-precise<=r<=lr[j]+precise and lg[j]-precise<=g<=lg[j]+precise and lb[j]-precise<=b<=lb[j]+precise):
                lc.append(j)
                break
            elif j==len(lr)-1:
                lr.append(r)
                lg.append(g)
                lb.append(b)
                lc.append(j+1)
        total+=length
        back=front
        reallength=round(length*k,1)
        ll.append(reallength)
        lpixel.append(round(length*rate,1))


total+=height-front

ll.pop(0)
lpixel.pop(0)

ll.append(round(((height-front)*k),1))
lpixel.append(round((height-front)*rate,1))#去除空值并添加新值


for i in range(0,len(lpixel)):
    temp=0
    if i==0:
        lPrintPosition.append(lpixel[i]/2)
    else:
        for j in range(0,i):
            temp+=lpixel[j]
        lPrintPosition.append((lpixel[i]/2)+temp)



for i in range(0,len(ll)):
    lengthcounter+=ll[i]
k2=pictureLength/lengthcounter#厘米数
for i in range(0,len(ll)):
    temp=ll[i]
    ll[i]=round(temp*k2,1)

lengthcounter2=0

for i in range(0,len(ll)):
    lengthcounter2+=ll[i]
print(lengthcounter2)
lPrintPosition.append(0)#以便能全部打印出来（因为for循环只到length-1)




imageOrignal = Image.open("C:\\Users\\userHu\\Pictures\\Saved Pictures\\test1_1.png")#蒙版图
resized_imageOrignal = imageOrignal.resize((truewidth,trueheight), Image.ANTIALIAS)

wsp=40#word size Pantone

setFont = ImageFont.truetype('C:/windows/fonts/arial.ttf', wordsize)
Fontwords = ImageFont.truetype('C:/windows/fonts/arial.ttf', 80)
Fontspecial = ImageFont.truetype('C:/windows/fonts/arialbi.ttf', wordsize)#arialbi,inkfree
FontPantone = ImageFont.truetype('C:/windows/fonts/arialbi.ttf', wsp)
imgAxises = Image.new("RGBA",(truewidth2,trueheight2),"white")

draw=ImageDraw.Draw(imgAxises)

linescounter=0

lengthreminder=4*wordsize

yposition=0.1*trueheight2#0.17



for i in range(0,len(lPrintPosition)-1):
    if(ll[i]>0.1):
        if(lPrintPosition[i+1]-lPrintPosition[i])<=wordsize or (lPrintPosition[i]-lPrintPosition[i-1])<=wordsize:#1.4*wordsize
            linescounter+=1
            draw.line((0,lPrintPosition[i]+(trueheight2-trueheight)/2,lengthreminder*linescounter,lPrintPosition[i]+(trueheight2-trueheight)/2),(147,112,219))
            draw.text((lengthreminder*linescounter+5,lPrintPosition[i]+(trueheight2-trueheight)/2-wordsize),str(ll[i]),(65,105,225),setFont)
        #if alphabat[lc[i]]=='G':
            #alphabat[lc[i]]='F'
            draw.text((lengthreminder*linescounter+5+2*wordsize,lPrintPosition[i]+(trueheight2-trueheight)/2-wordsize),str(alphabat[lc[i]]),(255,69,0),Fontspecial)
        else:
            linescounter=0
            draw.line((0,lPrintPosition[i]+(trueheight2-trueheight)/2,lengthreminder,lPrintPosition[i]+(trueheight2-trueheight)/2),(147,112,219))
            draw.text((lengthreminder+5,lPrintPosition[i]+(trueheight2-trueheight)/2-wordsize),str(ll[i]),(65,105,225),setFont)
        #if alphabat[lc[i]]=='G':
            #alphabat[lc[i]]='F'
            draw.text((lengthreminder+5+2*wordsize,lPrintPosition[i]+(trueheight2-trueheight)/2-wordsize),str(alphabat[lc[i]]),(255,69,0),Fontspecial)

#for i in range(1,len(lr)):
    #draw.rectangle((truewidth2-700,yposition,truewidth2-500,yposition+90),(lr[i],lg[i],lb[i]),'black')#300/500
    #print(lr[i],lg[i],lb[i])#300/500#需要知道RGB值时使用
    #draw.text((truewidth2-700-2*wsp,yposition),str(alphabat[i]),(255,69,0),FontPantone)
    #if i!=1:#有白色时使用
    #draw.text((truewidth2-500+wsp,yposition-wsp/4),"PANTONE",(65,105,225),FontPantone)#打印色卡号的代码，平时注释掉
    #draw.text((truewidth2-500+wsp/2,yposition+wsp*3/4),lpantone[i],(65,105,225),FontPantone)
    #yposition=yposition+150


draw.text((truewidth-500,10),u'60mm*40mm',(0,0,0),Fontwords)#改变打印出来的厘米数
imageDress= Image.new("RGBA",(truewidth2,trueheight2),"white")
imageDress.paste(resized_imageOrignal,((truewidth2-truewidth),round((trueheight2-trueheight)/2),truewidth2,round((trueheight2-trueheight)/2+trueheight)))
finalWidth=4096#4096/2560
cpHeight=500#color place height

finalHeight=2160+cpHeight#2160/1600

upperHeight=finalHeight-cpHeight


img = Image.new("RGBA",(finalWidth,finalHeight),"white")
img.paste(imgAxises,(finalWidth-truewidth2,round((upperHeight-trueheight2)/2),finalWidth,round(((upperHeight-trueheight2)/2+trueheight2))))
img.paste(imageDress,(finalWidth-2*truewidth2,round((upperHeight-trueheight2)/2),finalWidth-truewidth2,round(((upperHeight-trueheight2)/2+trueheight2))))


draw2=ImageDraw.Draw(img)
xposition=150


for i in range(1,len(lr)):
    #if i<=6:
    draw2.rectangle((xposition,2160,xposition+300,2160+180),(lr[i],lg[i],lb[i]),'black')#300/500
    #print(lr[i],lg[i],lb[i])#300/500#需要知道RGB值时使用
    draw2.text((xposition-2*wsp,2160+80),str(alphabat[i]),(255,69,0),FontPantone)
    #if i!=3:#有白色时使用
    #draw2.text((xposition,180+2160+0.5*wsp),"PANTONE",(65,105,225),FontPantone)#打印色卡号的代码，平时注释掉
    #draw2.text((xposition,180+2160+1.5*wsp),lpantone[i],(65,105,225),FontPantone)
    xposition=xposition+600











#数格距直接发条纹图蒙版图png和单循环大小就好了


img.save("C:\\Users\\userHu\\Pictures\\Saved Pictures\\fixedImage.png")
img.show()
#resized_image = img.resize((6720,4200), Image.ANTIALIAS)#没用的代码
#resized_image.save("C:\\Users\\userHu\\Pictures\\Saved Pictures\\resizedfixedImage.png")
imDetailed=img.filter(ImageFilter.DETAIL)
imDetailed.save("C:\\Users\\userHu\\Pictures\\Saved Pictures\\detailedfixedImage.png")







