from PIL import Image

def main():
    im = Image.open("head.png")
    print(im.height+(im.width*im.height))
    im.convert('L').save("gr.png")
    im = Image.open("gr.png")
    out = im
    out
    arr = []
    for x in range(im.width):
        for y in range(im.height):
            if out.getpixel((x,y)) <= 30:
                out.putpixel((x,y),255)
                arr.append("1")
            else:
                out.putpixel((x,y),0)
                arr.append("0")
        arr.append("\n")
    print(len(arr))
    fl = open("img.txt","w")
    fl.write(str("".join(arr)))
    out.show()
    return arr

def strToimg():
    fl = open("img.txt","r")
    arr = fl.read()
    #print(arr)
    y=0
    x=0
    for f in arr:
        if f == "\n":
            y+=1
        if f != "\n" and y == 0:
            x+=1
    print(y)
    print(x)
    #ou = Image.open("blnk.jpg").convert('L')
    ou = Image.new("L", (1193,y),color = "white")
    y = 0
    x = 0
    narr = []
    #for f in range(0,len(arr)-1,1):
    for f in arr.split(" "):
        try:
            if f == "\n":
                y += 1
                x = 0
            if f == "1":
                ou.putpixel((x,y),255)
            if f == "0":
                ou.putpixel((x,y),0)
            x += 1
        except ValueError:
            i = 0
        #print(int(arr[x]))
    #print(y)
    ou = ou.rotate(-90)
    ou.save("Result.png")
    #print(str("".join(narr)))
    
    return
main()
strToimg()