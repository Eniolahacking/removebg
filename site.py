import mechanize
import sys
import cookielib
browser=mechanize.Browser()
url='http://www.recruitment.psc.gov.ng'
proxy={'http':'128:090:484:839'}
cookioejar=cookielib.LWPCookieJar()
browser.set_proxies(proxy)
browser.set_cookiejar(cookiojar)
you=browser.open(url)
rd=you.read()
inpo=input('chose 1 if it is site url 2 check cookies')
if 1==inpo:
	print(rd)
elif 2==inpo:
     	print(cookioejar)
else:
	sys.exist()
