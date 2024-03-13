# D0020E
This code was created by us using Pycharm by Jetbrains, it is recommended to use this same program to make sure everything works the same. Though other IDEs can be used, ex. Visual Studio code or IDLE.
Download the code and run it in your IDE of choice, make sure you have the lastes python interpreter installed, then install the packages listed bellow. A guide to doing this can be found here: https://packaging.python.org/en/latest/tutorials/installing-packages/ .

pip install scrapy

pip install beautifulsoup4

pip install ujson

pip install serpapi

pip install google-search-results (GÖR EFTER SERAPI)

pip install customtkinter

pip install openpyxl

pip install requests_pkcs12

pip install python-dotenv

After everything is installed, make sure to get an API key for SerpAPI you also need certificates from SCB to get accses to their nece codes if you intend to run the code without changing it to get info on Swedish companies. 

If you intend to change it, change the value of "loc" on line 18 in webCrawlerMain.py to a call to a function that gets company names or just a list of names you want to google. If you wish to recive more websites per company name than 1 then changing the number on line 30 in the same file will fix that. On that same line you can also change the region you want to google in, if you intend to search a region other than stockholm it is recomended you change it. For more info on the googlecs.py file and the google API look at SerpAPIs website, https://serpapi.com/.

If you intend to run the code unchanged and you have aquired the needed APIs and certificates, simply run CompSearch.py and use the window to select nace code group and the region. If you inted to run the code without the certificates from SCB and have made the neccesery changes to webCrawlerMain.py simply run the webCrawler function found inside webCrawlerMain. Note that the input for webCrawler can be changed since the code no longer uses them for the code to work. 


