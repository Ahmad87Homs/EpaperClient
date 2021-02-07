import  socket
import imageToByte as itb
import time
from PIL import Image

#defination Section

image = Image.open('im1.jpg')
#@image = image.rotate(180)

data=itb.convertTobinaryMonochrome(image,960,640)
reves_data=itb.ButtomToLTopImage(data,960,640)
str_data=itb.converttoHEXstream(reves_data)

# start sending data
Buffer_Size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# TCP Protcol
ip_port=('192.168.1.39',80)
try:
    s.connect(ip_port)
    print("clint addrress",s.getsockname())
    print("server addrress",s.getpeername())
    time.sleep(1)
    count=0
    for i in range(0,len(str_data),640):
            print(str_data[i:i+640])
            s.send(str_data[i:i+640].encode("utf-8"))
            count+=1
            time.sleep(.010)
    print(count)
    s.close()
except Exception as msg:
    print('Error Message:',msg)
finally:
    print("program finished")