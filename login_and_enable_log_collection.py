import time

def enableLogCollection(self, ser, settings, delay, enter, login, retry, flag, user, passwd): #Log in and enable system log collection
    try:
        ser.open() #Open serial connection
        while retry <= 10: #Retry 10 times if no success
            ser.write(enter)
            if (self.readSer(ser, "Logged in prompt")): #Check if already logged in
                login = True
                break
            #Login
            if (login == False): 
                ser.write(user)   
                if (self.readSer(ser, "Password:")):
                    ser.write(passwd) 
                    ser.write(enter)
            if (self.readSer(ser, "Logged in prompt")):
                        login = True
                        break
            retry += 1
            time.sleep(delay)

        #Set flags for log collection  
        if login: 
            retry=0
            while retry <= 10: #Retry 10 times if no success
                ser.write(enter)
                ser.write(flag)
                if (self.readSer(ser, "Flags written succesfully")):
                    break
                retry += 1
                time.sleep(delay)

            #Enable logs 
            retry=0               
            while retry <= 10: 
                ser.write(enter)
                ser.write("enable")
                ser.write("status")
                if (self.readSer(ser, "on")):
                    break
                retry += 1
                time.sleep(delay)
            
            #Logout and close serial connection
            retry=0
            while retry <= 10:
                ser.write(enter)
                ser.write("exit")
                if (self.readSer(ser, "logout")):
                    ser.close()
                retry += 1
                time.sleep(delay)

    except Exception as e:
            ser.close()
            print ("Error in log enable process: " + str(e))
