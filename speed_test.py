import matplotlib 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20) 
matplotlib.rc('font', family='Arial')
import matplotlib.pyplot as plt

from pyplotz.pyplotz import PyplotZ
pltz = PyplotZ()
pltz.enable_chinese()


dic={"StrongVPN":[99,71],"ExpressVPN":[84,15],"Surfshark":[81,6],"FlowVPN":[76,4.7]}


download=[]
upload=[]
price=[]
for i in dic.values():
    upload.append(i[0])
    download.append(i[1])
    #price.append(i[2])
    
s=700
plt.figure(figsize = (10, 6))
plt.scatter(list(dic.keys()), upload,label="download_speed",s=s)
plt.scatter(list(dic.keys()), download,label="upload_speed",s=s)
#plt.scatter(list(dic.keys()), price,label="price",s=s)
plt.legend(fontsize=20)
plt.tight_layout()

pltz.xlabel('不同VPN厂商',fontsize=80)
plt.legend(fontsize=20)
pltz.title("墙知乎测速VPN比较图")
pltz.automate_font_size(scale=1.4)
#plt.savefig('2022-01.png')
#plt.show()


def getImage(path, zoom=1):
    return OffsetImage(plt.imread(path), zoom=zoom)


    
x = [0,10,20,30]
y = [80,100,70,65]
z=[50,60,40,42]

fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(x, y,label="download") 
ax.scatter(x, z,label="upload") 

c = [3+np.random.randint(10), 3+np.random.randint(10),3+np.random.randint(10), 3+np.random.randint(10)]
  
plt.errorbar(x, y, yerr=c, fmt="o")
plt.errorbar(x, z, yerr=c, fmt="o")
    
my_xticks = ['strong','expressvpn','surfshark','flowvpn']
plt.xticks(x, my_xticks)
ax.set_xlabel('VPN',size=60)
ax.set_ylabel('speed',size=60)
pltz.title('墙宇宙 VPN 速度测试, 2023-12',size=70)
pltz.automate_font_size(scale=0.7)
plt.legend(fontsize=20)
plt.savefig('C:/Users/eric/Desktop/aff_folder/hsiav.github.io/image/speed_test/vpn_speed_test.png')



from datetime import datetime, timedelta
def generate_date_range(delay):
    # 使用今天的日期作為結束日期
    end_date = datetime.today()
    end_date = end_date + timedelta(hours= 13)
    # 計算起始日期為結束日期前七天
    start_date = end_date - timedelta(days=delay)

    # 格式化日期範圍字符串
    date_range_string = f"{end_date.year} {start_date.month:02d}/{start_date.day:02d}-{end_date.month:02d}/{end_date.day:02d}"
    
    return date_range_string

# 呼叫函數並打印結果
print(generate_date_range(7))

print(generate_date_range(14))

print(generate_date_range(30))

print(generate_date_range(90))








# for delay in [7, 14, 30, 90]:
#     fig, ax = plt.subplots(figsize=(10,8))
#     ax.scatter(x, y,label="download") 
#     ax.scatter(x, z,label="upload") 

#     c = [3+np.random.randint(10), 3+np.random.randint(10),3+np.random.randint(10), 3+np.random.randint(10)]
    
#     plt.errorbar(x, y, yerr=c, fmt="o")
#     plt.errorbar(x, z, yerr=c, fmt="o")
        
#     my_xticks = ['strong','expressvpn','surfshark','flowvpn']
#     plt.xticks(x, my_xticks)
#     ax.set_xlabel('VPN',size=60)
#     ax.set_ylabel('speed',size=60)
#     pltz.title(f'墙宇宙 {generate_date_range(delay)} VPN 速度测试',size=70)
#     pltz.automate_font_size(scale=0.7)
#     plt.legend(fontsize=20)
#     plt.savefig(f'C:/Users/eric/Desktop/aff_folder/hsiav.github.io/image/speed_test/vpn_speed_test-{delay}.png')



# fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# # 迭代四個子圖，分別繪製數據
# for i, delay in enumerate([7, 14, 30, 90]):
#     row, col = divmod(i, 2)  # 計算子圖的行和列索引
#     ax = axs[row, col]

#     # 繪製下載和上傳的數據
#     ax.scatter(x, y, label="download")
#     ax.scatter(x, z, label="upload")

#     c = [3 + np.random.randint(10), 3 + np.random.randint(10), 3 + np.random.randint(10), 3 + np.random.randint(10)]

#     ax.errorbar(x, y, yerr=c, fmt="o")
#     ax.errorbar(x, z, yerr=c, fmt="o")

#     my_xticks = ['strong', 'expressvpn', 'surfshark', 'flowvpn']
#     ax.set_xticks(x)
#     ax.set_xticklabels(my_xticks)
#     ax.set_xlabel('VPN', size=12)
#     ax.set_ylabel('speed', size=12)
#     ax.set_title(f'墙宇宙 {generate_date_range(delay)} VPN 速度测试', size=14)

