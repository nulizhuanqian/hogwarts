import pytest
import yaml

# 需要安装yaml插件PyYAML,或使用命令pip install PyYAML，
# 使用yaml.safa_load()函数将和yaml.safe_dump()函数将python值和yaml格式数据互相转换
class TestData:
    # 使用string参数化'a,b'或者"a,b"
    @pytest.mark.parametrize('a,b',yaml.safe_load((open("./datal.yaml"))))
    def test_data(self,a,b):
        print(a+b)
