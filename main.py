from bs4 import BeautifulSoup as soup
import mechanize

#Find all products by name and do some maths about it
#AVG price, max and min price etc
#Program takes data from morele.net online shop

def find_soup(search):
    #find and return soup of site with searched word
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    #Our request
    url="https://www.morele.net/wyszukiwarka/0/0/,,,,,,,,,,,,/1/?q="+search
    webpage = br.open(url)

    return soup(webpage, "html.parser")

print "\n======================================================"
print "Program works with morlele.net online shop"
print "Welcome in my program what product are you looking for?"
print "------------------------------------------------------"
#get the name of product we'd like to find
search = raw_input("Name: ")
print "======================================================"

search = search.replace(" ","+") #delete all spaces and add '+' for searching

print "\nSearching...\n"

soup = find_soup(search)
#-----------------------------------------------------
#GET soup and make it as a list of prices
data = soup.find_all("div", { "class":"price-new" })
numbers = [d.text for d in data]
#-----------------------------------------------------
length = len(numbers)

#inicialize var's
suma = 0
maximum = 0
minimum = numbers[0]
x=0

for x in range(length):
    #scrapping only for acctual price
    price = numbers[x]
    z = price.find('z')
    price = price[:z]
    price = price.replace(" ","").replace(",",".")
    price = float(price)
    suma+=price
    
    #looking for maximum price of product
    if maximum < price:
        maximum = price

    #looking for minimum price of product
    if minimum > price:
        minimum = price

avg = suma / length
avg = round(avg,2)

#Output with data
print "--------------------------------------------------------------"
print "Avg price: ",avg,"PLN" #print avarage price of product
print "Maximum price: ",maximum,"PLN" #print maximum price of product
print "Minimum price: ",minimum,"PLN" #print maximum price of product
print "--------------------------------------------------------------"
