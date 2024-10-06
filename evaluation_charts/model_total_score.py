import json
from pyecharts.charts import Bar
from pyecharts import options as opts

# 定义权重
weights = {
    '准确性': 0.3,
    '逻辑性': 0.2,
    '全面性': 0.2,
    '适用性': 0.2,
    '语言表达': 0.1
}

with open('./model_evaluations.json', 'r', encoding='utf-8') as file:
    res = json.load(file)

# 提取模型名称和对应的评分
model_names = ['YuanBao', 'Ours', 'LLaMA-pro', 'LLaMA']
metrics = ['准确性', '逻辑性', '全面性', '适用性', '语言表达']

# 计算加权总分
weighted_scores = {model: sum(res[0][model][metric] * weights[metric] for metric in metrics) for model in model_names}

# 创建柱状图
bar = Bar()
bar.add_xaxis(model_names)
bar.add_yaxis("加权总分", list(weighted_scores.values()), bar_width=60)

# 设置全局配置项
bar.set_global_opts(
    title_opts=opts.TitleOpts(title='模型总体得分'),
    # xaxis_opts=opts.AxisOpts(name='【指标】 准确性-0.3 逻辑性-0.2 全面性-0.2 适用性-0.2 语言表达-0.1'),
    yaxis_opts=opts.AxisOpts(name='加权总分'),
    legend_opts=opts.LegendOpts(is_show=False)
)

# 渲染图表到 HTML 文件
bar.render('model_total_score.html')