import glob, os, ftplib

# Define connection variables

FTP_HOST = "ftp host"
FTP_USER = "ftp username";
FTP_PASS = "ftp password"

# Fetch file list into list (array)
os.chdir("folder holding data files")
filelist = glob.glob("sd*.csv")

# connect to FTP Server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
ftp.cwd('folder to upload files to')

# upload to FTP Server
mycount = 0

for i in filelist:
 file = filelist[mycount]
 with open(file, "rb") as file:
  ftp.storbinary("STOR %s" % file.name,file)
  print(file.name, " uploaded")
  ftp.dir()
  mycount += 1
ftp.close
