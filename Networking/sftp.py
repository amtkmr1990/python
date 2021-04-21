import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection(cnopts=cnopts, host='sftp.domain.com',username='username',password='Talend@123') as f:
    print(f.listdir())
    


