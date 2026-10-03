# Practice 04：读写文件与 Pandas

本文件夹对应 **CISC7204 / IBM Cognitive Class Python 101** 的第四周练习。前面几周处理的是内存里的列表和字典；这一周开始和**外部数据**打交道：

1. **读文本文件**：`open()`、`with`、`read` / `readline` / `readlines`  
2. **写文本文件**：模式 `'w'` 覆盖、`'a'` 追加，以及把一个文件复制到另一个  
3. **Pandas DataFrame**：用表格看数据——取前几行、取某一列、去重、按条件筛选  

建议顺序：**先看两份文件讲义，再做两份 Pandas 测验。**

---

## 文件说明

| 文件 | 类型 | 在做什么 |
|------|------|----------|
| `PY0101EN-4-1-ReadFile.ipynb` | 教学 | 打开文本、读全部/读若干字符/按行读 |
| `Example1.txt` | 数据 | 读文件实验用的三行示例文本 |
| `PY0101EN-4-2-WriteFile.ipynb` | 教学 | 写入、追加、把列表写进文件、复制文件 |
| `4.3_notebook_quizz_pandas.ipynb` | 测验 | `head()` 看前几行、用列名取出一列 |
| `4.4_notebook_quizz_pandas.ipynb` | 测验 | `unique()` 去重、按条件筛选行 |
| `watson-studio.html` | 参考 | IBM Watson Studio 介绍页（不是练习） |

带 `PY0101EN-` 前缀的是课程讲义（代码已经写好）；带 `notebook_quizz` 的是短测验。  
讲义里原来的路径是 IBM 云环境的 `/resources/data/`，已改成本文件夹下的相对路径，方便在本地运行。

---

## 练习内容与答案要点

### 1. 读文件（ReadFile）

- `open(路径, "r")` 得到文件对象；用完要 `close()`  
- 更稳妥的写法是 `with open(...) as file:`，离开缩进块会自动关闭  
- `read()` 读全部；`read(4)` 读接下来 4 个字符；`readline()` 读一行；`readlines()` 得到行组成的列表  

`Example1.txt` 内容是：

```
This is line 1
This is line 2
This is line 3
```

### 2. 写文件（WriteFile）

- `'w'`：从头写，文件不存在就创建，**已有内容会被清空**  
- `'a'`：在末尾追加，不会删掉原来的行  
- 可以把字符串列表循环 `write()` 进去  
- 复制：一边 `open(..., 'r')` 读，一边 `open(..., 'w')` 写  

运行写文件讲义后，本文件夹会出现 `Example2.txt`、`Example3.txt`（由 notebook 生成）。

### 3. Pandas 测验（`4.3` / `4.4`）

设 `df = pd.DataFrame({'a': [...], 'b': [...]})`：

- 前三行：`df.head(3)`（这里的 “plot” 指展示前几行，不是画图）  
- 取列 `'a'`：`df['a']`  
- 列 `'a'` 的不重复值：`df['a'].unique()`  
- 只保留 `a < 2` 的行：`df[df['a'] < 2]`  

---

## 怎么运行

1. 需要 Python 3，以及 `pandas`（`pip install pandas`）。  
2. 在本文件夹中打开 `.ipynb`，选中代码格后按 **Shift + Enter** 执行。  
3. 读/写文件的 notebook 请在 `practice04` 目录下运行，这样 `Example1.txt` 等相对路径才能找到。
