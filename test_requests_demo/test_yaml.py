import yaml
# 使用yaml.safe_dump生成.yaml文件
def test_yaml():

    env = {
        "default":"dev",
        "test-studio":
        {
            "dev": "127.0.0.1",
            "test": "127.0.0.2"
        }


    }
    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env,stream=f)