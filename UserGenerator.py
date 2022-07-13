#!/usr/bin/python3
import argparse


# Argument Parser
parser = argparse.ArgumentParser(description='Generating Custom Userlist')
parser.add_argument("-f","--file",required=True,help='Path of the first file')
parser.add_argument("-d","--delimiter",required=True,help='Set your delimiter')
parser.add_argument("-o","--outfile",required=False,help="File name to save the result")
args = vars(parser.parse_args())
options = parser.parse_args()

# Clear List Of Users
clear_list = list()
file = open(args["file"],"r")
read_file = file.readlines()
for item in read_file:
    clear_list.append(item.strip())

# Making two list (FirstName, LastName)
first_name, last_name = list(),list()
for var_name in clear_list:
    first_name.append(var_name.split()[0])
    last_name.append(var_name.split()[1])

#================================================================================================

# Functions
def allNoOut():
    for i in range(0,len(clear_list)):
        # First.Last
        print("%s%s%s"%(first_name[i].lower(),args['delimiter'],last_name[i].lower()))
        print("%s%s%s"%(first_name[i].upper(),args['delimiter'],last_name[i].upper()))
        print("%s%s%s"%(first_name[i].capitalize(),args['delimiter'],last_name[i].capitalize()))
        # F.Last
        print("%s%s%s"%(first_name[i][0].lower(),args['delimiter'],last_name[i].lower()))
        print("%s%s%s"%(first_name[i][0].upper(),args['delimiter'],last_name[i].upper()))
        print("%s%s%s"%(first_name[i][0].capitalize(),args['delimiter'],last_name[i].capitalize()))
        # First.L
        print("%s%s%s"%(first_name[i].lower(),args['delimiter'],last_name[i][0].lower()))
        print("%s%s%s"%(first_name[i].upper(),args['delimiter'],last_name[i][0].upper()))
        print("%s%s%s"%(first_name[i].capitalize(),args['delimiter'],last_name[i][0].capitalize()))
        # Last.First
        print("%s%s%s"%(last_name[i].lower(),args['delimiter'],first_name[i].lower()))
        print("%s%s%s"%(last_name[i].upper(),args['delimiter'],first_name[i].upper()))
        print("%s%s%s"%(last_name[i].capitalize(),args['delimiter'],first_name[i].capitalize()))
        # L.First
        print("%s%s%s"%(last_name[i][0].lower(),args['delimiter'],first_name[i].lower()))
        print("%s%s%s"%(last_name[i][0].upper(),args['delimiter'],first_name[i].upper()))
        print("%s%s%s"%(last_name[i][0].capitalize(),args['delimiter'],first_name[i].capitalize()))
        # Last.F
        print("%s%s%s"%(last_name[i].lower(),args['delimiter'],first_name[i][0].lower()))
        print("%s%s%s"%(last_name[i].upper(),args['delimiter'],first_name[i][0].upper()))
        print("%s%s%s"%(last_name[i].capitalize(),args['delimiter'],first_name[i][0].capitalize()))
        # First & Last
        print("%s"%(first_name[i]))
        print("%s"%(last_name[i]))
        print("%s %s"%(last_name[i],first_name[i]))
        print("%s %s"%(first_name[i],last_name[i]))


def allOut():
    w = open(args["outfile"],"a")
    for i in range(0,len(clear_list)):  
        # First.Last
        w.writelines("%s%s%s\n"%(first_name[i].lower(),args['delimiter'],last_name[i].lower()))
        w.writelines("%s%s%s\n"%(first_name[i].upper(),args['delimiter'],last_name[i].upper()))
        w.writelines("%s%s%s\n"%(first_name[i].capitalize(),args['delimiter'],last_name[i].capitalize()))
        # F.Last
        w.writelines("%s%s%s\n"%(first_name[i][0].lower(),args['delimiter'],last_name[i].lower()))
        w.writelines("%s%s%s\n"%(first_name[i][0].upper(),args['delimiter'],last_name[i].upper()))
        w.writelines("%s%s%s\n"%(first_name[i][0].capitalize(),args['delimiter'],last_name[i].capitalize()))
        # First.L
        w.writelines("%s%s%s\n"%(first_name[i].lower(),args['delimiter'],last_name[i][0].lower()))
        w.writelines("%s%s%s\n"%(first_name[i].upper(),args['delimiter'],last_name[i][0].upper()))
        w.writelines("%s%s%s\n"%(first_name[i].capitalize(),args['delimiter'],last_name[i][0].capitalize()))
        # Last.First
        w.writelines("%s%s%s\n"%(last_name[i].lower(),args['delimiter'],first_name[i].lower()))
        w.writelines("%s%s%s\n"%(last_name[i].upper(),args['delimiter'],first_name[i].upper()))
        w.writelines("%s%s%s\n"%(last_name[i].capitalize(),args['delimiter'],first_name[i].capitalize()))
        # L.First
        w.writelines("%s%s%s\n"%(last_name[i][0].lower(),args['delimiter'],first_name[i].lower()))
        w.writelines("%s%s%s\n"%(last_name[i][0].upper(),args['delimiter'],first_name[i].upper()))
        w.writelines("%s%s%s\n"%(last_name[i][0].capitalize(),args['delimiter'],first_name[i].capitalize()))
        # Last.F
        w.writelines("%s%s%s\n"%(last_name[i].lower(),args['delimiter'],first_name[i][0].lower()))
        w.writelines("%s%s%s\n"%(last_name[i].upper(),args['delimiter'],first_name[i][0].upper()))
        w.writelines("%s%s%s\n"%(last_name[i].capitalize(),args['delimiter'],first_name[i][0].capitalize()))
        # First & Last
        w.writelines("%s\n"%(first_name[i]))
        w.writelines("%s\n"%(last_name[i]))
        w.writelines("%s %s\n"%(last_name[i],first_name[i]))
        w.writelines("%s %s\n"%(first_name[i],last_name[i]))


#============================================================================================================

# Run
if __name__ == "__main__":
    if (options.outfile):
        allOut()
    else:
        allNoOut()
