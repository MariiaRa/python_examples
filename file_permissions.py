import stat, sys, os, string, subprocess, glob

def get_permissions():
    '''Using the stat module, get permissions for each file found and display them on the screen.

        Keyword arguments:
        pattern -- search pattern from user (*.txt. *example*, *.py etc)
        path -- current directory where python shell is running
        commandOutput -- results of find command (using subprocess module)
                
        Returns: listing of permissions for files

        '''

    try:
        pattern = input("Enter the file pattern to search for:\n")
        path = os.getcwd()
        files = glob.glob(path+'/'+pattern)

        print ("Files:")
        print(files)
        print ("================================")
        for file in files:
            mode=stat.S_IMODE(os.lstat(file)[stat.ST_MODE])
            print(mode)
            print ("\nPermissions for file ", file, ":")
            for level in "USR", "GRP", "OTH":
                for perm in "R", "W", "X":
                    if mode & getattr(stat,"S_I"+perm+level):
                        print (level, " has ", perm, " permission")
                    else:
                        print (level, " does NOT have ", perm, " permission")
    except:
        print ("There was a problem - check the message above")


if __name__ == '__main__':
    get_permissions()
    
