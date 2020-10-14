# ManageSystem
HDUHelp 二面的小项目

基于`Django`和`Django rest_framework`，纯后端，给前端提供`api`

数据库可在`SETTINGS`更改

运行前要执行`sh init.sh`初始化从数据库，同时初始化一个管理员账户

使用命令`python manage.py runserver 0.0.0.0:8080`来启动

> `/admin/` 为管理员登录页面，因为没写用户的`app`，所以直接把`admin`放出来吧
>

> `/api/student/create/` 为创建新数据的`api`，方法为`POST`，要求`学号(number)`唯一，若继续添加则返回已存在
>

> `/api/student/get/` 为获取所有学生数据的`api`，方法为`POST`，要求管理员身份，否则不能查询
>

> `/api/student/search/` 为根据个人信息查找室友的`api`，方法为`POST`，要求完整的个人信息，否则不能查询 (不能乱查)
>

> `/api/student/duty/` 为根据寝室查询值日信息的`api`，方法为`POST`，若填写的是楼号和寝室号，则返回所有人的值日数据，若填写的还有值日的星期值，即星期几，则返回当天值日的学生信息
> <br>
> `duty`的值代表了 星期几 ，按照理想情况为 1-7 ，可与前端对接，只能由管理员修改
>

> `/api/student/information/<id>/` 为根据`id`查询、修改数据的`api`，方法为`PUT`，要求管理员身份，否则不能查询或修改
> <br>
> 理想情况为前端先通过`/api/student/get/` 获取学生列表，同时可以获得`id`的值，然后可以直接在前端修改数据，并通过该`api`发送给后端