# # 調整整體布局
# plt.tight_layout()

# # 保存整張圖
# plt.savefig('C:/Users/eric/Desktop/aff_folder/hsiav.github.io/image/speed_test/vpn_speed_test_combined.png')
# plt.show()


import matplotlib
matplotlib.rc('font', family='Microsoft JhengHei')
# test for chinese
plt.pie([800, 300, 400],labels=['交通', '娛樂', '教育'])


fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# 迭代四個子圖，分別繪製數據
for i, delay in enumerate([7, 14, 30, 90]):

    x = [0,10,20,30]
    y = [80,100,70,65]
    z=[50,60,40,42]


    row, col = divmod(i, 2)  # 計算子圖的行和列索引
    ax = axs[row, col]

    # 繪製下載和上傳的數據
    ax.scatter(x, y, label="download")
    ax.scatter(x, z, label="upload")

    c = [3 + np.random.randint(10), 3 + np.random.randint(10), 3 + np.random.randint(10), 3 + np.random.randint(10)]

    ax.errorbar(x, y, yerr=c, fmt="o")
    ax.errorbar(x, z, yerr=c, fmt="o")

    my_xticks = ['strong', 'expressvpn', 'surfshark', 'flowvpn']
    ax.set_xticks(x)
    ax.set_xticklabels(my_xticks)
    ax.set_xlabel('VPN', size=12)
    ax.set_ylabel('speed', size=12)
    ax.set_title(f'墙宇宙 {generate_date_range(delay)} VPN 速度测试', size=14)

# 調整整體布局
plt.tight_layout()

# 保存整張圖
plt.savefig('C:/Users/eric/Desktop/aff_folder/hsiav.github.io/image/speed_test/vpn_speed_test_combined.png')
#plt.show()





#$$
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

expressvpn_original = [65, 80, 60, 77, 50, 55, 50]
locations = ['North America', 'Europe', 'Oceania', 'Asia', 'C-A', 'South America', 'Africa']
x_pos = [i for i, _ in enumerate(locations)]
np.random.seed(0)  # Ensure reproducibility

def generate_vpn_speeds(base_speeds):
    return [i + np.random.randint(5) - 5 for i in base_speeds]

# VPN names
vpns = ['ExpressVPN', 'StrongVPN', 'Surfshark', 'FlowVPN']

# Colors for different network types
network_colors = {'4G': 'red', '5G': 'green', 'WiFi': 'blue'}

# Generating data for each VPN
data_dict = {}
for vpn in vpns:
    data_dict[vpn] = {
        '4G': generate_vpn_speeds(expressvpn_original),
        '5G': generate_vpn_speeds(expressvpn_original),
        'WiFi': generate_vpn_speeds(expressvpn_original)
    }

# Creating DataFrames for each VPN
dfs = {}
for vpn in vpns:
    dfs[vpn] = pd.DataFrame({
        'Location': locations,
        f'{vpn} 4G': data_dict[vpn]['4G'],
        f'{vpn} 5G': data_dict[vpn]['5G'],
        f'{vpn} WiFi': data_dict[vpn]['WiFi']
    })

# Function to convert DataFrame to Markdown
def df_to_markdown(df, title):
    markdown = f"## {title}\n\n"
    markdown += df.to_markdown(index=False)
    return markdown

# Saving DataFrames to txt files
for vpn in vpns:
    title = f"{vpn} Speeds in Different Network Environments"
    markdown_table = df_to_markdown(dfs[vpn], title)
    with open(f'{vpn}_speeds_table.txt', 'w', encoding='utf-8') as f:
        f.write(markdown_table)

# Plotting
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(14, 24), sharex=True)

# Iterating through each VPN to plot its speed in different network environments
for i, vpn in enumerate(vpns):
    # Extracting speeds for each network type
    speeds_4G = dfs[vpn][f'{vpn} 4G']
    speeds_5G = dfs[vpn][f'{vpn} 5G']
    speeds_WiFi = dfs[vpn][f'{vpn} WiFi']

    # Plotting each network type for the current VPN
    axes[i].plot(x_pos, speeds_4G, color=network_colors['4G'], label=f'{vpn} 4G')
    axes[i].plot(x_pos, speeds_5G, color=network_colors['5G'], label=f'{vpn} 5G')
    axes[i].plot(x_pos, speeds_WiFi, color=network_colors['WiFi'], label=f'{vpn} WiFi')
    
    # Setting the title for each subplot
    axes[i].set_title(f"{vpn} Speeds in Different Network Environments")

    # Setting the labels and legend
    axes[i].set_ylabel("Speed (Mbps)")
    axes[i].legend(fontsize=20)

# Setting the x-axis labels for the last subplot
axes[-1].set_xticks(x_pos)
axes[-1].set_xticklabels(locations)
plt.xlabel("Regions")

# Show the plot
plt.tight_layout()
plt.savefig('C:/Users/eric/Documents/dr-ps.png')
#plt.show()