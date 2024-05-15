import argparse
import shutil
import os

AUTHOR_NAME = "Pkzoid (Akash Siddique)"
VERSION = "BETA"

print(AUTHOR_NAME)

print("""Data and files can be securely embedded in images, videos, executables, and more. Protect your data from:
    Viruses and malware
    Unwanted visibility""")

praser = argparse.ArgumentParser()
praser.add_argument("-m",help="Use 1 to read the .exe, and 0 to embed it")
praser.add_argument("-t",help="Specify the target where you want to embed your data, like in the .exe or elsewhere")
praser.add_argument("-f",help="Specify the filename of the file you want to embed into the .exe")
praser.add_argument("-v",help="unqiue code for store data & use for read")
praser.add_argument("-n",help="Export File Name")
praser.add_argument("-d",help="Specify The Directory")

def embed_exe(target:str,var : str):
    try:
        with open(target,"ab") as f:
            f.write(var.encode("utf-8"))
    except (FileNotFoundError):
        print(f"{target} File Not Found")
    except (PermissionError):
        print("File Acess Error Run As Admin")
    
def read_file(file:str):
    try:
        with open(file,"rb") as f:
            image = f.read()
        return image
    except (FileNotFoundError):
        print(f"{file} File Not Found")
    except (PermissionError):
        print("File Acess Error Run As Admin")

def write_into_exe(target:str,content:str):
    try:
        with open(target,"ab") as f:
            f.write(content)
        print("Successfully Embedded")
    except (FileNotFoundError):
        print(f"{target} File Not Found")
    except (PermissionError):
        print("File Acess Error Run As Admin")

def write_file(content:str,name:str):
    try:
        with open(name,"wb") as f:
            f.write(content)
    except (FileExistsError):
        user_Question = "File Already Exist With Same Name??\nDo You Want OverWrite it? Yes/No"
        if user_Question == "Yes" or user_Question == "Y":
            with open(name,"wb") as f:
                f.write(content)
    except (PermissionError):
        print("File Acess Error Run As Admin")

def read_exe(target:str,var:str,name:str):
    with open(target,"rb") as f:
        content = f.read()
        find = content.index(var.encode("utf-8"))
        f.seek(find+3)
        write_file(f.read(),name)


def Directory_Pack(target:str,path:str,name:str,var:str):
    archive = shutil.make_archive(name,"zip",path)
    if bool(archive):
        embed_exe(target,var)
        write_into_exe(target,read_file(archive))
        os.remove(name+".zip")

if __name__ == "__main__":
    args = praser.parse_args()
    if args.m == "0":
        embed_exe(args.t,args.v)
        write_into_exe(target=args.t,content=read_file(args.f))
    elif args.m == "1":
        read_exe(args.t,args.v,args.n)
    elif args.m == "2":
        Directory_Pack(args.t,args.d,args.n,args.v)
    else:
        print("invalid argument")


    
    

        

	