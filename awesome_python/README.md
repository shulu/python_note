*  awesome-python3-webapp/  <-- 根目录
*  |
*  +- backup/               <-- 备份目录
*  |
*  +- conf/                 <-- 配置文件
*  |
*  +- dist/                 <-- 打包目录
*  |
*  +- www/                  <-- Web目录，存放.py文件
*  |  |
*  |  +- static/            <-- 存放静态文件
*  |  |
*  |  +- templates/         <-- 存放模板文件
*  |
*  +- ios/                  <-- 存放iOS App工程
*  |
*  +- LICENSE               <-- 代码LICENSE

### 后端API包括：
* 获取日志：```GET /api/blogs```
* 创建日志：``` POST /api/blogs```
* 修改日志：``` POST /api/blogs/:blog_id ```
* 删除日志：``` POST /api/blogs/:blog_id/delete ```
* 获取评论：``` GET /api/comments ```
* 创建评论：``` POST /api/blogs/:blog_id/comments ```
* 删除评论：``` POST /api/comments/:comment_id/delete ```
* 创建新用户：```` POST /api/users ```
* 获取用户：``` GET /api/users ```
###管理页面包括：
* 评论列表页：``` GET /manage/comments ```
* 日志列表页：``` GET /manage/blogs ```
* 创建日志页：``` GET /manage/blogs/create ```
* 修改日志页：``` GET /manage/blogs/ ```
* 用户列表页：``` GET /manage/users ```
### 用户浏览页面包括：
* 注册页：``` GET /register ```
* 登录页：``` GET /signin ```
* 注销页：``` GET /signout ```
* 首页：``` GET / ```
* 日志详情页：``` GET /blog/:blog_id ```