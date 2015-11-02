from PIL import Image
import ImageFilter
import ImageEnhance
import os

#pil_im = Image.open('secode')

def binaryCode(secode):
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

    for y in xrange(3, out.size[1]-2):
        #print y
        for x in xrange(3, out.size[0]-2):
            #print x
            if pixdata[x, y] < 90:
                if pixdata[x+1, y] > 90 and pixdata[x-1, y] >90 and pixdata[x, y+1] > 90 and pixdata[x, y-1] > 90 and pixdata[x, y+1] > 90:
                    pixdata[x, y] =255
                count = 0
                l0 = [-2, -1, 0, 1, 2]
                l1 = [-2, -1, 0, 1, 2]
                for i in l0:
                    for j in l1:
                        if pixdata[x + i, y + j] <90:
                            count += 1
                if count == 2:
                    for i in l0:
                        for j in l1:
                            pixdata[x+i, y+j] = 255

    # bianyuan zaodian
    print out.size[1]
    for i in xrange(out.size[0]):
        pixdata[i, 1]  = 255
        pixdata[i, 0]  = 255
        #pixdata[i, 30] = 255
        pixdata[i, 29] = 255
        pixdata[i, 28] = 255

    # split algorithm
    #find the x_left
    c = 0
    t = 0
    x_left = 0
    for i in xrange(5, out.size[0]):
        t = 0
        for j in xrange(out.size[1]):
            if pixdata[i, j] == 0:
                c += 1
                t += 1
        if(t == 0):
            c = 0
        if(c >= 4):
            x_left = i - 4
            break
    print 'x_left\t',  x_left
    print "out.size[0]\t", out.size[0]
    # find x_right
    c = 0
    t = 0
    x_right = 0
    for i in xrange(5, out.size[0]):
        t = 0
        for j in xrange(0, out.size[1]):
            if  pixdata[out.size[0]-i, j] == 0:
                c += 1
                t += 1
        if t == 0:
            c = 0
        if c >= 4:
            x_right = out.size[0] - i + 4
            break
    print 'x_right\t',x_right



    #print pixdata[30,10]

    #out.filter(ImageFilter.MedianFilter())
    #enhancer = ImageEnhance.Contrast(out)
    #out = enhancer.enhance(2)
    #out = out.convert('1')





#print 'changed\t', pixdata[30,10]
    # copy the region
    region = (x_left, 0, x_right, 30)
    out = out.crop(region)
    pixdata = out.load()
    # process the new pic
    #print 'new pic size\t', out.size

    x0 = 0
    x1 = out.size[0]*1/4
    x2 = out.size[0]*2/4
    x3 = out.size[0]*3/4
    x4 = out.size[0]

    Lx = [x1, x2, x3]
    # wei tiao x
    # contain 30 points
    Ltrace = [[],[],[]]

    for i in range(3):
        x_temp = 0
        for j in xrange(2, 28):
            if pixdata[Lx[i]+x_temp, j] == 255:
                if pixdata[Lx[i]+x_temp, j+1] == 255:
                    Ltrace[i].append((Lx[i]+x_temp,j))
                if pixdata[Lx[i]+x_temp, j+1] == 0:
                    for t in [-1,1,-2,2,-3,3,-4,4]:
                        if pixdata[Lx[i]+x_temp+t, j+1] == 255 and pixdata[Lx[i]+x_temp+t, j] == 255:
                            x_temp = x_temp+t
                            Ltrace[i].append((Lx[i]+x_temp, j))


    print 'Ltrace length\t', len(Ltrace)


    # writh the trace
    '''
    for t in Ltrace[0]:
        pixdata[t[0],t[1]] = 200
        print '0\t',t
    for t in Ltrace[1]:
        pixdata[t[0],t[1]] = 200
        print '1\t', t


    for t in Ltrace[2]:
        pixdata[t[0],t[1]] = 200
        print '2\t', t
    '''
    #pixdata[31, 20] = 0
    print out.size
    print len(Ltrace)
    print len(Ltrace[2])

    out1 = out
    max = 0
    min = 200
    for t in Ltrace[0]:
        if t[0] > max:
            max = t[0]
        if t[0] < min:
            min = t[0]

    # change out1
    pixdata1 = out1.load()
    for t in Ltrace[0]:
        for i in range(t[0], max):
            pixdata[i, t[1]] = 255

    region = (0,0, max,30)
    out11 = out1.crop(region)


    ###
    out2 = out
    pixdata2 = out2.load()

    max_left = min
    max_right = 0

    for t in Ltrace[1]:
        if t[0] > max_right:
            max_right = t[0]

    for t in Ltrace[0]:
        for i in range(min, t[0]):
            pixdata2[i, t[1]] = 255
    for t in Ltrace[1]:
        for i in range(t[0], max_right):
            pixdata2[i, t[1]] = 255

    region = (max_left, 0, max_right, 30)
    out22 = out2.crop(region)

    #
    out3 = out
    # get left
    pixdata3 = out3.load()
    left = 200
    right = 0
    left2 = 200
    for t in Ltrace[1]:
        if t[0] < left:
            left = t[0]
    for t in Ltrace[2]:
        if t[0] > right:
            right = t[0]
        if t[0] < left2:
            left2 = t[0]
    for t in Ltrace[1]:
        for i in range(left, t[0]):
            pixdata3[i, t[1]] = 255
    for t in Ltrace[2]:
        for i in range(t[0], right):
            pixdata3[i, t[1]] = 255
    region = (left, 0, right, 30)
    out33 = out3.crop(region)




    out4 = out
    pixdata4 = out4.load()
    # get left right
    left = left2
    for t in Ltrace[2]:
        for i in range(left, t[0]):
            pixdata4[i, t[1]] = 255
    region = (left, 0, out4.size[0],30)
    out44 = out4.crop(region)






    #out1 = out.crop((0,  0, x1, 30))
    #out2 = out.crop((x1, 0, x2, 30))
    #out3 = out.crop((x2, 0, x3, 30))
    #out4 = out.crop((x3, 0, x4, 30))




    #size = (30, 20)
    #out.thumbnail(size)
    out11.save('./dest/'+secode[10:]+'11'+'.png')
    out22.save('./dest/'+secode[10:]+'22'+'.png')
    out33.save('./dest/'+secode[10:]+'33'+'.png')
    out44.save('./dest/'+secode[10:]+'44'+'.png')

    out.save('./dest/'+secode[10:]+'all'+'.png')
    #out1.save('./dest/'+secode[10:]+'01'+'.png')
    #out2.save('./dest/'+secode[10:]+'02'+'.png')
    #out3.save('./dest/'+secode[10:]+'03'+'.png')
    #out4.save('./dest/'+secode[10:]+'04'+'.png')



if __name__=="__main__":
    #for i in xrange(1):

        #print i

    #binaryCode('./soure/secode0'+str(i))
    binaryCode('./soure/secode')
    '''
    for i in xrange(9):
        #print i
        binaryCode('./soure/secode1'+str(i))
        binaryCode('./soure/secode2'+str(i))
    '''
#im.thumbnail((w//2,h//2))
#im.save('~/home/secode.png','png')

#pil_im2= pil_im
#outfile = './secode01'
#pil_im2.save(outfile)
