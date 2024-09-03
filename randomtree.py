import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 加载CSV数据
data = pd.read_csv('./output_csv/merged_flows.csv')

# 打印数据的前几行以确con认加载成功
print(data.head())

# 假设 'label' 是目标标签列，包含'normal'和其他木马分类
X = data.drop(columns=['label'])  # 特征列
y = data['label']  # 标签列

# 检查是否有任何非数值列，如果有则进行编码（可使用get_dummies）
X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)

# 创建随机森林分类器
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# 使用训练数据训练模型
rf_model.fit(X_train, y_train)

# 使用测试集进行预测
y_pred = rf_model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f'模型准确率: {accuracy:.2f}')

# 显示分类报告（包括精确度、召回率、F1-score）
print("分类报告:")
print(classification_report(y_test, y_pred))

# 显示混淆矩阵
print("混淆矩阵:")
print(confusion_matrix(y_test, y_pred))
