import argparse
from PIL import Image
#import cv2

parser = argparse.ArgumentParser(description='scroll2')
parser.add_argument("-p", "--picture", type=str, help="picture name", default="temp1.jpg", dest='fyl')
parser.add_argument("-d", "--direction", type=str, help="scroll direction: up, down, left, right", default="up", dest="direction")
parser.add_argument("-s", "--span", type=int, help="span of strip to move in pixels", default=10, dest="span")
parser.add_argument("-o", "--output", type=str, help="output file name", default=None, dest='fyl_out')
args = parser.parse_args()
fyl=args.fyl
direction=args.direction
span=args.span
out=args.fyl_out
im = Image.open(fyl)
wyd=im.width
hyt=im.height
if out is None:
    out=fyl
def concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
def concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

if direction == "up": #cut the top off & move to bottom thus moving image up
    im_cropb = im.crop((0, span, 512, 512))
    im_cropt = im.crop((0, 0, 512, span+1))
    outimg=concat_v(im_cropb, im_cropt)
    #or replace from bottom with noise

if direction == "down": #cut the bottom off and move to top thus moving image down
    im_cropb = im.crop((0, 512-span, 512, 512))
    im_cropt = im.crop((0, 0, 512, 512-span))
    outimg=concat_v(im_cropb, im_cropt) #reverse order)


if direction == "left":
    im_cropL = im.crop((0, 0, span+1, 512))
    im_cropR = im.crop((span, 0, 512, 512))
    outimg=concat_h(im_cropR, im_cropL)

if direction == "right":
    im_cropR = im.crop((512-span, 0, 512, 512)) #20 pixels from the right)
    im_cropL = im.crop((0, 0, 512-span, 512))# the rest of the pixels
    outimg=concat_h(im_cropR, im_cropL)

outimg.save(out)



