#!/usr/bin/env python3
import pandas as pd
import seaborn as sns
import numpy as np
import ast
import matplotlib.pyplot as plt
from pyecharts.charts import Bar
from pyecharts import options as opts


class PlotFunction:
    def __init__(self, input_path, function_type, target_columns=None, title=None, plot_type=None, output_path=None):
        self.input_path = input_path
        self.data = pd.read_csv(self.input_path) if self.input_path.split(
            '.')[-1] == 'csv' else ""
        self.function_type = function_type if function_type else 'correlation'
        self.columns = list(target_columns.split(',')) if target_columns else self.data.columns
        self.title = title
        self.plot_type = plot_type
        self.output_path = output_path if output_path else self.input_path.rsplit(
            '/', 1)[0]

        # read data from input path
        

    # plot function detail
    def plot_missing_value(self):
        data = self.data
        if len(self.columns) > 1:
            data = self.data[self.columns]
        total_missing_data = data.isnull().sum().sort_values(ascending=False)
        percent_of_missing_data = (data.isnull().sum(
        )/data.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat(
            [
                total_missing_data,
                percent_of_missing_data
            ],
            axis=1,
            keys=['Total', 'Percent']
        )
        # draw total_missing_data bar plot
        bar = (
            Bar(init_opts=opts.InitOpts())
            .add_xaxis(missing_data.index.tolist())
            .add_yaxis('Total', missing_data['Total'].tolist())
            .set_global_opts(title_opts=opts.TitleOpts(title="Missing Value Overview"))
        )
        bar.render(self.output_path+'/_missing_value.html')
        return "Wrote figure to " + self.output_path + "/_missing_value.html' file."

    def plot_correlation(self):
        data=self.data
        if len(self.columns) > 1:
            data = self.data[self.columns]
        # draw heatmap
        corr = data.corr()
        sns.heatmap(
            data=corr,
            annot=True,
            fmt='.2f',
            linewidths=.6,
            cmap='RdYlGn',
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values
        )
        plt.rcParams.update({'font.size': 25})
        fig = plt.gcf()
        plt.title(self.title, fontsize=16)
        fig.set_size_inches(15, 10)
        plt.savefig(self.output_path+'/heatmap.png')
        return "Wrote figure to " + self.output_path + "/heatmap.png' file."

    def plot_distribution(self):
        if len(self.columns) > 1:
            data = self.data[self.columns]
        ax = data.hist(figsize=(40,20))
        fig = ax[0][0].get_figure()
        fig.suptitle(self.title,fontsize=50)
        fig.savefig(self.output_path+'/distribution.png')
        # draw histogram and bar plot
        return "Wrote figure to " + self.output_path + "/distribution.png' file."

    def do_plot(self):
        if self.data.empty:
            return "Error in Reading File: Not a .csv file."
        if self.function_type == 'missing_value':
            return self.plot_missing_value()
        elif self.function_type == 'correlation':
            return self.plot_correlation()
        elif self.function_type == 'distribution':
            return self.plot_distribution()
        else:
            return "Something went wrong."
