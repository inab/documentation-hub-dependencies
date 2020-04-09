import config as props
import sys, getopt

#Github Token
TOKEN = props.token
OWNER =""
REPOSITORY=""

def main(argv):
    try:
        opts, remainder= getopt.getopt(argv,"hr:o:",["repo=","owner="])
        print(opts)
        print(remainder)
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
    print ('Repository is "', REPOSITORY)
    print ('Owner is "', OWNER)

if __name__ == "__main__":
   main(sys.argv[1:])