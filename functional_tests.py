from selenium import webdriver

# (1) 初始化Chrome浏览器实例
browser = webdriver.Chrome()

# (2) 打开本地的Django服务器页面
browser.get('http://localhost:8000')

# (3) 检查页面源码中是否包含'Django'字样
assert 'Django' in browser.page_source
