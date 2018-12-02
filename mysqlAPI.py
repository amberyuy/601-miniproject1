import pymysql
from collections import Counter


try:
    twdb = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        db="tw"
    )
except Exception:
    print("having trouble connecting MySQL database...")


def search_label(search_key):

    cursor = twdb.cursor()

    sql_s = "SELECT * FROM tw_info WHERE label1 LIKE '%{0}%' or label2 LIKE '%{1}%' or label3 LIKE '%{2}%' or label4 LIKE '%{3}%' or label5 LIKE '%{4}%'".format(search_key, search_key, search_key, search_key, search_key)
    try:
        cursor.execute(sql_s)
        target_s = cursor.fetchall()
        if not target_s:
            print("Can not find this label!")
        for target in target_s:
            twid = target[1]
            img_num = target[2]
            filename = target[3]
            print("The twitter ID that has this label is: ", twid)
            print("The number of images about this ID is: ", img_num)
            print("The filename that has this label is : ", filename)
    except Exception:
        print("Have some error...")


def search_twiiter_ID(search_twid):
    # id = @BU_Tweets,@taylorswift13

    cursor = twdb.cursor()
    # sql_s = "SELECT * FROM tw_info WHERE twID = '@taylorswift13'"
    sql = "SELECT * FROM tw_info WHERE twID LIKE '%{0}%'".format(search_twid)
    try:
        cursor.execute(sql)
        targets = cursor.fetchall()
        if not targets:
            print("Can not find this twitter ID!")
        img_num = targets[0][2]
        print("This twitter ID has {} images".format(img_num))
        print("This image of this twitter ID has labels as below: ")
        for target in targets:
            filename = target[3]
            label1 = target[4]
            label2 = target[5]
            label3 = target[6]
            label4 = target[7]
            label5 = target[8]
            print("file '{0}' has labels: {1}, {2}, {3}, {4}, {5}".format(filename, label1, label2, label3, label4, label5))
    except Exception:
        print("Have some error...")


def search_filename(search_file):
    cursor = twdb.cursor()
    sql = "SELECT * FROM tw_info WHERE filename LIKE '%{0}%'".format(search_file)
    try:
        cursor.execute(sql)
        targets = cursor.fetchall()
        if not targets:
            print("Can not find this filename!")
        for target in targets:
            twid = target[1]
            filename = target[3]
            label1 = target[4]
            label2 = target[5]
            label3 = target[6]
            label4 = target[7]
            label5 = target[8]
            print("Twitter ID is: ", twid)
            print("file '{0}' has labels: {1}, {2}, {3}, {4}, {5}".format(filename, label1, label2, label3, label4, label5))
    except Exception:
        print("Have some error...")


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
