## 用途

这是一个华中师范大学校园网自动登录或者防止掉线的脚本。

它目前可以做这些事：
- 校园网登录，无论是有线网、CCNU、CCNU-AUTO
- 防止掉线，每隔一段时间检查是否掉线
- 掉线重连，如果掉线了，它会自动重新连接

> 注意，一定要保证你的用户名和密码安全，同时在使用时，尽量不要开启代理工具，可能会导致无法访问认证服务器。


稍加修改，他还可以完成一下工作：

- 添加自己的用户名和密码，你可已轻松的将其移植到你的电脑
- 修改process的逻辑，可以完成定时注销、定时连接等功能
- 多修改一点，可以适用于相同登录逻辑的许多学校的校园网登录

## 安装过程

> 你最好有一定的python或者编程相关经验，以确保你能够安装必要组件。

### 1. 安装环境依赖

无论你是什么系统，都应该下载python3的环境，然后确保你有python3环境后，请在控制台中执行：
`pip install selenium`

> PS：我的环境是基于conda的python3.8,你不必和我完全一样

### 2. 安装浏览器驱动

selenium的运行需要浏览器的支持，但是selenium无法直接去操作浏览器，因此需要安装浏览器驱动。

这个浏览器驱动受限于你的浏览器，举例来讲，我的是egde 110版本，所以我需要去下载edge 110版本的驱动。

不同的系统，对这个驱动的处理方式不同。此处不再赘述，请确认你能够通过python+selenium打开百度首页，就说明你的环境装好了。

网上有大量的教程，请使用搜索引擎。

综上，在此步骤，你需要下载相关驱动，并放到合适未知，你可以不配置环境变量，从config.py中可以指定。


### 3. 启动

修改config.py中的配置，主要是驱动地址，是否可视化GUI，用户密码等内容。

控制台执行：
`python main.py 你的username 你的password`

## 后话

- 可能不会再更新，它已经满足我的需求。因为我有电脑在实验室，而这段时间经常断网，导致我得摇人帮我联网。
- 提供一个我的双击启动脚本`ccnu-net-monitor.cmd`，请参考.
- 此项目仅用于交流python学习技巧，禁止长时间运行给学校网络造成负担，作者不对任何恶意行为负责，不对任何针对此代码的修改负责。
