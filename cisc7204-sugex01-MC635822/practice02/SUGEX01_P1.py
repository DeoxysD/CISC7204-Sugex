import pandas as pd
from pathlib import Path

# SMILES列表节选
smi_box = [
    "COc1cc(C[C@H]2CO[C@H](c3ccc(O)c(OC)c3)[C@H]2CO)ccc1O",
    "CC(C)Cc1ccc(O)c(OC)c1",
    "Cc1cc(C)nc(NC(C)C)c1",
    "CCCCC(=O)OCC(COC(=O)CCCC)OC(=O)CCCC",
    "CC(C)(C)c1ccccc1",
    "CCOc1ccc(C(=O)Nc2ccccc2)cc1",
    "CC(=O)Nc1ccc(Oc2ccccc2)cc1"
]

# 相似度矩阵
similarity_matrix = [
    [0.0, 0.3170731707317073, 0.09375, 0.045112781954887216, 0.1111111111111111, 0.14678899082568808, 0.14018691588785046],
    [0.3170731707317073, 0.0, 0.21818181818181817, 0.06315789473684211, 0.16981132075471697, 0.14473684210526316, 0.13513513513513514],
    [0.09375, 0.21818181818181817, 0.0, 0.0425531914893617, 0.11320754716981132, 0.09090909090909091, 0.0945945945945946],
    [0.045112781954887216, 0.06315789473684211, 0.0425531914893617, 0.0, 0.03333333333333333, 0.06306306306306306, 0.045454545454545456],
    [0.1111111111111111, 0.16981132075471697, 0.11320754716981132, 0.03333333333333333, 0.0, 0.234375, 0.2459016393442623],
    [0.14678899082568808, 0.14473684210526316, 0.09090909090909091, 0.06306306306306306, 0.234375, 0.0, 0.5538461538461539],
    [0.14018691588785046, 0.13513513513513514, 0.0945945945945946, 0.045454545454545456, 0.2459016393442623, 0.5538461538461539, 0.0]
]


# 获取当前 .py 文件所在目录
current_dir = Path(__file__).parent

# 定义 data 文件夹路径
data_dir = current_dir / "data"

# 如果 data 文件夹不存在则创建
data_dir.mkdir(exist_ok=True)

# 保存 SMILES 列表
smi_df = pd.DataFrame(smi_box, columns=["SMILES"])
smi_df.to_csv(data_dir / "smi_box.csv", index=False)

# 2. 保存相似度矩阵（带行/列标签）
sim_df = pd.DataFrame(
    similarity_matrix,
    index=[f"Mol_{i}" for i in range(len(similarity_matrix))],
    columns=[f"Mol_{i}" for i in range(len(similarity_matrix))]
)
sim_df.to_csv(data_dir / "similarity_matrix.csv")

print(f"Data saved in {data_dir}")