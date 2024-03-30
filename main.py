'''
测试步骤
1. 启动浏览器
'''
from selenium import webdriver # 从selenium 导入 webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome() # 使用chrome的webdriver，保存在driver变量里
# webdriver.Firefox() # 使用firefox的webdriver

'''
2. 访问测试页面
'''
driver.get('https://baidu.com') # 访问了腾讯首页

'''
3. 精确寻找元素，对元素进行操作
定位策略: css选择器, xpath 等等, 可以查看By都支持什么类型
'''
A = driver.find_element(by=By.CSS_SELECTOR, value='#kw') # css选择器
B = driver.find_element(by=By.XPATH, value='//*[@id="su"]') # xpath

print(A)
print(B)

A.send_keys("北京时间") # 1.输入内容 2.上传文件 3.发送按键
# A.send_keys(Keys.CONTROL + 'c') # 代表ctr + c
B.click() # 左键单机



'''
UI记录：
- 此时此刻浏览器的实际展示效果
- 放在断言前，否则断言失败就不知道出错的页面样式了
'''
sleep(3) # 强制等待1秒
driver.get_screenshot_as_file("page.png") # 获取截图，保存到文件，文件后缀必须是png

'''
断言，是否有预期的情况或者页面出现
需要了解网页渲染过程：加载HTML，加载外部资源css、js、img，异步渲染。页面渲染过程没有办法介入，可以通过监听事件变化或者强制等待一段时间。
'''
html = driver.page_source # 网页的HTML
c = html.count("北京时间") # 统计北京时间出现次数
assert c > 1 , f"断言失败：{c=}" # c > 1 就继续向下执行，否则就执行f"断言失败：{c=}"

'''
4. 关闭浏览器，不通过代码也可以实现关闭浏览器，只要之后没有阻塞性代码即可
'''
driver.quit() # 完全退出浏览器
# driver.close() # 关闭当前窗口

# input() # 阻塞性代码，等待输入
