# ﻿学校体温自动上报

---

最近武汉肺炎形势严重，但各方都还在搞形式主义。。比如学校这个天天上报体温，无语。

闲来无事拿着练习python的借口写了个自动化，自动填写体温等信息并提交。

## 免责声明

此脚本只做方便同学打卡之用

会默认与昨日信息相同，且自动生成一正常体温填入。

如有体温不正常或所在地发生变化请立即停用此脚本并如实上报。

如使用此脚本造成不良后果，一切责任由使用人承担，与此脚本作者无关。

```diff

- 使用即为同意以上免责声明！！

- 使用即为同意以上免责声明！！

- 使用即为同意以上免责声明！！

```

使用方法
---

需要python3, selenium以及chromedriver。

我都Push上来了。。除了↑

运行之前自己修改头部的初始信息，将××××××替换成自己的信息即可。默认当天填写情况和昨天一致，~~心理状态为正常。~~

---

**2020.02.20更新：**
现在点击“与昨日相同”后只需再填写体温。

**2020.02.24更新：**
重构垃圾代码，简单封装并加入检查机制和更好的反馈信息。

~~**2020.03.12重大更新：**~~

~~现已完全支持托管模式，托管地址：~~（已停止托管）

~~使用前请仔细阅读使用须知！！！~~

~~使用前请仔细阅读使用须知！！！~~

~~使用前请仔细阅读使用须知！！！~~

**2020.04.07更新：**
取消了托管服务，以后也不会在提供。
但自动化的源码会继续更新。

**2020.04.08更新：**
源码加入填写是否接待境外人员选项

新增邮件提醒服务，使用前请仔细阅读网页上的内容。

邮件提醒开通地址：[点击跳转](http://121.36.100.12:5000)

运行就完了。
