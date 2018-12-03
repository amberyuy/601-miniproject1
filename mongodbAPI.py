import pymongo

client = pymongo.MongoClient("")

twdb = client.tw  # database
tw_info = twdb.twinfo  # collection


def search_label(search_key):

    nosql = {'$or': [{"label1": (search_key)}, {"label2": (search_key)}, {"label3": (search_key)}, {"label4": (search_key)}, {"label5": (search_key)}]}
    target_s = twdb.twinfo.find(nosql)
    # target_s = twdb.twinfo.find({'$or': [{"label1": (search_key)}]})

    if not target_s:
        print("Can not find this label!")
    for target in target_s:
        for key, value in target.items():
            twid = target['twID']
            img_num = target['num']
            filename = target['filename']
            print("=======================================================")
            print("The twitter ID that has this label is: ", twid)
            print("The number of images about this ID is: ", img_num)
            print("The filename that has this label is : ", filename)


def search_twiiter_ID(search_twid):
    # id = @BU_Tweets,@taylorswift13
    target_s = twdb.twinfo.find({"twID": (search_twid)})
    if not target_s:
        print("Can not find this twitter ID!")
    img_num = target_s[0]['num']
    print("This twitter ID has {} images".format(img_num))

    for target in target_s:
        print("=======================================================")
        print("This image of this twitter ID has labels as below: ")
        for key, value in target.items():
            filename = target['filename']
            label1 = target['label1']
            label2 = target['label2']
            label3 = target['label3']
            label4 = target['label4']
            label5 = target['label5']
        print("file '{0}' has labels: {1}, {2}, {3}, {4}, {5}".format(filename, label1, label2, label3, label4, label5))


def search_filename(search_file):
    target_s = twdb.twinfo.find({"filename": (search_file)})
    if not target_s:
        print("Can not find this filename!")
    for target in target_s:
        for key, value in target.items():
            twid = target['twID']
            filename = target['filename']
            label1 = target['label1']
            label2 = target['label2']
            label3 = target['label3']
            label4 = target['label4']
            label5 = target['label5']
        print("=======================================================")
        print("Twitter ID is: ", twid)
        print("file '{0}' has labels: {1}, {2}, {3}, {4}, {5}".format(filename, label1, label2, label3, label4, label5))


def main():
    # print("Please input the label that you want to search")
    # search_key = str(input())
    # search_label(search_key)
    # print("Please input the twitter ID that you want to search ")
    # search_twid = str(input())
    # search_twiiter_ID(search_twid)
    print("Please input the file name that you want to search ")
    search_file = str(input())
    search_filename(search_file)


if __name__ == '__main__':
    main()
