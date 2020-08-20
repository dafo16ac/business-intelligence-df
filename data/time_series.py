import plotly.graph_objs as go
from settings import hotel_data

""" TIME SERIES DATA """
TimeSeriesDate = hotel_data.groupby(['TimeArrival']).mean().copy()

revenues_scatter = go.Scatter(x=TimeSeriesDate.index,
                              y=TimeSeriesDate['TOT_ADR'].rolling(window=3).mean(),
                              name='Tot Revenues per day',
                              line=dict(
                                  color=('#dc3d4f'),
                                  width=1.5, ))

rating_scatter = go.Scatter(x=TimeSeriesDate.index,
                            y=TimeSeriesDate['Rating'].rolling(window=3).mean(),
                            name='Rating',
                            yaxis='y2',
                            line=dict(
                                color=('#3DDCCA'),
                                width=1.5, ))

traces = [rating_scatter, revenues_scatter]

""" SETTINGS LAYOUTS """
layout_scatter_slider = dict(
    # title='Time Series with Rangeslider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=7,
                     label='1w',
                     step='day',
                     stepmode='backward'),
                dict(count=14,
                     label='2w',
                     step='day',
                     stepmode='backward'),
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(visible=True),
        type='date'
    ),
    yaxis=dict(
        title='Tot Rev per day (MA 3d)'
    ),
    yaxis2=dict(
        title='Rating (MA 3d)',
        overlaying='y',
        side='right'
    ),
    legend=dict(orientation="h"),
    height=480,
    # COLOR THEME
    plot_bgcolor="#fafafa",
    paper_bgcolor="#fafafa",
)
