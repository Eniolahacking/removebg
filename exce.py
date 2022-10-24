
import mechanize 
def url(site):
serve=mechanize.Browser()
you=serve.open(site) 
pon=you.read() 
print pon 
url("http://www.recruitment.psc.gov.ng")
