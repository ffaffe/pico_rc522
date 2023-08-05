from mfrc522 import MFRC522 
import utime
from machine import Pin

lock =Pin(28,Pin.OUT)
buzzer = Pin(27, Pin.OUT)
RLed =Pin(18,Pin.OUT)
GLed =Pin(19,Pin.OUT)

lock.value(1)
buzzer.value(0)
RLed.value(0)
GLed.value(0)



def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
                  
rc522 = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

print("")
print("Place the RFID Card")
print("")


while True:

    (stat, tag_type) = rc522.request(rc522.REQALL)

    if stat == rc522.OK:
        (status, raw_uid) = rc522.SelectTagSN()
        if stat == rc522.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("Card detected! UID: {}".format(rfid_data))
            if rfid_data == "81a3dc79":
                
                lock.value(0)
                GLed.value(1)
                utime.sleep(5)
                lock.value(1)
                GLed.value(0)
                
                
            elif rfid_data == "ad6d1583":
                
                lock.value(0)
                GLed.value(1)
                utime.sleep(5)
                lock.value(1)
                GLed.value(0)
                
            elif rfid_data == "866080f8":
                
                lock.value(0)
                GLed.value(1)
                utime.sleep(5)
                lock.value(1)
                GLed.value(0)
                
                
            elif rfid_data == "337cd633":
                
                lock.value(0)
                GLed.value(1)
                utime.sleep(5)
                lock.value(1)
                GLed.value(0)
                

            else:
                
                buzzer.value(1)
                RLed.value(1)
                utime.sleep(1)
                buzzer.value(0)
                RLed.value(0)
