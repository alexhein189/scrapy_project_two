from flask import Flask
import subprocess
import os
import json

#Imported spiders which were created for each article
from projectdev.projectdev.spiders.edition import Edition
from projectdev.projectdev.spiders.escape import Escape
from projectdev.projectdev.spiders.cntravelerkudos import Cntravelerkudos
from projectdev.projectdev.spiders.cntraveler import Cntraveler
from projectdev.projectdev.spiders.highlightszimmermann import Highlightszimmermann
from projectdev.projectdev.spiders.monocle import Monocle


from scrapy.crawler import CrawlerProcess
from multiprocessing import Process
path = os.path.dirname(__file__)
app = Flask(__name__)

#list that contains the name of the json files
file_list = ["/edition.json","/escape.json","/cntravelerkudos.json","/cntraveler.json","/highlightszimmermann.json","/monocle.json"]

#methods that start each CrawlerProcess for each spider for every article
def start_edition_process():
    process = CrawlerProcess()
    process.crawl(Edition)
    process.start()

def start_escape_process():
    process = CrawlerProcess()
    process.crawl(Escape)
    process.start()
    
def start_cntravlerkudos_process():
    process = CrawlerProcess()
    process.crawl(Cntravelerkudos)
    process.start()

def start_cntraveler_process():
    process = CrawlerProcess()
    process.crawl(Cntraveler)
    process.start()

def start_highlightszimmermann_process():
    process = CrawlerProcess()
    process.crawl(Highlightszimmermann)
    process.start()
    
def start_monocle_process():
    process = CrawlerProcess()
    process.crawl(Monocle)
    process.start()


#route to the main page of the web application
@app.route('/analysis')
def hello_world():
    if __name__=="__main__":
        
        #list of processes instantiated from each article using the above methods
        process_list_1 = []
        
        #Process library is used to make sure that the methods for 
        #creating the CrawlerProcess for each spider runs asynchronously 
            
        p1=Process(target=start_edition_process)
        process_list_1.append(p1)
        #starts the process which means script is running by itself 
        #and in the back the start_edidition_process() function running in parallel

        p2=Process(target=start_escape_process)
        process_list_1.append(p2)
        # p2.start()
        
        p3=Process(target=start_cntravlerkudos_process)
        process_list_1.append(p3)
        
        p4=Process(target=start_cntraveler_process)
        process_list_1.append(p4)
        
        p5=Process(target=start_highlightszimmermann_process)
        process_list_1.append(p5)
        
        p6=Process(target=start_monocle_process)
        process_list_1.append(p6)
        
        #loop iteratres through the list and starts each process asynchronously
        for p in process_list_1:
            p.start()
        
        #join() makes sure that the code executes the component that loads the contents onto data only when all the
        #crawler processes are done    
        for p in process_list_1:
            p.join()
        

    data_list=[]
    
    #iteratres through the file_list that contains the JSON file names in order to load the data and append it to
    #the data list
    for file in file_list:
        with open(path+file) as items_file:
            data=json.load(items_file)
            data_list.append(data)


    return {'data':data_list}

if __name__ == '__main__':
    app.run(debug=True)
