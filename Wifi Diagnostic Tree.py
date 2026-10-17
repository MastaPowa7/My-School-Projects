import sys
print("Reboot the computer and try to connect")
Fix1 = input("DId this solve your problem?: ")

if Fix1 == "yes":
     sys.exit
else:
     print("Reboot the router and try to connect")
     Fix1 = input("DId this solve your problem?: ")

if Fix1 == "yes":
     sys.exit
else:
     print("Make sure the cables are plugged in firmly")
     Fix1 = input("DId this solve your problem?: ")

if Fix1 == "yes":
     sys.exit
else:
     print("Move the router to a new location")
     Fix1 = input("DId this solve your problem?: ")

if Fix1 == "yes":
     sys.exit
else:
     print("Get a new router")
     sys.exit