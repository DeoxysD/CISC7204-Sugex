# Practice 01：Python 入门（打印、类型、字符串）

本文件夹对应 **CISC7204 / IBM Cognitive Class Python 101** 的第一周练习，主题是 Python 最基础的三件事：

1. 用 `print()` 输出文字，并学会写注释  
2. 认识基本数据类型（`int` / `float` / `str` / `bool`），以及类型转换  
3. 对字符串做索引、切片、步长（stride）和常用方法（`upper()`、`find()`、`replace()`）

建议顺序：**先看两份教学 notebook，再做对应的小测验 notebook。**

---

## 文件说明

| 文件 | 类型 | 在做什么 |
|------|------|----------|
| `PY0101EN-1-1-Types.ipynb` | 教学 + 练习 | 第一段 Python：`print`、注释、错误信息、对象类型、表达式与变量 |
| `1.1_notebook_quizz_v2.ipynb` | 测验 | 巩固 `print()`、换行符 `\n`、注释 `#` |
| `1.2_notebook_quizz_types.ipynb` | 测验 | 用 `type()` 查看类型；把字符串转成 `int` 再转成 `bool` |
| `PY0101EN-1-2-Strings.ipynb` | 教学 + 测验 | 字符串定义、正负索引、切片、stride、转义、字符串方法 |
| `1.3_notebook_quizz_String_Operations.ipynb` | 测验 | 切片取前 4 个字符、步长 2、转成大写 |

带 `PY0101EN-` 前缀的是课程讲义（中间穿插练习题）；带 `notebook_quizz` 的是短测验，每题一个空代码格。

---

## 练习内容与答案要点

### 1. Hello World 与注释（`1.1`）

- 单行输出：`print("Hello World")`
- 两行输出：字符串中间用 `\n`，例如 `print("Hello\nWorld")`
- 注释：`#` 后面的文字不会被执行，可以写在代码同一行末尾

### 2. 类型（`1.2` 与 Types 讲义）

- `"Hello World"` 的类型是 `str`
- `"1.1"` 虽然看起来像小数，但带引号，类型仍是 `str`
- `"1"` 可以先 `int("1")` 得到整数 `1`，再 `bool(...)` 得到 `True`（非零为真）
- `/` 是浮点除法（`6 / 2` 的类型是 `float`）；`//` 是整除（`6 // 2` 的类型是 `int`）
- 运算符优先级：`x = 3 + 2 * 2` 得到 `7`；括号会改变顺序：`y = (3 + 2) * 2` 得到 `10`

### 3. 字符串操作（`1.3` 与 Strings 讲义）

设 `Letters = "ABCDEFGHIJK"`：

- 切片 `Letters[0:4]` 得到前四个字符 `"ABCD"`（结束下标不包含）
- 步长 `Good[::2]`：每隔一个字符取一次，可以把 `"GsoAo+d"` 读成 `"Good"`
- `"uppercase".upper()` 得到 `"UPPERCASE"`
- 字符串相加是拼接：`"1" + "2"` 得到 `"12"`，不是数字 3
- `find("snow")` 返回子串第一次出现的下标；`replace("Mary", "Bob")` 做替换

---

## 怎么运行

在本文件夹中打开任意 `.ipynb`，选中代码格后按 **Shift + Enter** 执行。  
Types 讲义里有两格是**故意写错**的（缺少引号、把 `print` 写成 `frint`），用来演示 Python 的报错方式，运行时看到错误是正常的。
