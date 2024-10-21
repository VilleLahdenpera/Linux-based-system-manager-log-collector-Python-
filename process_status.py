import subprocess, os

def processExists(process): #Check if process is running
    try:
        call = "TASKLIST", "/FI", "imagename eq %s" %process
        output = subprocess.check_output(call)
        last_line = output.strip().split("\r\n")[-1]
        return last_line.lower().startswith(process.lower())
    except Exception as e:
            print("Error in checking process status: " + str(e))

def openProcess(self, process, location, config):    #Open process
    try:
        if (self.processExists(process)): #Check if already running
                os.system("taskkill /f /im " + process) #Restart
                process = subprocess.Popen(location, config)
    except Exception as e:
        print("Error in opening the process: " +str(e))


def openPararrelProcess(location):   #Open pararrel python process
    try:
        sp = subprocess.Popen(["python", location], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #Start subprocess from file
        while True: #Print output
            out = sp.stdout.readline()
                sp.stdout.flush()
                print(out)
                if out == "":
                    break
        while True: #Print errors and alerts
            err = sp.stderr.readline()
                sp.stderr.flush()
                print(err)
                if err == "":
                    break
        sp.poll()
    except Exception as e:
        print ("Error running paraller process: " + str(e))