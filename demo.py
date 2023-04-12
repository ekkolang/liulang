from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 设置 ChromeDriver 路径和浏览器选项
chromedriver_path = 'your_path_to_chromedriver'
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式运行

# 创建 ChromeDriver 实例
driver = webdriver.Chrome(chromedriver_path, options=chrome_options)

# 待查询的序列号列表
serial_numbers = ['21A911879', '21A911880', '21A911881']

# 查询每个序列号的保修到期日期
for sn in serial_numbers:
    # 构建查询网址
    url = f'https://www.inspur.com/eportal/ui?struts.portlet.action=/portlet/download-front!toView.action&pageId=2367231&index=2&product_id=6706&productSN={sn}'

    # 打开网页
    driver.get(url)

    # 提取保修到期日期
    element = driver.find_elements(By.XPATH,'/html/body/div[8]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/dl[6]/dd')

    warranty_date = element.text
    print(f'{sn} 的保修到期日期是 {warranty_date}')

# 关闭浏览器
driver.quit()
