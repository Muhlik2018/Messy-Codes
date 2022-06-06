import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter




image = Image.open("sample2.png")
imDetailed=image.filter(ImageFilter.DETAIL)
imDetailed.save("result2.png")


