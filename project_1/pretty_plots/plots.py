import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as tick
import matplotlib.lines as mlines

def bar_plot(df, format_function, **info):
    plt.figure(figsize=[15, 10])
    if info['hue']:
        bplot = sns.barplot(x=info['x'], y=info['y'], hue=info['hue'], data=df)
    else:
        bplot = sns.barplot(x=info['x'], y=info['y'], data=df, color='blue')
    for p in bplot.patches:
        if p.get_width() < 1:
            bplot.annotate(f'{float(p.get_width()):.0%}',
                          (p.get_x() + p.get_width() + float(info['x_offset']),
                           p.get_y() + p.get_height() + float(info['y_offset'])),
                           ha='left', size=15)
        else:
            bplot.annotate(f'{int(p.get_width()):,}',
                           (p.get_x() + p.get_width() + float(info['x_offset']),
                            p.get_y() + p.get_height() + float(info['y_offset'])),
                            ha='left', size=15)

    plt.xticks(size=15)
    plt.yticks(size=15)
    plt.xlabel(info['x'].strip().title(), size=15)
    plt.ylabel(info['y'].strip().title(), size=15)
    plt.title(info['title'].strip().title(), size=20)
    bplot.xaxis.set_major_formatter(tick.FuncFormatter(format_function))
    plt.show()

def box_plot_w_means(df, df2, **info):
    if info['showfliers']:
        plt.figure(figsize=[15, 10])
        bplot = sns.boxplot(data=df, x=info['x'], y=info['y_wo_means'], color=info['box_color'], showfliers=info['showfliers'])
        sns.stripplot(x=info['x'], y=info['y_w_means'], data=df2, color=info['mean_color'], dodge=True, size=15, jitter=False)
        plt.xticks(size=15)
        plt.yticks(size=15)
        plt.xlabel(info['xlabel'])
        plt.ylabel(info['ylabel'], size=15)
        plt.title(info['title'], size=15)
        yellow_dot =mlines.Line2D([0], [0], color='white', markerfacecolor=info['mean_color'],
                              marker='o', markersize=15, label='Mean')
        plt.legend(handles=[yellow_dot]);
        plt.show()
    else:
        plt.figure(figsize=[15, 10])
        bplot = sns.boxplot(data=df, x=info['x'], y=info['y_wo_means'], color=info['box_color'], showfliers=info['showfliers'])
        sns.stripplot(x=info['x'], y=info['y_w_means'], data=df2, color=info['mean_color'], dodge=True, size=15, jitter=False)
        plt.xticks(size=15)
        plt.yticks(size=15)
        plt.xlabel(info['xlabel'])
        plt.ylabel(info['ylabel'], size=15)
        plt.title(info['title'], size=15)
        yellow_dot =mlines.Line2D([0], [0], color='white', markerfacecolor=info['mean_color'],
                                  marker='o', markersize=15, label='Mean')
        plt.legend(handles=[yellow_dot]);
        plt.show()

def agg_price_bar_plots(df, **kwargs):
    try:
        g1 = sns.barplot(x=kwargs['x'], y=kwargs['left_y'], hue=kwargs['hue'], data=df,
                         ci=kwargs['ci'], ax=kwargs['left_plot'])
        g2 = sns.barplot(x=kwargs['x'], y=kwargs['right_y'], hue=kwargs['hue'], data=df,
                         ci=kwargs['ci'], ax=kwargs['right_plot'])
        kwargs['figure'].suptitle(kwargs['suptitle'])
        kwargs['left_plot'].set(xlabel=kwargs['left_xlabel'], ylabel=kwargs['left_ylabel'], title=kwargs['left_title'])
        kwargs['right_plot'].set(xlabel=kwargs['right_xlabel'], ylabel=kwargs['right_ylabel'], title=kwargs['right_title'])
        g1.yaxis.set_major_formatter(tick.FuncFormatter(big_mark_formatter))
        g2.yaxis.set_major_formatter(tick.FuncFormatter(big_mark_formatter))
        plt.show()
    except KeyError as e:
        g1 = sns.barplot(x=kwargs['x'], y=kwargs['left_y'], data=df,
                         ci=kwargs['ci'], ax=kwargs['left_plot'], color='blue')
        g2 = sns.barplot(x=kwargs['x'], y=kwargs['right_y'], data=df,
                         ci=kwargs['ci'], ax=kwargs['right_plot'], color='blue')
        kwargs['figure'].suptitle(kwargs['suptitle'])
        kwargs['left_plot'].set(xlabel=kwargs['left_xlabel'], ylabel=kwargs['left_ylabel'], title=kwargs['left_title'])
        kwargs['right_plot'].set(xlabel=kwargs['right_xlabel'], ylabel=kwargs['right_ylabel'], title=kwargs['right_title'])
        g1.yaxis.set_major_formatter(tick.FuncFormatter(big_mark_formatter))
        g2.yaxis.set_major_formatter(tick.FuncFormatter(big_mark_formatter))
        plt.show()

def agg_price_point_plots(df, **info):
    sns.pointplot(x=info['x'], y=info['left_y'], hue=info['hue'], data=df, ci=None, ax=info['left_plot'],
                 join=info['join'])
    info['left_plot'].set_title(info['left_title'])
    info['left_plot'].set(xlabel=info['xlabel'], ylabel=info['left_ylabel'])
    
    sns.pointplot(x=info['x'], y=info['right_y'], hue=info['hue'], data=df, ci=None, ax=info['right_plot'],
                 join=info['join'])
    info['right_plot'].set_title(info['right_title'])
    info['figure'].suptitle(info['suptitle'])
    info['right_plot'].set(xlabel=info['xlabel'], ylabel=info['right_ylabel'])
    plt.show()

def big_mark_formatter(x, y):
    return f'{int(x):,}'

def percent_formatter(x, y):
    return f'{float(x):.0%}'
