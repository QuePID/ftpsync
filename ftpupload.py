import glob, os, ftplib

# Define connection variables

FTP_HOST = "put_ftp_hostname_or_ip_here"
FTP_USER = "put_ftp_username_here";
FTP_PASS = "put_ftp_password_here"

# Fetch file list into list (array)
os.chdir("put_path_to_local_folder_here")
filelist = glob.glob("put_filenames_to_upload_with_wildcards_here")
print(filelist)



# connect to FTP Server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
ftp.cwd('put_path_on_ftp_to_place_uploads')
ftp.dir()
# upload to FTP Server
mycount = 0

for i in filelist:
 file = filelist[mycount]
 with open(file, "rb") as file:
  ftp.storbinary("STOR %s" % file.name,file)
  print(file.name, " uploaded")
  ftp.dir()
  mycount += 1
