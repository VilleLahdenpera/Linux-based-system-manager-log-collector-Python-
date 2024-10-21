import serial, os, datetime

def setupSerial(port, baud): #Setup serial connection
    try:
        ser=serial.Serial(port=port,baudrate=baud,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1) #Serial port configuration
        try:
            ser.close() #Close previous serial connection
        except: pass
    except Exception as e:
        print("Error in Serial setup process: " + str(e))
        return
    return ser


def readSerial(ser, expect, buffer): #Read serial port for expected return
    try: 
        lines=0
        while lines < 10:
            read = ser.readline().decode("ascii").strip()
            buffer += datetime.datetime.now().strftime("[%Y/%m/%d - %H:%M:%S] ") + read #Collect serial data with time and date
            if expect in read:
                    return True
            lines += 1
        return False
    except Exception as e:
        print("Error in reading serial input: " + str(e))