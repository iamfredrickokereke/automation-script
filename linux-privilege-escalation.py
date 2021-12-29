
#!/usr/bin/env/python3

#####################################################################
#																	#
#		A simple automation tool for Linux Privilege Escalation	#
#																	#
# 		Features:												#
#				* OS, Release, and Kernel information gathering     #
#				* Root service check                                #
#				* SUID-GUID check ('can this user sudo anything?')  #
#				* Check for SUID-GUID abusable binaries             #
#																	#
#####################################################################


def main():
    clear
    check_time()
    check_os()
    check_user()
    exit()



main()
