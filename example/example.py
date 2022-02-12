# -*- coding: utf-8 -*-
# file: example.py
# time: 05/02/2022
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

from metric_visualizer import MetricVisualizer
import numpy as np

MV = MetricVisualizer()

trial_num = 5  # number of different trials,
repeat = 10  # number of repeats
metric_num = 3  # number of metrics

for trial in range(trial_num):
    for r in range(repeat):  # repeat the experiments to plot violin or box figure
        metrics = [(np.random.random() + n) for n in range(metric_num)]  # n is metric scale factor
        for i, m in enumerate(metrics):
            MV.add_metric('Metric-{}'.format(i + 1), round(m, 2))
    MV.next_trial()

save_path = None
MV.summary(save_path=save_path)  # save fig into .tex and .pdf format
MV.traj_plot_by_trial(save_path=save_path, xlabel='', axrotation=30)  # save fig into .tex and .pdf format
MV.violin_plot_by_trial(save_path=save_path)  # save fig into .tex and .pdf format
MV.box_plot_by_trial(save_path=save_path)  # save fig into .tex and .pdf format
MV.avg_bar_plot_by_trial(save_path=save_path)  # save fig into .tex and .pdf format
MV.sum_bar_plot_by_trial(save_path=save_path)  # save fig into .tex and .pdf format

save_path = 'example'
MV.summary(save_path=save_path)  # save fig into .tex and .pdf format
MV.traj_plot(save_path=save_path, xlabel='', axrotation=30)  # save fig into .tex and .pdf format
MV.violin_plot(save_path=save_path)  # save fig into .tex and .pdf format
MV.box_plot(save_path=save_path)  # save fig into .tex and .pdf format
MV.avg_bar_plot(save_path=save_path)  # save fig into .tex and .pdf format
MV.sum_bar_plot(save_path=save_path)  # save fig into .tex and .pdf format

# save_path = None
# MV.summary(save_path=save_path)  # save fig into .tex and .pdf format
# MV.traj_plot_by_metric(save_path=save_path, xlabel='', axrotation=30)  # save fig into .tex and .pdf format
# MV.violin_plot_by_metric(save_path=save_path)  # save fig into .tex and .pdf format
# MV.box_plot_by_metric(save_path=save_path)  # save fig into .tex and .pdf format
# MV.avg_bar_plot_by_metric(save_path=save_path)  # save fig into .tex and .pdf format
# MV.sum_bar_plot_by_metric(save_path=save_path)  # save fig into .tex and .pdf format
