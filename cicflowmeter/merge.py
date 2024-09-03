import os
import subprocess
import pandas as pd

# 指定PCAP文件所在的文件夹路径
pcap_folder = "Rats_pcap"
output_folder = "./output_csv"

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 获取所有PCAP文件的列表
pcap_files = [f for f in os.listdir(pcap_folder) if f.endswith('.pcap')]

# 存储所有CSV文件的数据用于合并
csv_list = []

# 处理每个PCAP文件
for pcap_file in pcap_files:
    # 提取文件名（不包含扩展名）作为label
    file_label = os.path.splitext(pcap_file)[0]
    
    # 定义CSV文件的输出路径
    output_csv = os.path.join(output_folder, f"{file_label}.csv")
    
    # 构造cicflowmeter命令
    cmd = f"cicflowmeter -f {os.path.join(pcap_folder, pcap_file)} -c {output_csv}"
    
    # 执行命令行命令
    subprocess.run(cmd, shell=True)
    
    # 读取生成的CSV文件
    df = pd.read_csv(output_csv)
    
    # 在CSV中添加label列
    df['label'] = file_label
    
    # 将处理后的DataFrame添加到列表中
    csv_list.append(df)

# 合并所有CSV文件
merged_df = pd.concat(csv_list)

# 保存最终合并的CSV文件
merged_output_csv = os.path.join(output_folder, "merged_flows.csv")
merged_df.to_csv(merged_output_csv, index=False)

print(f"合并后的CSV文件已保存至: {merged_output_csv}")
