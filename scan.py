from all_scan_git_url import  all_git_urls
from concurrent.futures import ThreadPoolExecutor
import util
import req
import logger
import os


def scan(git_url:str):
    try:
        request = req.Request(git_url)
        resp=request.request()
    except Exception as e:
        print("[-] 发生了错误，请手动测试 giturl:"+git_url+" 具体的问题是: ",e)
        logger.g_logger.log(git_url)
        return
    repo_name=util.extract_repo_name(git_url)
    with open("result/"+repo_name+"_result.html","w+",encoding="utf-8") as f:
        f.write(resp)




def main():
    # 创建result 目录
    os.mkdir("result")

    # 创建线程池
    thread_pool=ThreadPoolExecutor(max_workers=5)
    for git_url in all_git_urls:
        # 提交扫描任务
        thread_pool.submit(scan,git_url)

    thread_pool.shutdown(wait=True)
    print("[+] 扫描结束")


if __name__ == "__main__":
    main()