# ddt 自动化测试数据驱动---第三方包，用来做数据和用例分类

# 1）安装对应ddt文件
pip install ddt

# 2)包含内容
三个模块：
data(python当中的普通数据类型：字典、元组、列表)
unpack（用来做数据的解包，把对应的数据自动一个一个进行分割出来）
file_data:数据格式json、yaml（读取出来以字典格式展示）

# 3）应用
3-1）导包
from ddt import ddt, data, unpack

3-2）装饰对应的类 @ddt
3-3）通过准备数据进行用例的执行
data：
方法一
# @data(("hami", "123456"), ("yulisa", "123456"))
# @data(["hami", "123456"], ["yulisa", "123456"])
# @data({"user": "hami", "pwd": "123456"}, {"user": "yulisa","pwd": "123456"})
 方法二
# li = [{"user": "hami", "pwd": "123456"}, {"user": "yulisa","pwd": "123456"}]
#  @data(*li)

file_data:json yaml
读取对应文件路径
# @file_data(r"E:\python-learning\UT\TC\Testlogdata.yaml")
excel文件需要自己封装方法或者重构ddt文件
读取Excel == [{},{},{}]
# @unpack

































