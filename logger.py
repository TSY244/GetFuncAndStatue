from threading import Lock

class Logger(object):
    def __init__(self,file_name:str):
        self._file_name=file_name
        self._lock=Lock()

        # 对文件进行初始化
        f=open(file_name,"w+",encoding="utf-8")
        f.close()

    def log(self,msg:str):
        with self._lock:
            with open(self._file_name,"a") as f:
                f.write(msg+"\n")

    def log_splicer(self,msgs):
        with self._lock:
            with open(self._file_name,"a") as f:
                for msg in msgs:
                    f.write(msg+"\n")



g_logger=Logger("log.txt")