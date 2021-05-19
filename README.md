<h1 align="center">

GDUF_autocheck

</h1>

**广东金融学院易广金健康打卡**
- [x] 支持多人打卡👨‍👩‍👧‍👧
- [x] 支持Server酱微信通知打卡结果💬
- [x] 目前仅支持固定校内打卡🏫（默认地址是肇庆校区，本部的朋友需要到[main.py](main.py)自行改一下地址哈）
- [x] 基于Github Actions定时每日早上8:00自动打卡，完全解放你的设备和服务器✔<br>
- Github Actions会比设定时间延迟1小时左右执行，故本项目的cron设置提早了1小时
- [ ] 正在改善Secrets提交方法！

## 使用方法
- Star并Fork此项目。<br>
[Github fork 别人的项目源作者更新后如何同步更新](https://blog.csdn.net/zhongzunfa/article/details/80344585)
- 进入你的仓库，Settings → Secrets,
- 添加2个 Secrets（利用Secrets解决隐私问题）：

|Name |Value                                                        |
|:----|:------------------------------------------------------------|
|USERS|{"名字":["logintoken","学号"],"名字2":["logintoken2","学号2"]}|
|SCKEY|SCUxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      |

备注：<br>
①理论上USERS项的Value格式填写正确，可添加无限用户<br>
②如何获取[logintoken](如何获取logintoken.pdf) <br>
③如何获取[SCKEY](如何获取SCKEY.pdf)<br>
④添加SCKEY这一步为可选步骤（非必要），不添加不会影响打卡，只是当打卡失败时不会向微信推送失败提醒

## 与我联系
- 有任何问题可以提交[issues](https://github.com/feizao67/GDUF_autocheck/issues/new)  
- QQ交流群：[550758147](https://qm.qq.com/cgi-bin/qm/qr?k=NM9kxBkkvWsNiKx-4y0IzzzpaaXbjGOx&jump_from=webapi)


## 许可
本项目以 MIT 协议开源，详情请见 [LICENSE](LICENSE) 文件。
