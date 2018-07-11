import tarfile, sys

def tar_archive():
    '''Using the tarfile module, open tar, extract files, get info about file and list all files in archive.

        Arguments:
        sys.argv[1] -- name of tar
       
        '''
 
    try:
        #open tarfile
        tar = tarfile.open(sys.argv[1], "r:tar")
 
        #present menu and get selection
        selection = input("\nEnter \n1 to extract a file \n2 to display information on a file in the archive \n3 to list all the files in the archive\n")
        #perform actions based on selection above
        if selection == "1":
            filename = input("enter the filename to extract:  ")
            tar.extract(filename)
        elif selection == "2":
            filename = input("enter the filename to inspect:  ")
            for tarinfo in tar:
                if tarinfo.name == filename:
                    print ("\nFilename:\t\t", tarinfo.name, "\nSize:\t\t\t", tarinfo.size, "bytes", "\nPermiissions:\t\t", tarinfo.mode)
        elif selection == "3":
            print(tar.list(verbose=True))
    except:
        print ("There was a problem running the program")

if __name__ == '__main__':
    tar_archive()
