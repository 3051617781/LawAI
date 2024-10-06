import json
from pyecharts.charts import Bar
from pyecharts import options as opts

# 读取 JSON 数据
with open('./model_evaluations.json', 'r', encoding='utf-8') as file:
    res = json.load(file)

# 提取模型名称和对应的评分
model_names = ['YuanBao', 'Ours', 'LLaMA-pro', 'LLaMA']
metrics = ['准确性', '逻辑性', '全面性', '适用性', '语言表达']

# 计算每个模型的评分
scores = {model: [res[0][model][metric] for metric in metrics] for model in model_names}

# 创建柱状图
bar = Bar()
bar.add_xaxis(metrics)
for model_name in model_names:
    bar.add_yaxis(model_name, scores[model_name])

# 设置全局配置项
bar.set_global_opts(
    title_opts=opts.TitleOpts(title='模型性能对比'),
    xaxis_opts=opts.AxisOpts(name='评分指标'),
    yaxis_opts=opts.AxisOpts(name='分数'),
    legend_opts=opts.LegendOpts(orient='vertical', pos_top='20%', pos_left='85%')
)

# 渲染图表到 HTML 文件
bar.render('model_performance_comparison.html')