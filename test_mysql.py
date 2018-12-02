import mysqlAPI


while True:
    print("we have 3 functions:")
    print("1. search label and get related twitter ID, filename and the number of images that has downloaded.")
    print("2. search twitter ID and get related labels, filename and the number of images that has downloaded.")
    print("3. search filename and get related twitter ID and labels.")
    print("4. exit.")
    print("Please select an operation")
    s = int(input())
    if s == 1:
        print("Please input the label that you want to search")
        search_key = str(input())
        print("================================================")
        mysqlAPI.search_label(search_key)
        print("================================================")
        print("\n")

    elif s == 2:
        print("Please input the twitter ID that you want to search ")
        search_twid = str(input())
        print("================================================")
        mysqlAPI.search_twiiter_ID(search_twid)
        print("================================================")
        print("\n")

    elif s == 3:
        print("Please input the file name that you want to search ")
        search_file = str(input())
        print("================================================")
        mysqlAPI.search_filename(search_file)
        print("================================================")
        print("\n")
    else:
        break
