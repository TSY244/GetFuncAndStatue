# 批量执行

在项目根目录中创建urls.txt 文件
> vim urls.txt

将git url 填写进去

然后只需要执行scan.py 就行
```sh
python3 scan.py 
```

## 定制化
需要在 global_data.py 中填写需要使用的模型等数据


# 处理批量执行的结果
将html 中的结果输出到 process_result.txt 中

```sh 
python3  process_result.py
```



# 处理网页

可以通过将网页下载下来，复制其中的内容，放入input.txt，然后通过 get_result_txt.py 文件进行处理

但是建议使用批量处理html 的的方式处理html