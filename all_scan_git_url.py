import os.path

all_git_urls=[]

flag=False

def once_run():
    global all_git_urls
    global flag

    if not flag:
        if len(all_git_urls) == 0:
            # 判断文件是否存在
            file_path = "urls.txt"
            if not os.path.exists(file_path):
                raise Exception("即不存在url.txt 也不存在all_git_urls")
            with open(file_path, "w") as f:
                all_git_urls = f.readlines()

    flag=True

once_run()
