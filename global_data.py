

default_req={
            "token": "your_token_here",  # 可选字段
            "GitURL": "",  # 必填字段
            "isUseAi": "true",  # 布尔值需转为字符串
            "isUseAiPrompt": "false",
            "aiPrompt": "",  # 可选
            "isReturnBool": "true",
            "aiModel": "deepseek-v3-local-II",  # AI模型名称
            "permissionModel": "permissionModel",  # 权限模型类型
            "projectType": "多角色多权限的后台服务",
            "authenticationCodes": ""  # 注意字段名需加 []
        }

default_target="http://127.0.0.1:8080/findCode/scan"