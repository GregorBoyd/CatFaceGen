
def drawcat(filename="cat"):

    from PIL import Image,ImageDraw
    from random import randint as rint

    img = Image.new("RGB", (256,256), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    r,g,b = rint(0,255), rint(0,255), rint(0,255)
    dr = (rint(0,255) - r)/256.
    dg = (rint(0,255) - g)/256.
    db = (rint(0,255) - b)/256.
    for i in range(256):
        r,g,b = r+dr, g+dg, b+db
        draw.line((i,0,i,256), fill=(int(r),int(g),int(b)))

#cat main colours
    cr,cg,cb = rint(50,255), rint(50,255), rint(50,255)

    #draw left ear
    draw.polygon([12,48,98,75,30,130], fill = (int(cr),int(cg),int(cb)), outline ='black')

    #draw right ear
    draw.polygon([244,48,158,75,226,130], fill = (int(cr),int(cg),int(cb)), outline ='black')

    #draw face (inc redrawing inside of ears to get rid of lines
    draw.ellipse((24, 64, 232, 236), fill = (int(cr),int(cg),int(cb)), outline ='black')
    draw.polygon([18,54,98,76,31,129], fill = (int(cr),int(cg),int(cb)))
    draw.polygon([238,54,158,76,225,129], fill = (int(cr),int(cg),int(cb)))

#cat 2nd colours
    cr2,cg2,cb2 = rint(0,255), rint(0,255), rint(0,255)
    
    #ear
    draw.polygon([38,109,72,81,27,64], fill = (int(cr2),int(cg2),int(cb2)))
    draw.polygon([218,109,184,81,229,64], fill = (int(cr2),int(cg2),int(cb2)))

    #draw patterns
    patterntype = rint(0,1)
    if patterntype == 0:
        #forehead
        draw.polygon([89,73,110,68,104,85], fill = (int(cr2),int(cg2),int(cb2)))
        draw.polygon([167,73,146,68,152,85], fill = (int(cr2),int(cg2),int(cb2)))
        #side
        draw.polygon([47,200,57,183,34,183], fill = (int(cr2),int(cg2),int(cb2)))
        draw.polygon([209,200,199,183,222,183], fill = (int(cr2),int(cg2),int(cb2)))
    else:
        pass
    
    #draw whiskers
    #left
    draw.line([34,136,104,152],'black')
    draw.line([38,155,102,160],'black')
    #right
    draw.line([222,136,152,152],'black')
    draw.line([218,155,154,160],'black')
        
    #draw mouth
    mouthtype = rint(0,1)
    if mouthtype == 0:
        draw.arc([100,147,128,187], 0, 180, 'black')
        draw.arc([128,147,156,187], 0, 180, 'black')
    else:
        draw.line([128,167,128,187],'black')
        draw.arc([100,167,128,207], 0, 180, 'black')
        draw.arc([128,167,156,207], 0, 180, 'black')
        
    nosetype = rint(0,1)
    if nosetype == 0:
    #draw nose type 1
        draw.polygon([120,150,136,150,128,167], fill = 'black')
    else:
        #draw nose type 2
        draw.polygon([120,150,128,140,136,150,128,167], fill = 'black')

    eyetype = rint(0,2)
    if eyetype == 0:
        #draw eye type 1
        draw.ellipse((110, 125, 120, 135), fill = 'black')
        draw.ellipse((136, 125, 146, 135), fill = 'black')
    elif eyetype == 1:
        #draw eye type 2
        draw.ellipse((105, 125, 120, 135), fill = 'black')
        draw.ellipse((136, 125, 151, 135), fill = 'black')
    else:
        #draw eye type 3
        draw.arc([98,125,124,136], 0, 180, 'black')
        draw.arc([132,125,158,136], 0, 180, 'black')

    img.save(filename + ".png", "PNG")

if __name__ == "__main__":
    drawcat()

