import re


def extract_repo_name(git_url:str)->str:
    """
    从 Git URL 中提取仓库名称
    """
    # 移除协议前缀和.git后缀
    if git_url.endswith('.git'):
        git_url = git_url[:-4]

    # 匹配常见 Git URL 模式
    patterns = [
        r"[:/]([^/:]+?/[^/:]+?)$",  # 匹配 user/repo 格式
        r"/([^/]+?)$"  # 匹配最后一段作为仓库名
    ]

    for pattern in patterns:
        match = re.search(pattern, git_url)
        if match:
            # 获取最后一部分作为仓库名
            full_name = match.group(1)
            # 如果包含路径分隔符，取最后一段
            if '/' in full_name:
                return full_name.split('/')[-1]
            return full_name

    # 如果所有匹配失败，返回最后一部分
    return git_url.split('/')[-1]
