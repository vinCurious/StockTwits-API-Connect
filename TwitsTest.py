"""
Author: Vinay More

program to connect StockTwits API and returning the "suggested" messages
"""
import urllib.request
import codecs
import json
import datetime

def readfile(input):
    """
    A private function that reads suggested messages from corresponding json

    :param input: company abbreviation at stocktwits
    :return: None
    """
    print("\n--------------------------------------------------------------"+input+"--------------------------------------------------------------")
    reader = codecs.getreader("utf-8")
    url = "https://api.stocktwits.com/api/2/streams/symbol/" + input + ".json"
    datatmp = urllib.request.urlopen(url)
    data = json.load(reader(datatmp))
    lineCounter=0
    buyCounter=0
    minDate=datetime.datetime.today()+datetime.timedelta(days=1)
    maxDate=datetime.datetime.today()

    for line in data['messages']:
        lineCounter=lineCounter+1
        msg = str(line['body'].encode('utf-8'))
        time = str(line['created_at'].encode('utf-8'))

        if(datetime.datetime.strptime((time[2:12]+" "+time[13:21]), '%Y-%m-%d %H:%M:%S')>maxDate):
            maxDate=datetime.datetime.strptime((time[2:12]+" "+time[13:21]), '%Y-%m-%d %H:%M:%S')
        if(datetime.datetime.strptime((time[2:12]+" "+time[13:21]), '%Y-%m-%d %H:%M:%S')<minDate):
            minDate=datetime.datetime.strptime((time[2:12]+" "+time[13:21]), '%Y-%m-%d %H:%M:%S')

        if(msg.find("buy")>0 or msg.find("Buy")>0 or msg.find("BUY")>0):
            buyCounter=buyCounter+1
        print(str(lineCounter)+" "+time[1:]+" "+"Msg: " + msg[1:])
    print("Results for "+input+": ")
    print("BUY COUNT: "+str(buyCounter)+" BUY HIT RATIO: "+str(buyCounter/lineCounter)+" DATETIME RANGE FROM "+str(minDate)+" TO "+str(maxDate))

if __name__ == "__main__":
    """
    The main program calls readfile function for each company
    :return: None
    """
    readfile("SRPT")
    readfile("CLMT")
    readfile("IBM")
    readfile("PYPL")
    readfile("GLD")

