from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import logger
import os

log=logger.Logger("process_result.log")
result_file = logger.Logger("process_result.txt")

def process_result(html_file_name:str):
    with open(html_file_name, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    result_data=["\nfile_name:"+html_file_name]
    # 遍历文档中的直接子元素
    for func_card in soup.find_all("div", class_="function-card"):
        for func_name_div in func_card.find_all("div", class_="function-name"):
            func_name_and_statue = func_name_div.get_text().replace("函数: ", "").replace("\n", "")
            splited = func_name_and_statue.split(" ")
            ret = [i for i in splited if i != ""]
            if len(ret) != 2:
                msg = f"ret len != 2, ret is {ret}"
                log.log(msg)
                continue
            result_data.append(f"{ret[0]}-{ret[1]}")
    result_data.append("\n\n")
    result_file.log_splicer(result_data)




def main():
    base_path="result"
    file_list = os.listdir(base_path)
    if len(file_list) == 0:
        print(f"[-] {base_path} 没有结果！")
    pool = ThreadPoolExecutor(max_workers=10)
    for file_name in file_list:
        if file_name.endswith(".html"):
            process_result(f"{base_path}/{file_name}")
            # pool.submit(process_result,f"{base_path}/{file_name}")

    pool.shutdown(wait=True)


if __name__=="__main__":
    main()

