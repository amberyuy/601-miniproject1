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
- The MongoDB database will not show its content until you insert some content. So you can open the `tw_google_API.py` to see how to insert content into MongoDB

#### To get twitter images and labels and `store data into MySQL Database and MongoDB`
        python tw_google_API.py

