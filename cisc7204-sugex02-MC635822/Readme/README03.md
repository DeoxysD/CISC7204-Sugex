# Practice 03：条件、循环、函数与对象

本文件夹对应 **CISC7204 / IBM Cognitive Class Python 101** 的第三周练习。前两周学的是数据和容器；这一周学的是**控制程序怎么走**：

1. **条件与分支**：用比较、`if` / `else`、`and` / `or` 决定走哪条路  
2. **循环**：用 `for` 遍历、用 `while` 按条件重复  
3. **函数**：把一段逻辑包起来，输入参数、`return` 结果  
4. **类与对象**：用 `class` 描述一类东西（例如一辆车），再创建具体对象、调用方法

建议顺序：**先看教学 notebook，再做对应的小测验。**

---

## 文件说明

| 文件 | 类型 | 在做什么 |
|------|------|----------|
| `PY0101EN-3-1-Conditions.ipynb` | 教学 + 测验 | 比较运算、`if` / `elif` / `else`、逻辑运算 |
| `3.1_notebook_quizz__Conditions_and_Branching.ipynb` | 测验 | 填出使比较为真的值；让 `if` 打印指定句子 |
| `PY0101EN-3-2-Loops.ipynb` | 教学 + 测验 | `range`、`for` 遍历列表、`while` 提前退出 |
| `3.2_notebook_quizz__Loops.ipynb` | 测验 | 用循环打印列表；填出使 `while` 打印 1 到 10 的 `x` |
| `PY0101EN-3-3-Functions.ipynb` | 教学 + 测验 | 定义函数、`return`、局部/全局变量、函数复用 |
| `3.3_notebook_quizz_functions.ipynb` | 测验 | 完成乘法函数 `f`、列表求和函数 `g` |
| `PY0101EN-3-4-Classes.ipynb` | 教学 | 用类描述 Circle / Rectangle，创建对象并调用方法 |
| `3.4_notebook_quizz_objects.ipynb` | 测验 | 创建 `Car` 对象、打印属性、循环调用 `sell()` |

带 `PY0101EN-` 前缀的是课程讲义；带 `notebook_quizz` 的是短测验。  
Classes 讲义本身没有空的测验格（示例已经写好）；对象练习主要在 `3.4` 测验里。

---

## 练习内容与答案要点

### 1. 条件与分支（`3.1`）

- `i > 100` 要为 `True`，`i` 必须大于 100，例如 `i = 101`
- `if x == 'a'` 要打印 `"this is a"`，就把 `x` 设成 `'a'`
- `x > 0 and y < 10` 在 `x = 1` 时，`y` 只要小于 10 即可，例如 `y = 0`
- 专辑评分 `8.5 > 8` 时打印 Amazing；否则走 `else` 打印 ok
- 用 `or` 连接多个年份条件：早于 1980，或正好是 1991 / 1993

### 2. 循环（`3.2`）

- `for a in A:` 依次打印列表元素
- `while(y < x)` 从 `y = 1` 开始，要打印 `1` 到 `10`，`x` 应设为 **11**（因为结束下标不包含：`y` 变成 11 时循环停止）
- `range(-5, 6)` 才会包含两端的 `-5` 和 `5`
- `while` 遇到评分 `< 6` 就退出；拷贝 `'orange'` 时，一旦遇到别的颜色就停

### 3. 函数（`3.3`）

- `f(a, b)` 返回乘积：`return a * b`
- `g(c)` 返回列表元素之和：`return sum(c)`
- `div(a, b)` 返回 `a / b`
- 同一个 `con(a, b)` 用的是 `+`：整数会相加，字符串/列表/元组会拼接

### 4. 对象（`3.4`）

给定 `make="BMW"`、`model="M3"`、`color="red"`：

- 创建对象：`my_car = Car(make, model, color)`
- 查看属性：`my_car.car_info()`
- 循环卖 5 次：`for i in range(5): my_car.sell()`，再调用一次 `car_info()`，`owner_number` 会变成 5

---

## 怎么运行

在本文件夹中打开任意 `.ipynb`，选中代码格后按 **Shift + Enter** 执行。  
Classes 讲义里画矩形/圆需要 `matplotlib`；若环境里没有该库，画图那几格会报错，不影响前面的类定义和属性访问。
