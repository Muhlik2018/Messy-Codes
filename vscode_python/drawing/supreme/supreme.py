from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter




wordsize=20
wordsize2=20
str1='Complied'
str2='successfully'
number=len(str1)
halfsquarewordsize=wordsize*wordsize/2
printposition=halfsquarewordsize**0.5
print(printposition)
width=720
height=1280



img = Image.new("RGBA",(width,height),"white")

for i in range(0,width):
    for j in range(0,height):
        img.putpixel((i,j),(253,245,230))
#for j in range(0,height):
    #img.putpixel((round(width/2),j),(255,255,255))


Fontspecial = ImageFont.truetype('C:/windows/fonts/arialbi.ttf', wordsize)#simfang arialbi
draw=ImageDraw.Draw(img)

printwidth,printheight= draw.textsize(str1,font=Fontspecial)
draw.text(((width-printwidth)/2,(height-printheight)/2-20),str1,(

47,79,79),Fontspecial)#248,248,255
printwidth2,printheight2= draw.textsize(str2,font=Fontspecial)#7,113,223 248,248,255
draw.text(((width-printwidth2)/2,(height-printheight2)/2+printheight),str2,(

47,79,79),Fontspecial)



img.save("C:\\Users\\userHu\\Documents\\学校材料\\testpictures\\square.png")
img.show()


#for i in range(0,int(height/20)+1):
    #for j in range(0,int(width/20)+1):
        #draw.text((j*printposition*number+2*printposition+i*20,1.5*i*printposition),str1,(255,69,0),Fontspecial)
#imgnew=img.crop((width/2,printposition,width,height/2))
#img.save("C:\\Users\\userHu\\Documents\\学校材料\\testpictures\\desinger.png")
#imgnew.save("C:\\Users\\userHu\\Documents\\学校材料\\testpictures\\croped.png")
#imgnew.show()