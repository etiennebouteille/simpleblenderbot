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
and paste those lines
```
* * * * * fswebcam /home/pi/SillyTweeter/mypicture.png
* * * * * python /home/pi/SillyTweeter/SillyTweeter.py
``` 
