from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

imgDress=Image.open("C:\\Users\\userHu\\Pictures\\Saved Pictures\\sheet1.png")
imgDress=imgDress.resize((500,700), Image.ANTIALIAS)
imgtemp=Image.new("RGBA",(600,1000),"white")
imgtemp.paste(imgDress,(0,50,500,750))
draw=ImageDraw.Draw(imgtemp)
x1=20
x2=80
counter=0
lpantone=['18-3718TPX','11-0601TPX','16-4010TPX','18-3718TPX','15-3807TCX','17-1608 TPX','xx-xxxxTPX']
Fontspecial = ImageFont.truetype('C:/windows/fonts/arialbi.ttf',15)#arialbi,inkfree
lr=[144,255,141,168,173]
lg=[107,255,166,173,162]
lb=[143,255,186,200,180]


for i in range(0,5):
    draw.rectangle((counter+x1,800,counter+x1+x2,825),(lr[i],lg[i],lb[i]),'black')
    draw.text((counter+x1,850),lpantone[i],(65,105,225),Fontspecial)
    counter=counter+x1+x2
imgfinal=Image.new("RGBA",(700,1000),"white")
imgfinal.paste(imgtemp,(100,0,700,1000))
imgfinal.save("C:\\Users\\userHu\\Pictures\\Saved Pictures\\savedsheet.png")




imgfinal.show()