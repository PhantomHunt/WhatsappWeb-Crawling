# WhatsappWeb-Crawling
In this project I am crawling Whatsapp Web to retrieve all the chats and media from all contacts.  

# Requirements:
Prior Knowledge of Python and selenium
install selenium- pip install selenium

# Explaination

I am using edge driver. You can use any but must install it and give its .exe path in the driver variable.

I made this code in python3.

I recommend using spider ide with conda environment (Anaconda package). 

I have put in two logics:-

Logic1: Clicking on the contacts one by one and simultaneously crawling the chats for that particular contact.
Logic2:(Recommended) Getting all the contacts first and then searching those contacts and clicking it and then crawling it.

*Note: In both these logics I am able to get only 19 contacts atmost.(Issue)

Open whatsapp web and log into it in the browser(Whose web driver you are using) by scanning QR code before executing script. You have to do this only for first time.

While executing have patience, It will take time as for loop used to scroll is huge. For testing I recommend making its range 250-300.

All the problems in the code are well described in comments and still if you find any difficulty, please whatsapp me -8527467123

