if __name__ == "__main__":
    # sectets字段录入
    name, loginToken, studentID = [], [], []
    checkinfo = {}
    while True:
        try:
            users = input()
            info = users.split(',')
            name.append(info[0])
            loginToken.append(info[1])
            studentID.append(info[2])
            # checkinfo[name] = [loginToken, studentID]
        except:
            break
    print(name)
