## EC601 mini project 1
### Build a library (preferable in python) that downloads images from a twitter feed, convert them to a video and describe the content of the images in the video.

- Code by python
- Use Twitter API to access the twitter content, use tweepy download images 
- Use FFMPEG to convert images to videos
- Use Google Vision API to describe the content, use pil to label images

## EC601 mini project 3
#### Create MySQL Database
    CREATE TABLE tw_info(
    infoid INT NOT NULL AUTO_INCREMENT,
    twID VARCHAR(40),
    num VARCHAR(20),
    filename VARCHAR(20),
    label1 VARCHAR(40),
    label2 VARCHAR(40),
    label3 VARCHAR(40),
    label4 VARCHAR(40),
    label5 VARCHAR(40),
    primary key (infoid));
    
#### Create MongoDB
- The MongoDB database will not show its content until you insert some content. So the code below is to show the collection.

    client = pymongo.MongoClient("")
    twdb = client.tw
    twitterID = "test"
    img_num = 10
    filename = "test.jpg"
    label1 = "1"
    label2 = "2"
    label3 = "3"
    label4 = "4"
    label5 = "5"
    comm = {"twID": tw_id, "num": img_num, "filename": key, "label1": label1, "label2": label2, "label3": label3, "label4":       label4, "label5": label5]}
    tw_info.insert_one(comm)
