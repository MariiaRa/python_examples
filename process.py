import subprocess, os

def get_pprocess():
    '''Using the subprocess module, display information on a running process.

        Arguments:
        program -- name of the program/process to check
                        
        Returns: information about running process
        '''


    program = input("Enter the name of the program to check: ")
    try:
        #perform a ps command and assign results to a list
        ps = subprocess.Popen(["ps", "-af"], stdout=subprocess.PIPE)
        grep = subprocess.Popen(["grep", program], stdin=ps.stdout, stdout=subprocess.PIPE)
        ps.stdout.close()
        result = grep.communicate()[0]
        proginfo = result.decode('utf-8')[:-1].split()
        print(proginfo)
        #display results
        print ("\nFull path:\t\t", proginfo[11].split("..")[0], "\nOwner:\t\t\t", proginfo[0], "\nProcess ID:\t\t", proginfo[1], "\nParent process ID:\t", proginfo[2], "\nTime started:\t\t", proginfo[4])
    except:
        print ("There was a problem with the program.")

if __name__ == '__main__':
    get_pprocess()
