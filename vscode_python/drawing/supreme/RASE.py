from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

width=400
height=400
wordsizeEnglish=20
strChinese="皇家万六学院"
strEnglish="Royal Academy of Software Engineering"
lengthChinese=len(strChinese)
lengthEnglish=len(strEnglish)
wordsizeChinese=wordsizeEnglish*(lengthEnglish*3/4)/lengthChinese
halfsquarewordsizeEnglish=wordsizeEnglish*wordsizeEnglish/2
ppE=halfsquarewordsizeEnglish**0.5
halfsquarewordsizeChinese=wordsizeChinese*wordsizeChinese/2
ppC=halfsquarewordsizeChinese**0.5

FontE=ImageFont.truetype('C:/windows/fonts/arialbi.ttf', round(wordsizeEnglish))
FontC=ImageFont.truetype('C:/windows/fonts/arialbi.ttf', round(wordsizeChinese))
raseArt = Image.new("RGBA",(width,height),"white")
drawwork=ImageDraw.Draw(raseArt)


drawwork.text(((width-ppE*lengthEnglish)/2+ppE*lengthEnglish/4,(height-ppC-ppE)/2),strChinese,(255,69,0),FontC)
drawwork.text(((width-ppE*lengthEnglish)/2,(height-ppC-ppE)/2+ppC),strEnglish,(255,69,0),FontE)

raseArt.show()