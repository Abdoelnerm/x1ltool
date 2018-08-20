#!/data/data/com.termux/files/usr/bin/python2

import sys, os

path = os.getcwd()
sys.path.append(path)
apt_folder = "/data/data/com.termux/files/usr/etc/apt"
bin = "data/data/com.termux/files/usr/bin"
share = "data/data/com.termux/files/usr/share"

if not os.path.isfile("%s/sources.list" % (apt_folder)):
    print "\n[x] sorry bro. x1l only available on termux.\n"
    sys.exit()

else:
    print "\n[*] installing x1l...\n"
    print "\n[*] installing x1l...\n"
    os.system("cd %s && rm -fr x1l" % (share))
    os.system("cp x1l %s" % (bin))
    os.system("mkdir -p %s/x1l && cp -r core %s/x1l" %
             (share, share))
    os.system("cp -r module %s/x1l && cp -r other %s/x1l" %
             (share, share))
    os.system("apt-get install --assume-yes nmap php curl")
    os.system("pip2 install requests bs4")
    print "\n[*] Done !!! type command x1l to launch x1l\n"
