'''
Following Code provide you the access to the API
You can run both Epseak and modify the code to access
Other interesting APIs

Created By : Kumar Shubham
Date : 11 Feb 2016

=========================================================
pre requisite of the code

1.requests( sudo pip install requests )
2.json( sudo pip install json )
3.epseak( sudo apt-get install espeak )
4. re
==========================================================
'''  
import requests
import json
import re
import os 

# creating the API class for defining the input
class API(object):
    def __init__(self):
        self.host = "http://52.77.222.248/"
        #self.port = 80

    def call(self,url):
        # Function to send get request with the given url
        
        ## modify it for passing more than one Argument to a given API
        ##(http://52.77.222.248/?image=http://www.showroominfo.in/wp-content/uploads/2014/11/Harley-Davidson-Bike.jpg)
        values = {'image' : url
                 }
        ## urlencode is needed especially when you need to parse more than one value for an API
        ## can be ignored  for only one variable
        r= requests.get(self.host, params = values)
        return r.content 

    def ExceptionHandling(self,url):
        ## Handle the exception in the code
        ## check the status code is OK or not  if so return True otherwise False
        output = json.loads(self.call(url))
        if (int(output['status']['code']) == 404):
            Exception(output[status][msg])
            return False,output

        elif(int(output['status']['code']) == 200):

            return True,output
        else:
            return False,output
            
    def genereateOutput(self,url):

        ## First check the status of the code
        isOk,output=self.ExceptionHandling(url)

        ## running the code only if isOK
        if (isOk):
            
            ## extracting the list of Interest
            output = output['body']['predictions']['classes']
            
            ##sorting the list on the basis of a key
            output = sorted(output, key=lambda k: k['prob']) 


            ## removing the number 
            p = re.compile(ur'n\d*(.*)}')
            list_output_sort = []
            for word in output:
                temp =re.findall(p, str(word))[0]
                list_output_sort.append(temp)
            return list_output_sort
        else:
            return "No Output"


## Function using the class for  extracting the data
def wall_e_See(url):
    wall_e = API()
    return wall_e.genereateOutput(url)

def wall_e_Speak(speak):
    os.system("espeak " + str(speak))

if __name__ ==  "__main__":
   # t = API()
    #saw = wall_e_See('http://www.showroominfo.in/wp-content/uploads/2014/11/Harley-Davidson-Bike.jpg')
    wall_e_Speak("Hello")


