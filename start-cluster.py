import os

def getChoice():
    os.system("clear")
    cwd = os.getcwd() + "/DockerComposes"

    subdirs = {}
    counter = 1
    for root, dirs, files in os.walk(cwd):
        for dir in dirs:
            subpath = os.path.join(root, dir)
            full_name = subpath + "/docker-compose.yml"
            if os.path.isfile(full_name):
                subdirs[counter] = full_name
                counter += 1
                
    for i in subdirs.keys():
        name = subdirs[i].split("DockerComposes/")[1].replace("/docker-compose.yml", "").replace("/", " ")
        print(f"{i}) {name}")
    try:
        choice = int(input("Enter your choice : "))
    except:
        return getChoice()
    if choice == len(subdirs) + 1:
            exit()
    elif choice > len(subdirs) + 1 or choice < 1:
        del choice
        return getChoice()
    else:
        return choice, subdirs

def isDetachMode():
    detachmode = input("Start in detach mode Y/N")

    if detachmode in ["Y", "y"]:
        return True
    elif detachmode in ["N", "n"]:
        return False
    else:
        return isDetachMode()
    
choice, subdirs = getChoice()
command = f"docker compose -f {subdirs[choice]} up"
if isDetachMode():
    command += " -d"
print(command)
os.system(command)