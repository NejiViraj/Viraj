Welcome in Neji!
===================




> **Note: (For Cloud Storage)**

> - We can not give assurance about security due to hoster's policies.
> - This is package mainly used to upload your file into online world.
> - This will help you to send the your file in directory into online world.
> - This package uses the some extra site in order to cloud store.
> - Transfer will be secured.

### Features

- Cloud storage for free by this module.
- Create Graphical user interface by this module. (Combine web technology and python usage)

# Help
```python
"""
    Run this code for more detailed information
"""
from neji import Help
al = Help()
al.author()
al.version()
al.example()
al.CloudStorage()
al.Frame()
al.OpenPort()
al.PortGui()
```
Here you will get help with example.


# Example
```python
#####################################################
################    Example     #####################
#####################################################
""" imported module"""
from neji import PortGui,OpenPort
from flask import Flask
app = Flask(__name__)

"""checking open random port"""
a = OpenPort().FindOpenPort()

@app.route("/")
def al():
    return "<title>"+str(a)+"</title>Hello World"

# Launch window when server is started, kill server when window killed
PortGui(port=a,width=100,frequency=2).AsyncRun()
# Running asynchronus-ly

# start sever
app.run(port=a,debug=True)


'''
For django like or any localserver, you can use this logic:
1. import respective module
2. start infinite loop too run (don't consider indentation)
    while True:
        a = OpenPort().AnyPortExist(host_="localhost",port_=8080,silent_=False)
        if a:
            break
    PortGui(port=a).AsyncRun()
3. when port get existed, Window will launch
4. server will killed by this module itself for security
5. NOTE :: Giving port number is essential. (start from :5000,max limit of port : 65,535)
'''
```
Title of opened software will determined by title tag.
Icon of software determined by Favicon icon.



# Cloud storage
```python
##############################################
############  CloudStorage   #################
##############################################


a = CloudStorage(file_path,silent=False)
# file_path             ==> Give local file path which you want to upload
# If silent             ==> True -> Does not print anything related it

# # Total method available : 1
    # 1. upload()
"""
ignore indentation
eg.1 -> upload()

    a = CloudStorage("C:\\Users\\Viraj...\\longhorn.tt")
    print(a.upload())

        >> https://...
        # return link
        """
```
Give valid file path, It will upload. (Ingnore indentation)


# PortGui
```python

####################################################
###############   PortGui        ###################
####################################################


a = PortGui(host="localhost",port=8080,fullscreen=False,width=600,height=400,maximized=False,silent=False,frequency=1)
# host                  ==> Give host name -> str
# port                  ==> Give port name -> int
# fullscreen            ==> If you want fullscreen, Make this true -> Boolean
# width                 ==> Give width number -> int
# height                ==> Give height number -> int
# maximized             ==> If you want maximized, Make this true -> Boolean
# silent                ==> If you want silent, Make this true -> Boolean
# frequency             ==> frequecy of check port in second -> float

"""
# # Total method available : 2
    # 1. SyncRun()
    # 2. AsyncRun()

eg.1 -> SyncRun()

    a = PortGui(port=13131).SyncRun()
    # This function use is not recommanded
    # This means synchronus run which blocks your code



eg.2 -> AsyncRun()

    a = PortGui(port=13131).AsyncRun()
    # This function use is recommanded
    # This means Asynchronus run which won't blocks your code
    # Window will launch
    # Server will kill after closing window"""
```


# Frame
```python

#################################################
################    Frame       #################
#################################################


a = Frame()
"""
# # Total method available : 1
    # 1. ChromeHunter()

eg.1  -> ChromeHunter()

    a = Frame().ChromeHunter()
    print(a)

        >> L:\...\chrome.exe -> str
        # return chrome path"""
```



# OpenPort
```python
###############################################
################    OpenPort     ##############
###############################################

a = OpenPort(host='localhost',start_port_number=5500,end_port_number=65000,silent=False)
# host                  ==> Give host name
# start_port_number     ==> Give number from which you want to start port
# end_port_number       ==> Give number from which you want to end (max. limit : "65,535")

"""
# Total methods available : 3
    # 1. AnyPortExist(host_="localhost",port_=8080,silent_=False)
    # 2. FindOpenPort()
    # 3. QuiteServer()

eg.1    -> AnyPortExist(host_="localhost",port_=8080,silent_=False)

    a = OpenPort().AnyPortExist(host_="localhost",port_=8080,silent_=False)
    print(a)
    # if a -> True -> Port is using; else reverse
    # If silent -> True -> Does not print anything related it


eg.2    -> FindOpenPort()
    a = OpenPort().FindOpenPort()
    print(a)
    # This will give port which is open, randomly selected


eg.3    -> QuiteServer()
    a = OpenPort().QuiteServer()
    # This will quite server"""
```




## Code Contributing
Pull requests, we are welcome. For major changes, please open an issue first to discuss what you would like to change. 
Contact us to improvement this package on:
**unanneji@gmail.com** 

your are welcome to our improvement.
Please make sure to update tests as appropriate.


## License
Developed by **Viraj Neji**

Contact on: unanneji@gmail.com (We will try.)

**MIT**

