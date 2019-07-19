class FileHelper:
    def readLines(self,path):
        fh=open(path,'r')
        res=fh.readlines()
        fh.close()
        return res
    def writeLine(self,path,line):
        fh=open(path,'w+')
        fh.write(line)
        fh.close()
        return fh

    def tryclose(self,fh):
        if not fh.closed:
            fh.close()



