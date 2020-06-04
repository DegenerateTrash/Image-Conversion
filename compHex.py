from PIL import Image
import uuid
import os

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
            red.append("{} ".format(hex(out.getpixel((x,y))[0]).replace("0x","")))
            gre.append("{} ".format(hex(out.getpixel((x,y))[1]).replace("0x","")))
            blu.append("{} ".format(hex(out.getpixel((x,y))[2]).replace("0x","")))
        gre.append("\n ")
        blu.append("\n ")
        red.append("\n ")
    flr = open("{}\imgr.txt".format(uui),"w")
    flg = open("{}\imgg.txt".format(uui),"w")
    flb = open("{}\imgb.txt".format(uui),"w")
    flr.write(str("".join(red)))
    flg.write(str("".join(gre)))
    flb.write(str("".join(blu)))
    out.show()
    return

def strToimg():

    fol = str(input("Folder: "))
    flr = open("{}\imgr.txt".format(fol),"r")
    flg = open("{}\imgg.txt".format(fol),"r")
    flb = open("{}\imgb.txt".format(fol),"r")
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
    ou = Image.new("RGB", (xz,yz))
    y = 0
    x = 0
    narr = []
    flr = flr.split(" ")
    flb = flb.split(" ")
    flg = flg.split(" ")
    #for f in range(0,len(arr)-1,1):
    x = 0
    for f in range(0,len(flr)-1,1):
        try:
            if flr[f] == "\n":
                y += 1
                x = 0
            else:
                col = (int("0x{}".format(flr[f]),16),int("0x{}".format(flg[f]),16),int("0x{}".format(flb[f]),16))
                ou.putpixel((x,y),col)
                x += 1
        except ValueError:
            i = 0
    ou.save("{}\Result.jpg".format(fol))
    return
main()
strToimg()