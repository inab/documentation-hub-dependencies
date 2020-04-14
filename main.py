import config as props
import sys, getopt
from Repository import Repository


#Github Token
TOKEN = props.token
OWNER =""
REPOSITORY=""

def main(argv):
    global OWNER
    global REPOSITORY

    try:
        opts, remainder= getopt.getopt(argv,"hr:o:",["repo=","owner="])
        print(opts)
    except getopt.GetoptError:
        print ('-r or --repo  The name of the github repository')
        print ('-o or --owner  The owner of the github repository')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('-r or --repo  The name of the github repository')
            print ('-o or --owner  The owner of the github repository')
            sys.exit()
        elif opt in ("-r", "--repo"):
            REPOSITORY = arg
        elif opt in ("-o", "--owner"):
            OWNER = arg
    if(OWNER and REPOSITORY):
        d = Repository(OWNER,REPOSITORY,TOKEN)
        d.createJsonFile()
    else:
        print("Both arguments are mandatory")

    

if __name__ == "__main__":
   main(sys.argv[1:])