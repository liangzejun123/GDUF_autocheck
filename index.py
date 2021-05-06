def get_sectets(users):
    while True:
        try:
            info = users.split(',')
            checkinfo[info[0]] = [info[1], info[2]]
            return checkinfo
        except:
            break


if __name__ == "__main__":
    # sectets字段录入
    checkinfo = {}
    users = input()
    get_sectets(users)
    print(checkinfo)
