def get_sectets():
    while True:
        try:
            users = Input()
            info = users.split(',')
            checkinfo[info[0]] = [info[1], info[2]]
            return checkinfo
        except:
            break


if __name__ == "__main__":
    # sectets字段录入
    checkinfo = {}
    get_sectets()
    print(checkinfo)
