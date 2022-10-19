from PIL import ImageFont, ImageDraw, Image  
#import cv2
#import numpy as np
#import datetime
#import os
#import copy
#import time
#import sys
import argparse
parser = argparse.ArgumentParser(description='text2image')
parser.add_argument("-t", "--text", type=str, help="Text", default="I love you, Mom", dest='text')
parser.add_argument("-p", "--picture", type=str, help="picture name", default="temp1.jpg", dest='fyl')
parser.add_argument("-x", "--xx", type=int, help="x coordinate", default=100, dest="xcoord")
parser.add_argument("-y", "--yy", type=int, help="y coordinate", default=100, dest="ycoord")
parser.add_argument("-s", "--size", type=int, help="font size", default=16, dest="size")
parser.add_argument("-f", "--font", type=str, help="font name (and path)", default=None, dest="font")
#parser.add_argument("-c", "--color", nargs=3, type=int, help="Font color (R G B)",default=(0,0,0), dest="color")
parser.add_argument("-r", "--red", type=int, help="red value", default=0, dest='red')
parser.add_argument("-g", "--green", type=int, help="green value", default=0, dest='green')
parser.add_argument("-b", "--blue", type=int, help="blue value", default=0, dest='blue')

args = parser.parse_args()
text=args.text
fyl=args.fyl
x=args.xcoord
y=args.ycoord
size=args.size
red=args.red
green=args.green
blue=args.blue

colr=(red, green, blue)

#if args.font is not None:
#    font=args.font
#else:

font = ImageFont.truetype("WeenDings-rnP8.ttf", size)  
#font = ImageFont.load_default()
image = Image.open(fyl)  
   
draw = ImageDraw.Draw(image)  
   
# use a truetype font  

   
draw.text((x, y), text, font=font, fill=colr)  
   
image.save(fyl) 
image.save("test.png")

