from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
print("Hello, world!")
image = Image.open("C:\\Users\\userHu\\Pictures\\Saved Pictures\\test2_1.png")#没蒙皮的
image=image.convert("RGB")
image.show()
truewidth2=2000#2000/1200
trueheight2=2000#2000/1200
truewidth=1920#1920/1080
trueheight=1920#1920/1080
width, height = image.size
rate=truewidth/width
print(width,height)
r1,g1,b1,front,back,total,lengthcounter,lengthcounter2=0,0,0,0,0,0,0,0#基础数据
pictureLength=90#图片总长度（厘米数
precise=2#精度
k=pictureLength/width
lr,lg,lb=[0],[0],[0]#基础数据
lpixel,ll,lc,lPrintPosition=[],[],[],[]#基础数据
alphabat=['A','A','B','C','D','E','F','G','H','I','J','K','L','M','N']


for i in range(0,width):
    r2,g2,b2=image.getpixel((i,height/2))
    if (r2-precise<=r1<=r2+precise and g2-precise<=g1<=g2+precise and b2-precise<=b1<=b2+precise):
        thingtodo=0
    else:
        front=i
        r,g,b=image.getpixel((i,height/2))
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
k2=90/lengthcounter#厘米数
for i in range(0,len(ll)):
    temp=ll[i]
    ll[i]=round(temp*k2,1)

lengthcounter2=0

for i in range(0,len(ll)):
    lengthcounter2+=ll[i]
print(lengthcounter2)
lPrintPosition.append(0)#以便能全部打印出来（因为for循环只到length-1)




imageOrignal = Image.open("C:\\Users\\userHu\\Pictures\\Saved Pictures\\test1_1.png")#蒙皮的
resized_imageOrignal = imageOrignal.resize((truewidth,trueheight), Image.ANTIALIAS)

wordsize=20#调节字体大小

setFont = ImageFont.truetype('C:/windows/fonts/arial.ttf', wordsize)
Fontwords = ImageFont.truetype('C:/windows/fonts/arial.ttf', 50)
Fontspecial = ImageFont.truetype('C:/windows/fonts/inkfree.ttf', wordsize)#arialbi
imgAxises = Image.new("RGBA",(truewidth2,trueheight2),"white")

draw=ImageDraw.Draw(imgAxises)

linescounter=0

lengthreminder=4*wordsize

yposition=0.17*trueheight2



for i in range(0,len(lPrintPosition)-1):
    if(lPrintPosition[i+1]-lPrintPosition[i])<=1.4*wordsize or (lPrintPosition[i]-lPrintPosition[i-1])<=1.4*wordsize:
        linescounter+=1
        draw.line((0,lPrintPosition[i]+(truewidth2-truewidth)/2,lengthreminder*linescounter,lPrintPosition[i]+(truewidth2-truewidth)/2),(147,112,219))
        draw.text((lengthreminder*linescounter+5,lPrintPosition[i]+(truewidth2-truewidth)/2-wordsize),str(ll[i]),(65,105,225),setFont)
        draw.text((lengthreminder*linescounter+5+2*wordsize,lPrintPosition[i]+(truewidth2-truewidth)/2-wordsize),str(alphabat[lc[i]]),(255,69,0),Fontspecial)
    else:
        linescounter=0
        draw.line((0,lPrintPosition[i]+(truewidth2-truewidth)/2,lengthreminder,lPrintPosition[i]+(truewidth2-truewidth)/2),(147,112,219))
        draw.text((lengthreminder+5,lPrintPosition[i]+(truewidth2-truewidth)/2-15),str(ll[i]),(65,105,225),setFont)
        draw.text((lengthreminder+5+2*wordsize,lPrintPosition[i]+(truewidth2-truewidth)/2-15),str(alphabat[lc[i]]),(255,69,0),Fontspecial)


for i in range(1,len(lr)):
    draw.rectangle((truewidth2-500,yposition,truewidth2-300,yposition+30),(lr[i],lg[i],lb[i]),'black')#300/500
    draw.text((truewidth2-500-2*wordsize,yposition),str(alphabat[i]),(255,69,0),Fontspecial)#300/500
    yposition=yposition+50


draw.text((truewidth-400,10),u'90mm*90mm',(0,0,0),Fontwords)#改变打印出来的厘米数
imageDress= Image.new("RGBA",(truewidth2,trueheight2),"white")
imageDress.paste(resized_imageOrignal,((truewidth2-truewidth),round((truewidth2-truewidth)/2),truewidth2,round((truewidth2-truewidth)/2+trueheight)))
finalWidth=4096#4096/2560
finalHeight=2160#2160/1600


img = Image.new("RGBA",(finalWidth,finalHeight),"white")
img.paste(imgAxises,(finalWidth-truewidth2,round((finalHeight-trueheight2)/2),finalWidth,round(((finalHeight-trueheight2)/2+trueheight2))))
img.paste(imageDress,(finalWidth-2*truewidth2,round((finalHeight-trueheight2)/2),finalWidth-truewidth2,round(((finalHeight-trueheight2)/2+trueheight2))))
img.save("C:\\Users\\userHu\\Pictures\\Saved Pictures\\fixedImage.png")
#resized_image = img.resize((6720,4200), Image.ANTIALIAS)
#resized_image.save("C:\\Users\\userHu\\Pictures\\Saved Pictures\\resizedfixedImage.png")
imDetailed=img.filter(ImageFilter.DETAIL)
imDetailed.save("C:\\Users\\userHu\\Pictures\\Saved Pictures\\detailedfixedImage.png")





