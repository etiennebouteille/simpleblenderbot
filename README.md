# simpleblenderbot
A simple bot that will tweet blender pictures from a Raspberry Pi

The `robot` folder goes in `/home/pi/`

To run it you will need blender 2.78 (not test with other version)
```
sudo apt-get install blender
```

You will also need twython

```
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install twython
```

Last thing you need to do is open the crontab 
```
crontab -e
```
and copy those lines
```
0 * * * * sudo python /home/pi/robot/twitterbot.py
1 * * * * blender -b /home/pi/robot/suzanne.blend --python home/pi/robot/mycode.py
``` 

More detailed instructions here : 
https://medium.com/@etienne.bouteille/creating-a-twitter-bot-with-blender-and-a-raspberry-pi-3032660255a
