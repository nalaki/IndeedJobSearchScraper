import requests
import json
import csv

#Format &q='exact+phrase'

api_url = 'http://api.indeed.com/ads/apisearch?publisher=##############&v=2&limit=100000&format=json'
#insert your publisher id in place of the ############
j = open('Fortune500PreScrape.csv')
csv_j = csv.reader(j)

TheSet = ['sfsfsdfds'] #Enter your search term as a string
for row in csv_j:
    TheSet.append(row[0])


j.close()

TheSet = set(TheSet)


SearchTerms = TheSet


for Term in SearchTerms:
    SearchTermForSave = Term
    SearchTermForScrape = '"' + SearchTermForSave + '"'
    number = -25
    
    #Creating countries set - List of Countries
    countries = set(['us','ar','au','at','bh','be','br','ca','cl','cn','co','cz','dk','fi','fr','de','gr','hk','hu','in','id','ie','il','it','jp','kr','kw','lu','my','mx','nl','nz','no','om','pk','pe','ph','pl','pt','qa','ro','ru','sa','sg','za','es','se','ch','tw','tr','ae','gb','ve'])
    
    #The actual Scraping
    for SCountry in countries:
        
        Country = SCountry #this is the variable assigned to the country
        
        urlfirst = api_url + '&co=' + Country + '&q=' + SearchTermForScrape
        
        grabforNum = requests.get(urlfirst)
        json_content = json.loads(grabforNum.content)
        print(json_content["totalResults"])
        
        numresults = (json_content["totalResults"])
        # We need to send the request once to pull the number of results. 
        # Our numresults variable must match the actual number of job results to the lower of the 25 increment or the last page will repeat over and over
        
    
    
        for number in range(-25, numresults - 25, 25):  
            url = api_url + '&co=' + Country + '&q=' + SearchTermForScrape + '&latlong=1' + '&start=' + str(number + 25) 
            response = requests.get(url)
            f = open(SearchTermForSave + '_All_Countries' +'.json','a')
            f.write (response.content)
            f.close()
            print numresults , 'left '+' Complete' , url