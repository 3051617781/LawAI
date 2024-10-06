import json
from pyecharts.charts import Pie, Grid
from pyecharts import options as opts

with open('./model_evaluations.json', 'r', encoding='utf-8') as file:
    res = json.load(file)

# 提取模型名称和对应的评分
# model_names_all = ['YuanBao', 'Ours', 'LLaMA-pro', 'LLaMA']
model_names = ['Ours']
metrics = ['准确性', '逻辑性', '全面性', '适用性', '语言表达']

# 创建饼图
pies = []

for model in model_names:
    pie = Pie()
    pie_data = [(metric, res[0][model][metric]) for metric in metrics]
    pie.add("", pie_data)
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title=f'模型指标相对比例')
    )
    # 设置中间半径
    pie.set_series_opts(
        radius=["35%", "70%"],
        label_opts=opts.LabelOpts(formatter="{b}: {d}%")
    )
    pies.append(pie)

# 使用 Grid 组件合并饼图
grid = Grid()
for i, pie in enumerate(pies):
    grid.add(pie, grid_opts=opts.GridOpts(pos_top=i * 300 + 50, pos_left=50))

# 渲染图表到 HTML 文件
grid.render('model_metrics_pie.html')