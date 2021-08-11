import requests
import time
import ast
import os


# 易班打卡
def main(checkinfo):
    global date
    date = time.strftime("%Y-%m-%d", time.localtime())
    i = 0
    L = list(checkinfo.keys())
    L.sort()
    while i < len(checkinfo):
        try:
            post(checkinfo["%s" % L[i]][0], checkinfo["%s" % L[i]][1])
        except KeyError:
            tuisong("%s" % L[i], "loginToken过期，请修改")
        else:
            if yb_result["code"] != 0:
                tuisong("%s" % L[i], yb_result["msg"])
        i = i+1
    print("%s 脚本运行完成" % date)


def post(loginToken, address):
    global yb_result
    session = requests.Session()
    url_1 = "http://f.yiban.cn/iapp378946/i/%s" % loginToken
    a = session.get(url=url_1, headers=UA, allow_redirects=False)
    url_2 = a.headers['Location']
    header_loginToken = {"loginToken": "%s" % loginToken}
    b = session.get(url=url_2, headers=header_loginToken,
                    allow_redirects=False)
    url_get = b.headers["Location"]
    c = session.get(url=url_get, headers=UA, allow_redirects=False)
    studentID = c.headers['Location'].split('studentID=')[1]
    url_bind = "https://ygj.gduf.edu.cn/Handler/device.ashx?flag=checkBindDevice"
    bind = session.get(url=url_bind, headers=UA)
    url_save = "https://ygj.gduf.edu.cn/Handler/health.ashx?"
    data_yb_save = {
        "flag": "save",
        "studentID": "%s" % studentID,
        "date": "%s" % date,
        "health": "体温37.3℃以下（正常）",
        "address": "广东省肇庆市端州区七星街靠近广东金融学院肇庆校区",
        "isTouch": "否",
        "isPatient": "不是"
    }
    if not address:
        yb_result = session.post(
            url=url_save, headers=UA, data=data_yb_save).json()
        return yb_result
    else:
        data_yb_save["address"] = address
        yb_result = session.post(
            url=url_save, headers=UA, data=data_yb_save).json()
        return yb_result


# 推送判断
def tuisong(name, error):
    api = "https://api.day.app/%s/易班打卡异常提醒/%s %s?" % (BARK, name, error)
    send = requests.post(url=api)


if __name__ == "__main__":
    # sectets字段录入
    BARK = os.environ["BARK"]
    USERS = os.environ["USERS"]
    USERS = ast.literal_eval(USERS)
    UA = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.10"
    }

    main(USERS)
