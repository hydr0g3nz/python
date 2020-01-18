def uploadfile(f):
    import ftplib

    filename =  f   

    ip = "119.59.104.31"
    port = 2002
#login
    ftp = ftplib.FTP()
    ftp.connect(ip,port)
    ftp.login('unclepyd','Uncle1234')

    mypath = '/domains/uncle-pydatabase.com/public_html/hm'

    checkpath = ftp.cwd(mypath)
    files = ftp.nlst()#check file in dir

    fileupload = open(filename,'rb')

    result = ftp.storbinary('STOR ' + filename , fileupload)

    print('result',result)
    print("checkpath",checkpath)
    print("file",files)
uploadfile('airforce.jpg')