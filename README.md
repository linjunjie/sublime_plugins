#Sublime插件集合

我本地是在 OSX 10.9.5 环境下

sublime目录为(基本上是通用的目录地址）：

/Users/andy/Library/Application Support/Sublime Text 2/

sublime自定义插件目录为：

/Users/andy/Library/Application Support/Sublime Text 2/Packages/User/


- addComments.py

如何添加addComments.py?

	1. Tools -> New Plugins
	2. 之后将addComments.py中的代码拷贝进去然后保存（其实这时候文件就自动保存到了自定义插件目录）
	3. Preference -> Key Bindings - User, 然后设置addComments的快捷键，我本地设置如下：
		{ "keys": ["super+i"], "command": "add_comments" },
	4. 你可以发现插件的文件名如果是addComments，那么快捷键中相对应的名称就是add_comments

<或者你也可以直接把文件addComments.py拷贝到自定义插件目录>

然后使用Command+i就可以使用这个功能了 :-)

