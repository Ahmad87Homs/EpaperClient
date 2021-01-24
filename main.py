import  socket
import imageToByte as itb
import time
from PIL import Image

#defination Section

image = Image.open('image1.bmp')
image = image.rotate(360)

data=itb.convertTobinaryMonochrome(image,296,128)
reves_data=itb.rigtToLiftImage(data,296,128)
str_data=itb.converttoHEXstream(reves_data)

# start sending data
Buffer_Size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# TCP Protcol
ip_port=('192.168.1.48',80)
try:
    s.connect(ip_port)
    print("clint addrress",s.getsockname())
    print("server addrress",s.getpeername())
    time.sleep(1)
    count=0
    for i in range(0,len(str_data),128):
            print(str_data[i:i+128])
            s.send(str_data[i:i+128].encode("utf-8"))
            count+=1
            time.sleep(.010)
    print(count)
    s.close()
except Exception as msg:
    print('Error Message:',msg)
finally:
    print("program finished")