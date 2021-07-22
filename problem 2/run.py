import sys
import hashlib

#get args
args = sys.argv
if len(args) != 4:
    print("Expected 3 arguments, got {}.".format(len(args)-1))

else:
    fileName = args[1]
    try:
        with open(fileName) as f:
            hashType = args[2]
            hashTest = args[3]
            hashFound = False

            #get hash type
            if hashType.lower() == "md5":
                hashType = hashlib.md5()
                hashFound = True
            elif hashType.lower() == "sha1":
                hashType = hashlib.sha1()
                hashFound = True
            elif hashType.lower() == "sha256":
                hashType = hashlib.sha256()
                hashFound = True
            else:
                print("Hash type not found!")

            
            if hashFound:
                #get hash sum
                for part in iter(lambda: f.read(4096).encode(encoding="UTF-8"), b""):
                    hashType.update(part)

                #get result
                if hashType.hexdigest() == hashTest:
                    print("{} OK".format(fileName))
                else:
                    print("{} FAIL".format(fileName))
    
    except:
        print("{} NOT FOUND".format(fileName))