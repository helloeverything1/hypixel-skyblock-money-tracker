# hypixel-skyblock-money-tracker
Tracks how much money a profile has in their bank and graphs it, as long as they enable the bank api. (you could really use this to track anything from the hypixel api)

If it breaks, try googling it, because I dont know how to code very well.

You need a api key (do /api new) and the profile id of the profile you want to track.
To get the profile id go to https://api.hypixel.net/skyblock/profiles?key=apikey&uuid=uuid and put your api key and the uuid of the player (get the uuid on namemc.com) that has the profile in there, then click on profiles, then open all of the numbers and look for the name of the profile you want to track next to cute_name. Once you find it, look above it and copy its profile id.
![profile id](https://user-images.githubusercontent.com/86126478/152691461-85497243-7503-4dca-acaa-5eb5a0454603.png)

To install just copy all the files from the repo to a folder and install python and then install matplotlib with pip then open main.py in a text editor and put your api key and profile id in the key and profile spots.

Each time the program runs, it gets the amount of money in the bank then puts it in a file called bank.txt along with a number to be the x axis. So if you want to make a long graph of how much money a profile has, you will have to figure out how to make the script run every certain amount of time (I used cron).

To graph that info, run graph.py.

To reset the data open bank.txt and erase everything in it, then open X.txt and set the number to 0.



