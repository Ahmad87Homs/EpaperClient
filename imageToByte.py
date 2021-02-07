from PIL import Image

def toHex(value):
    if(value<10):
        return str(value)
    elif(value==10):
        return 'A'
    elif (value==11):
        return 'B'
    elif(value==12):
        return 'C'
    elif (value==13):
        return 'D'
    elif (value==14):
        return 'E'
    elif (value==15):
        return 'F'
    else :
        return '0'

def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)


def convertTobinaryMonochrome(image,width,height):
    white = (255)
    black = (0)
    data=''
    count=0
    #image = Image.open(path)
    image = image.resize((width, height))
    image = image.convert('1')
    for i in range(0, width):
        for j in range(0, height):
            if ((image.getpixel((i, j))) == white):
                data = data + '1'
            elif ((image.getpixel((i, j))) == black):
                data = data + '0'
            else:
                data = data + '0'
            count = count + 1
    if(count==(width*height)):
        return data
    else:
        raise Exception("Error: Passed value can't be negative")
        return 'Converting Error'


def rigtToLiftImage(data,width,height):
    reves_data=''
    for i in range(0, width):
        for j in range(0, height):
            index = ((width-1 - i) * height) + j
            reves_data = reves_data + data[index]
    return reves_data

def ButtomToLTopImage(data,width,height):
    reves_data=''
    for i in range(0, height):
        for j in range(0, width):
            index=(height-i-1)+(height*j )
           # index = ((width-1 - i) * height) + j
            reves_data = reves_data + data[index]
    return reves_data


def converttoHEXstream(reves_data):
    str_data = ''
    str_temp=''
    for i in range(0, len(reves_data), 8):
        MSB = int(reves_data[i:i + 4])
        LSB = int(reves_data[i + 4:i + 8])
        c = (BinaryToDecimal(MSB) << 4) | (BinaryToDecimal(LSB))
        str_temp = (toHex(BinaryToDecimal(MSB)) + toHex(BinaryToDecimal(LSB)))
        str_data = str_data + str_temp
    return str_data
