from PIL import Image
import ImageFilter
import ImageEnhance
import os

#pil_im = Image.open('secode')

def binaryCode(secode, outfile):
    im = Image.open(secode)
    w, h = im.size

#im.rotate(45)
    #print 'im.mode/t'+im.mode

    out = im.convert('L')

    pixdata = out.load()
    #print type(pixdata)
    print pixdata[30,10]
    #pixdata[30,10] = 0
    # binary pic
    for y in xrange(out.size[1]):
        for x in xrange(out.size[0]):
            if pixdata[x,y] < 90:
                pixdata[x,y] =0
            if pixdata[x,y] >= 90:
                pixdata[x,y] = 255

    for y in xrange(3, out.size[1]-1):
        print y
        for x in xrange(2, out.size[0]-1):
            print x
            if pixdata[x, y] < 90:
                if pixdata[x+1, y] > 90 and pixdata[x-1, y] >90 and pixdata[x, y+1] > 90 and pixdata[x, y-1] > 90 and pixdata[x, y+1] > 90:
                    pixdata[x, y] =255
    print pixdata[30,10]

    #out.filter(ImageFilter.MedianFilter())
    #enhancer = ImageEnhance.Contrast(out)
    #out = enhancer.enhance(2)
    #out = out.convert('1')





#print 'changed\t', pixdata[30,10]

    out.save(outfile)


if __name__=="__main__":
    for i in xrange(8):
        print i
        binaryCode('./soure/secode0'+str(i), './dest/out'+str(i)+'.png')



#im.thumbnail((w//2,h//2))
#im.save('~/home/secode.png','png')

#pil_im2= pil_im
#outfile = './secode01'
#pil_im2.save(outfile)
