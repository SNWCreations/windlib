# **Windlib 更新日志**

## **v1.9.0**

修复 "compress" 函数中的一个细节错误。

**!重要更改!** 现在, 当解压目标为 rar 但是 rarfile 库未安装时, "extract" 函数会引发 ModuleNotFound 异常。

**!重要更改!** 现在, 当 "get_file" 函数在 下载请求出错 时, 会引发 requests 库的某个原生异常。

**!重要更改!** 现在, 当传入 "get_md5" 或 "get_sha1" 的参数 "path" 不是有效文件时, 会引发和文件有关的异常。

调整 setup.py，修复了依赖库不能安装的问题，增加许可证类型。

## **v1.8.0**

全新的包结构。

给 "find_files_with_the_specified_extension" 函数作细节修复，现在此函数返回的列表中所包含的文件路径会是绝对路径。

**!破坏性更改!** 移除 "file_or_dir_exists" 函数。

修复 README.md 中的 Markdown 语法错误。

## **v1.7.10**

对 v1.7.9 进行紧急修复。

## **v1.7.9**

对 LICENSE 中对作者(也就是我)的称谓进行小修改。

移除 setup.py 中 classifiers 的一个错误项。

移除一些无用的导入模块。

补充说明文档。

对一些函数进行细节修复。

**!破坏性更改!** 小型重构 "compress_to_zip_file" 函数，并将其重命名为 "compress" ，增加对 'tar' 'tar.gz' 格式文件的支持。

## **v1.7.8**

完善 setup.py 的一些信息。

删除 "os_info" "find_str_in_file" 函数。

移除 get_file 函数的 show_progress 参数，调用时直接显示进度条。

给 get_file 函数中的 GET 请求加上伪装UA，防止被某些服务器拦截。

将 HISTORY.md 重命名为 CHANGES.md

文档完全中文化，移除英文文档，Github上的仓库不再更新，转到Gitee仓库持续更新。

## **v1.7.7**

更新 "get_file" 函数。

## **v1.7.6**

优化 "get_sha1" 函数。

添加 "get_md5" 函数。

## **v1.7.5**

修复 "get_file" 函数的一个BUG。

---

## **v1.7.4**

添加 "get_sha1" 函数。

---

## **v1.7.3**

更新 "get_file" 函数。

更新一些函数。

---

## **v1.7.2**

重新编写 "pushd" 函数。

对 \_\_init__.py 格式化

---

## **v1.7.1**

修复一个BUG。

---

## **v1.7.0**

添加 "is_it_broken" "pushd" 和 "compress_to_zip_file" 函数。

对一些函数进行修复。

---

## **v1.6.1**

添加 "file_or_dir_exists" 函数。 (替换 "file_exists" 函数。)

优化一些函数。

---

## **v1.6.0**

添加 "copy_file" 函数。

---

## **v1.5.0**

"extract" 函数现在支持 .tar.gz 格式的压缩文件。

---

## **v1.4.2**

修复 setup.py 的关键问题。

---

## **v1.4.1**

优化 "extract" 函数。

修复 "copy_file" 函数的问题。

---

## **v1.4.0**

添加 "extract" 函数。 (替换 "unzip" 函数)

更新 README.md。

---

## **v1.2.2 - v1.3.0**

没有更新，只是修复和调试。

---

## **v1.2.1**

第一个发布于 PYPI 的版本。

---

## v1.2.1之前的版本去哪了？

v1.2.1之前的版本只是我私人使用，自v1.2.1开始发布于PYPI，但是旧版本不能与我现在的作品兼容，所以没有保留。

---

## 感谢您的使用
