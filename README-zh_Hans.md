# **Windlib**

有用的函数库，由SNWCreations创建。

这对每个人都是有用的函数库。

如果您有任何疑问，请给我反馈。

但我可能未及时答复，请原谅我。

#### [English](https://github.com/SNWCreations/windlib/blob/main/README.md) / 简体中文

---

## **用法**

***提示：如果使用 “import windlib” 方法导入我的函数，则下面示例中的函数名称应更改为 “windlib.<函数名称>” 。***

***如果使用 “from windlib import <函数名称>” 方法，则不需要“windlib”前缀。***

### **typeof - 检测变量的类型。**

    例如，我将变量“a”定义为10（这是一个整数，即“int”型），并使用以下方法调用此函数：

    typeof(a)

    该函数返回字符串“int”。

---

### ** check_os - 检查操作系统信息。**

通过 “platform” 模块，将调用参数中提供的系统标签（第一个参数）与当前系统标签进行比较。

函数 “platform.system()” 可能返回一个字符串，该字符串是可用于比较的系统标签。

如果您的python作品支持多个系统，则可以将支持的系统类型合并到一个列表中，然后调用此函数。

    例如，如果某作品支持Windows，Mac OS，Jython（Java虚拟机中的Python）和Linux，则可以将这四个系统的标签定义为support_list：['win32'，'darwin'，'linux'，'Java']

    然后，通过以下方法调用它：

    check_os(support_list)


**默认参数：**

slient - 执行时不生成任何信息。

默认值是true。有效值为True或False。

auto_exit - 如果获取的系统类型不是您想要的，它将根据该变量决定是否终止该进程。

如果该进程终止，将返回错误值“1”。

默认值为False。有效值为True或False。

---

### **os_info - 获取操作系统信息。**

获取有关系统的详细信息，**不包括有关计算机附件的信息。**

完整信息将另存为变量 “os_version” 。

如果 “slient” 参数为False，则在函数运行时生成提示。

---

### **extract - 解压缩文件。**

解压缩文件。

支持“.zip”，“.gz”，“.tar”，“.rar”文件。

下一个版本将支持“ .tar.gz”格式。

支持rar文件需要“rarfile”库。

您可以从 https://sourceforge.net/projects/rarfile.berlios/files/latest/download“ 下载 “rarfile” 库。

如果 “slient” 参数为False，则在函数运行时生成提示。

---

### **get_file-从Internet下载文件。**

从Internet下载文件。

如果 “show_progress” 参数为True，则下载时将显示进度。此参数的默认值为False。

如果 “slient” 参数为False，则在函数运行时生成提示。

---

### **get_os_partition - 获取系统分区的驱动器号。**

获取系统所在分区的驱动器号。

将返回变量“os_partition”。(内容可能是A-Z中任意一个字母)

---

### ** file_exists-检查文件是否存在。**

检查文件是否存在。

如果 “auto_exit” 参数为True，则在找不到目标文件时程序将退出。

如果 “slient” 参数为False，则在函数运行时生成提示。

---

### **find_files_with_the_specified_extension - 在目标文件夹中查找具有指定扩展名的文件。**

在目标文件夹中找到具有指定扩展名的文件，然后将该文件名添加到 **file_list** 列表中。

*参数 “folder” 的默认值为“.” （当前目录）*

“file_type” 变量必须是扩展名，并且不需要带有 “.” 。

例如“txt”，“jar”，“md”，“class”。

不能是“.txt”，“.jar”，“.md”，“.class”。

如果 “slient” 参数为False，则在函数运行时将生成提示。

---

### **find_str_in_file-查找文件中的字符串。**

在文件中查找目标字符串。

“文件名”参数**必须**是有效的文件名（可以是绝对路径或相对路径）。

如果 “slient” 参数为False，则在函数运行时将生成提示。

---

## 版权所有（C）2021 SNWCreations。
