import pymysql
from collections import Counter
password = " "
keyword = 'hair'


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


def search_mysqldb(search_key):

    cursor = twdb.cursor()

    sql_s = "SELECT twID FROM tw_labels WHERE label like '%{}%'".format(search_key)
    cursor.execute(sql_s)
    target_s = cursor.fetchall()
    print(target_s)
    no_repeat_target = sorted(set(target_s), key=target_s.index)

    if len(no_repeat_target) > 0:
        print("These are the twitter ID which have the label you search")
        print(no_repeat_target)
    else:
        print("no twitter ID in database has the laber you search")


def get_label_number():

    cursor = twdb.cursor()
    sql_g = "SELECT twID, count(*) FROM tw_labels GROUP BY twID"

    try:
        cursor.execute(sql_g)
        label_number = cursor.fetchall()
    except Exception:
        print("can not found the twitter ID")

    print("The number of labels  twitter ID has:")
    print(label_number)


def get_most_labels(input_label_number):

    cursor = twdb.cursor()
    sql_gm = "SELECT label, count(*) FROM tw_labels GROUP BY label order by count(*) desc limit input_label_number"
    try:
        cursor.execute(sql_gm)
        most_labels = cursor.fetchall()
    except Exception:
        print("can not found labels")
    print("Labels are as below:")
    print(most_labels)


def main():
    print("Please input the keyword that you want to search")
    search_key = str(input())
    print("Please input the number of labels that you want to know ")
    input_label_number = int(input())
    search_mysqldb(search_key)
    get_label_number()
    get_most_labels(input_label_number)


if __name__ == '__main__':
    main()
