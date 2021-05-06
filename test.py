# 未完善的改良
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
    users = input()

    # 调用改良
    # checkinfo = {}
    # get_sectets(users)
    # print(checkinfo)

    # 调用原版
    print(users)
