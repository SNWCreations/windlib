# **Windlib**

警告：此仓库已弃用，请到Gitee上继续查看更新 www.gitee.com/SNWCreations/windlib

有用的函数库，由SNWCreations创建。

这对每个人都是有用的函数库。

如果您有任何疑问，请给我反馈。

但我可能未及时答复，请原谅我。

#### [English](https://github.com/SNWCreations/windlib/blob/main/README.md) / 简体中文

## **用法**

***提示：如果使用 “import windlib” 方法导入我的函数，则下面示例中的函数名称应更改为 “windlib.<函数名称>” 。***

***如果使用 “from windlib import <函数名称>” 方法，则不需要“windlib”前缀。***

---

### **typeof - 检测变量的类型。**

    例如，我将变量“a”定义为10（这是一个整数，即“int”型），并使用以下方法调用此函数：

    typeof(a)

    该函数返回字符串“int”。

---

### **check_os - 检查操作系统信息。**

通过 “platform” 模块，将调用参数中提供的系统标签（第一个参数）与当前系统标签进行比较。

函数 “platform.system()” 可能返回一个字符串，该字符串是可用于比较的系统标签。

如果您的python作品支持多个系统，则可以将支持的系统类型合并到一个列表中，然后调用此函数。

    例如，如果某作品支持Windows，Mac OS，Jython（Java虚拟机中的Python）和Linux，则可以将这四个系统的标签定义为support_list：['win32'，'darwin'，'linux'，'Java']

    然后，通过以下方法调用它：

    check_os(support_list)

---

### **os_info - 获取操作系统信息。**

获取有关系统的详细信息，**不包括有关计算机附件的信息。**

完整信息将作为返回值返回。

---

### **extract - 解压缩文件。**

解压缩文件。

支持“.zip”，“.gz”，“.tar”，“.rar”，“.tar.gz”文件。

如果需要支持rar文件，则需要“rarfile”库。

您可以从 https://sourceforge.net/projects/rarfile.berlios/files/latest/download“ 下载 “rarfile” 库。

---

### **get_file-从Internet下载文件。**

从Internet下载文件。

如果 “show_progress” 参数为True，则下载时将显示进度。此参数的默认值为False。

当下载出错时，会返回'DOWNLOAD_FAILED'。

当下载完成时，目标文件在本地的路径会被返回。

---

### **get_os_partition - 获取系统分区的驱动器号。**

获取系统所在分区的驱动器号。

将返回一个字符串。(内容可能是A-Z中任意一个字母)

---

### **file_or_dir_exists - 检查指定的文件(或文件夹)是否存在。**

检查指定的文件(或文件夹)是否存在。

当目标是目录时，会返回'IS_DIR'。

当目标是文件时，会返回'IS_FILE'。

当函数找不到目标时，会返回'NOT_FOUND'。

当目标不是有效路径是，会返回'TARGET_INVAILD'。

---

### **find_files_with_the_specified_extension - 在目标文件夹中查找具有指定扩展名的文件。**

在目标文件夹中找到具有指定扩展名的文件，然后将该文件名添加到 **file_list** 列表中。

*参数 “folder” 的默认值为“.” （当前目录）*

“file_type” 变量必须是扩展名，并且不需要带有 “.” 。

例如 "txt", "jar", "md", "class"，或 ".txt" ".jar" ".md" ".class".

---

### **find_str_in_file-查找文件中的字符串。**

在文件中查找目标字符串。

“文件名”参数**必须**是有效的文件名（可以是绝对路径或相对路径）。

---

### **copy_file - 复制文件（或文件夹）到指定的目录**

复制文件（或文件夹）到指定的目录。

可以通过列表的方式同时将多个文件复制到指定目录。

---

### **is_it_broken - 检查一个文件（或目录）是否损坏。**

检查一个文件（或目录）是否损坏。

允许调用时通过列表检查大量文件和目录。

若使用列表来检查文件，则可能返回一个列表，里面记录所有损坏文件的路径。

---

### **pushd - 临时切换到一个目录。**

临时切换到一个目录，并在切换前保存当前路径以用于下次调用时返回。

使用方法:

    with pushd(directory):
        #code

---

### **compress_to_zip_file - 压缩一个目录下的所有文件到一个zip文件。**

压缩一个目录下的所有文件到一个zip文件。

使用方法:

    compress_to_zip_file('./a', 'a.zip')

---

### **get_sha1 - 获取一个文件的SHA1校验值**

获取一个文件的SHA1校验值。

使用方法:

    get_sha1('a.txt')

---

### **get_md5 - 获取一个文件的MD5校验值**

获取一个文件的MD5校验值。

使用方法:

    get_md5('a.txt')

---

## 版权所有（C）2021 SNWCreations。
