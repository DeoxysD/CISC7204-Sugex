# Practice 05：NumPy 一维与二维数组

本文件夹对应 **CISC7204 / IBM Cognitive Class Python 101** 的第五周练习。前面用的是 Python 列表；这一周换成 **NumPy 数组**，用来做向量和矩阵运算（科学计算、数据处理的基础）。

1. **一维数组**：把列表转成 `ndarray`，看 `type` / `shape` / `dtype`，做加减乘、点积、`sin`、画图  
2. **二维数组**：矩阵的形状、取某一行、**按元素相乘**（`A * B`）和 **矩阵乘法**（`np.dot`）

建议顺序：**先看教学 notebook，再做对应的小测验。**

---

## 文件说明

| 文件 | 类型 | 在做什么 |
|------|------|----------|
| `PY0101EN-5-1-Numpy1D.ipynb` | 教学 + 测验 | 一维数组的索引、切片、向量运算、点积、作图 |
| `5.1_notebook_quizz_numpy1d.ipynb` | 测验 | 列表转数组、查看属性、`y = sin(x) + 2` 并画图 |
| `PY0101EN-5-2-Numpy2D.ipynb` | 教学 | 二维数组、Hadamard 积、`np.dot`、转置 |
| `5.2_notebook_quizz_numpy2d.ipynb` | 测验 | 二维数组的属性、取第二行、两种乘法 |

带 `PY0101EN-` 前缀的是课程讲义；带 `notebook_quizz` 的是短测验。  
2D 讲义本身没有空测验格（示例已经写好）；二维练习主要在 `5.2` 测验里。

---

## 练习内容与答案要点

### 1. 一维数组（`5.1`）

```python
a = np.array([1, 2, 3, 4, 5])
type(a)     # numpy.ndarray
a.shape     # (5,)
a.dtype     # 元素类型，例如 int64
a.mean()    # 平均值 3.0
```

函数与作图：

```python
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) + 2
plt.plot(x, y)
```

讲义测验里还会练：

- 向量减法：`u - v`
- 数乘：`-2 * z`
- 对应元素相乘：`a * b`
- 点积：`np.dot(a, b)`  
  两个向量垂直时点积为 **0**（例如 `[1, 0]` 和 `[0, 1]`）；不垂直时不为 0（例如 `[1, 1]` 和 `[0, 1]` 的点积是 `1`）

### 2. 二维数组（`5.2`）

设 `A = np.array([[11, 12], [21, 22], [31, 32]])`：

- `type(A)`、`A.shape`（这里是 `(3, 2)`）、`A.dtype`
- 第二行：`A[1]` 得到 `[21, 22]`（下标从 0 开始）

两种乘法不要混：

| 写法 | 含义 |
|------|------|
| `A * B` | 对应位置相乘（Hadamard 积） |
| `np.dot(A, B)` | 矩阵乘法（行乘列） |

例如 `B` 是单位阵时：`A * B` 会把非对角元素变成 0；`np.dot(A, B)` 得到的还是 `A`。

---

## 怎么运行

1. 需要 Python 3，以及 `numpy`、`matplotlib`：  
   `pip install numpy matplotlib`  
2. 在本文件夹中打开 `.ipynb`，选中代码格后按 **Shift + Enter** 执行。  
3. `%matplotlib inline` 是 Jupyter 专用命令，在 notebook 里运行即可显示图像。
