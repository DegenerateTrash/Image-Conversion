from PIL import Image
import uuid
import os
import base64
import time

def main():
    im = Image.open(str(input("Image Name: ")))
    i = True
    while i == True:
        try:
            uui = str(uuid.uuid4())
            os.mkdir(uui)
            i = False
        except:
            h = 0
            print("A")
    print(im.height+(im.width*im.height))
    im.save("gr.png")
    im = Image.open("gr.png")
    out = im
    out
    red = []
    blu = []
    gre = []
    for y in range(im.height):
        for x in range(im.width):
            red.append("{} ".format(base64.b64encode(
                bytes(
                    str(
                        out.getpixel(
                            (x,y)
                            )
                            [0]
                            )
                            ,'utf-8'
                            ))))
            gre.append("{} ".format(base64.b64encode(
                bytes(
                    str(
                        out.getpixel(
                            (x,y)
                            )
                            [1]
                            )
                            ,'utf-8'
                            ))))
            blu.append("{} ".format(base64.b64encode(
                bytes(
                    str(
                        out.getpixel(
                            (x,y)
                            )
                            [2]
                            )
                            ,'utf-8'
                            ))))
        gre.append("\n ")
        blu.append("\n ")
        red.append("\n ")
    flr = open("{}\imgr.txt".format(uui),"w", encoding="utf-8")
    flg = open("{}\imgg.txt".format(uui),"w", encoding="utf-8")
    flb = open("{}\imgb.txt".format(uui),"w", encoding="utf-8")
    flr.write(str("".join(red)))
    flg.write(str("".join(gre)))
    flb.write(str("".join(blu)))
    out.show()
    return

def strToimg():

    fol = str(input("Folder: "))
    start = time.time()
    flr = open("{}\imgr.txt".format(fol),"r", encoding="utf-8")
    flg = open("{}\imgg.txt".format(fol),"r", encoding="utf-8")
    flb = open("{}\imgb.txt".format(fol),"r", encoding="utf-8")
    flr = flr.read()
    flg = flg.read()
    flb = flb.read()
    #print(arr)
    yz=0
    xz=0
    for f in flr.split(" "):
        if f == "\n":
            yz+=1
        if f != "\n" and yz == 0:
            xz+=1
    print(yz)
    print(xz)
    #ou = Image.open("blnk.jpg").convert('L')
    ou = Image.new("RGB", (xz,yz), color="black")
    y = 0
    x = 0
    narr = []
    #for f in range(0,len(arr)-1,1):
    x = 0
    flr = flr.split(" ")
    flg = flg.split(" ")
    flb = flb.split(" ")
    
    for f in range(0,len(flr)-1,1):
        flr[f] = flr[f].replace("b'", "")
        flr[f] = flr[f].replace("'", "")
        flg[f] = flg[f].replace("b'", "")
        flg[f] = flg[f].replace("'", "")
        flb[f] = flb[f].replace("b'", "")
        flb[f] = flb[f].replace("'", "")
        try:
            if flr[f] == "\n":
                y += 1
                x = 0
            else:
                #print(int(base64.b64decode(str(flr[f])),16))
                try:
                    #print(base65536.decode(str(flr[f])))
                    #print(int(base64.b64decode(str(flr[f])),16))
                    col = (int(base64.b64decode(str(flr[f])),16),int(base64.b64decode(str(flg[f])),16),int(base64.b64decode(str(flb[f])),16))
                    
                    ou.putpixel((x,y),col)
                    x += 1
                except:
                    p = 0
        except ValueError:
            i = 0
    try:
        ou.save("{}\Result.png".format(fol))
    except:
        p=0
    print("Took {0:0.1f} seconds".format(time.time() - start))
    return
#main()
strToimg()