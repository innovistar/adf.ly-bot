from fp.fp import FreeProxy
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import os

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-sh-usage")
url = input(" [URL] ")




def adfly():
	# url = input(" [URL] ")
	try:
		p = FreeProxy(country_id=['US', 'BR'], timeout=0.3, rand=True).get()

		proxy = p[7:]
		print(proxy)
	except:
		pass
	
	proxy_ip_port = str(proxy)
	proxy = Proxy()
	proxy.proxy_type = ProxyType.MANUAL
	proxy.http_proxy = proxy_ip_port
	proxy.ssl_proxy = proxy_ip_port

	capabilities = webdriver.DesiredCapabilities.CHROME
	proxy.add_to_capabilities(capabilities)


# replace 'your_absolute_path' with your chrome binary absolute path
	driver = webdriver.Chrome(desired_capabilities=capabilities)
	

	try:
		driver.get(str(url))
		print ("Cheking the site...................")
	except:
		print ("There is a problem with your internet connention. Try again later")
		pass

	time.sleep(8)
	print ("Clicking Sevices")
	try:
		elemen = driver.find_element_by_xpath("/html/body/div[6]/table/tbody/tr[1]/td/div/div[1]/span[2]/a")
		time.sleep(7) 
		elemen.click()

	except:
		pass
	time.sleep(10)
	driver.quit()

def run():
	# while True:
	print("Press [R] to run bot")
	print("Press [Q] to quit bot")
	i = input("[Bot] :")
	if i == "R":
		while True:
			try:
				adfly()
				time.sleep(20)
			except:
				time.sleep(30)
			continue
	elif i == "Q":
		# break
		quit()
run()