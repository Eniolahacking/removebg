
import mechanize 
def url(site):
link=mechanize.Browser()
you=link.open(site) 
pon=you.read() 
print pon 
sito="http://www.recruitment.psc.gov.ng" 
url(sito)
