import pandas as pd

# 1. 读文件；若列分隔符是逗号且首行就是表头，用默认参数即可
df = pd.read_csv('data.csv', skipinitialspace=True)

# ----------  问题答案  ----------
# 1 每个种族的人数
race_counts = df['race'].value_counts()

# 2 男性平均年龄
male_avg_age = df.loc[df['sex'] == 'Male', 'age'].mean()

# 3 学士学位占比
pct_bachelors = (df['education'] == 'Bachelors').mean() * 100

# 4 高等教育（Bachelors/Masters/Doctorate）且收入>50K 的占比
higher_ed = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
pct_high_ed_50k = (df.loc[higher_ed, 'salary'] == '>50K').mean() * 100

# 5 非高等教育收入>50K 占比
pct_low_ed_50k = (df.loc[~higher_ed, 'salary'] == '>50K').mean() * 100

# 6 每周最低工作小时数
min_hours = df['hours-per-week'].min()

# 7 工作小时数最低人群工资>50K 的比例
min_hours_people = df['hours-per-week'] == min_hours
pct_min_hours_50k = (df.loc[min_hours_people, 'salary'] == '>50K').mean() * 100

# 8 收入>50K 比例最高的国家及其百分比
# 只统计样本数>=10 的国家（避免极端值），可自行调整阈值
country_stats = df[df['salary'] == '>50K']['native-country'].value_counts()
country_total = df['native-country'].value_counts()
valid = country_total >= 10
pct_by_country = (country_stats / country_total * 100).loc[valid]
top_country = pct_by_country.idxmax()
top_pct = pct_by_country.max()

# 9 印度收入>50K 人群中最常见的职业
india_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
top_occ_in_india = india_50k['occupation'].value_counts().idxmax() if not india_50k.empty else 'N/A'

# ----------  打印结果  ----------
print('1 各种族人数：\n', race_counts)
print('2 男性平均年龄：', male_avg_age)
print('3 学士学位占比：', f'{pct_bachelors:.1f}%')
print('4 高等教育且>50K占比：', f'{pct_high_ed_50k:.1f}%')
print('5 非高等教育>50K占比：', f'{pct_low_ed_50k:.1f}%')
print('6 每周最低工作小时：', min_hours)
print('7 最低工时人群>50K比例：', f'{pct_min_hours_50k:.1f}%')
print('8 >50K比例最高国家：', top_country, f'{top_pct:.1f}%')
print('9 印度>50K最受欢迎职业：', top_occ_in_india)
