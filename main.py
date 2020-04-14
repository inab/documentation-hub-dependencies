import config as props
import sys
import getopt
from GitHubDataFetcher import GitHubDataFetcher
from DependencyFile import DependencyFile
from ErrorFile import ErrorFile


# Github Token
TOKEN = props.token
OWNER = ""
REPOSITORY = ""
OUTPUTFILE = ""

def showHelp():
    print('-r or --repo  The name of the github repository')
    print('-o or --owner  The owner of the github repository')
    print('-f or --outputfile (Optional) (Default : <OWNER+REPONAME>dependecies.json) \
            The output file')

def main(argv):
    global OWNER, REPOSITORY, OUTPUTFILE

    try:
        # opts are the arguments and remainders are the arrguments that will not be complete if something goes wrong
        opts, remainder = getopt.getopt(
            argv, "hr:o:f:", ["repo=", "owner=", "outputfile="])
    except getopt.GetoptError:
        showHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            showHelp()
            sys.exit()
        elif opt in ("-r", "--repo"):
            REPOSITORY = arg
        elif opt in ("-o", "--owner"):
            OWNER = arg
        elif opt in ("-f", "--outputfile"):
            OUTPUTFILE = arg
    # check if repo and owner are specified
    if(OWNER and REPOSITORY):
        # create the fetcher
        data = GitHubDataFetcher(OWNER, REPOSITORY, TOKEN)
        # get the response object
        res = data.getInfo()

        # response is type ErrorFile or DependencyFile
        if(isinstance(res, DependencyFile)):
            if(OUTPUTFILE):
                output = OUTPUTFILE+"dependecies.json"
            else:
                output = OWNER+REPOSITORY+"dependecies.json"
        elif(isinstance(res, ErrorFile)):
            output = "error.json"
            # write file
        res.toJson(output)
    else:
        print("--repo and --owner arguments are mandatory")


if __name__ == "__main__":
    main(sys.argv[1:])
