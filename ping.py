import subprocess, os, platform

def checkPing(self, host, status):  #Check ping status
    try:
        with open(os.devnull, "w") as DEVNULL:     
            p = "-n" if platform.system().lower()=="windows" else "-c"
            subprocess.check_call(["ping", p, 5, host],stdout=DEVNULL,stderr=DEVNULL)
            status = True
            print("Ping to " + host + " " + str(status))
            return status
    except Exception as e:
        print ("Error in ping process: " + str(e))