import paramiko, datetime, os

def command(address, user, passwd, command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(address, username=user, password=passwd) #Connect to to client with ssh
        stdin, stdout, stderr = client.exec_command(command) #Send command
        exit_status = stdout.channel.recv_exit_status() #Wait for status   
        if exit_status == 0:
                client.close()
        else:
            print("Error while giving the command. Exit status:" + exit_status)
            client.close()       
    except Exception as e:
        print("Error in command process: " + str(e))



def downloadData(address, user, passwd, name, location):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(address, username=user, password=passwd)
        new_name = str(datetime.datetime.now().strftime("%y%m%d")) + "_" + str(datetime.datetime.now().strftime("%H%M")) + ".zip" #Give data date and time
        sftp = ssh.open_sftp()
        sftp.get(location + name, os.path.join(name,new_name)) #Download data from client
        command = "sudo rm " + location + name #Delete data from client
        stdin, stdout, stderr = ssh.exec_command(command)
        exit_status = stdout.channel.recv_exit_status() #Wait for status   
        if exit_status == 0:
            ssh.close()
        else:
            print("Error while giving the remove command. Exit status:" + exit_status)
            ssh.close()
    except Exception as e:
            print ("Error in download process: " + str(e))