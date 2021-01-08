import plotly.graph_objs as go
from assets import graph_layouts
from settings import hotel_data, pd

""" DISTRIBUTION CHANNEL VALUES  """
# DISTRIBUTION CHANNEL
TATO = hotel_data.loc[hotel_data['Distribution Channel'] == 'TA/TO']
direct = hotel_data.loc[hotel_data['Distribution Channel'] == 'Direct']
corporate = hotel_data.loc[hotel_data['Distribution Channel'] == 'Corporate']
gds = hotel_data.loc[hotel_data['Distribution Channel'] == 'GDS']

tot_dchannel_perc = hotel_data['Distribution Channel'].count()
TATO_perc = TATO['Distribution Channel'].count()
direct_perc = direct['Distribution Channel'].count()
corporate_perc = corporate['Distribution Channel'].count()
gds_perc = gds['Distribution Channel'].count()

TATO_mean = round(TATO['Additional Expenditures'].mean(), ndigits=1)
direct_mean = round(direct['Additional Expenditures'].mean(), ndigits=1)
corporate_mean = round(corporate['Additional Expenditures'].mean(), ndigits=1)
gds_mean = round(gds['Additional Expenditures'].mean(), ndigits=1)

TATORev_mean = round(TATO['ADR'].mean(), ndigits=1)
directRev_mean = round(direct['ADR'].mean(), ndigits=1)
corporateRev_mean = round(corporate['ADR'].mean(), ndigits=1)
gdsRev_mean = round(gds['ADR'].mean(), ndigits=1)

TATO_rating = round(TATO['Customer Satisfaction Rating'].mean(), ndigits=1)
direct_rating = round(direct['Customer Satisfaction Rating'].mean(), ndigits=1)
corporate_rating = round(corporate['Customer Satisfaction Rating'].mean(), ndigits=1)
gds_rating = round(gds['Customer Satisfaction Rating'].mean(), ndigits=1)

TATO_nights = round(TATO['Nights'].mean(), ndigits=1)
direct_nights = round(direct['Nights'].mean(), ndigits=1)
corporate_nights = round(corporate['Nights'].mean(), ndigits=1)
gds_nights = round(gds['Nights'].mean(), ndigits=1)

TATO_wd = round(TATO['Week Nights'].mean(), ndigits=1)
direct_wd = round(direct['Week Nights'].mean(), ndigits=1)
corporate_wd = round(corporate['Week Nights'].mean(), ndigits=1)
gds_wd = round(gds['Week Nights'].mean(), ndigits=1)

TATO_we = round(TATO['Weekend Nights'].mean(), ndigits=1)
direct_we = round(direct['Weekend Nights'].mean(), ndigits=1)
corporate_we = round(corporate['Weekend Nights'].mean(), ndigits=1)
gds_we = round(gds['Weekend Nights'].mean(), ndigits=1)

TATO_nation_rev = TATO.groupby('Country')['ADR'].mean().sort_values(ascending=False).index[0]
direct_nation_rev = direct.groupby('Country')['ADR'].mean().sort_values(ascending=False).index[0]
corporate_nation_rev = corporate.groupby('Country')['ADR'].mean().sort_values(ascending=False).index[0]
gds_nation_rev = gds.groupby('Country')['ADR'].mean().sort_values(ascending=False).index[0]

TATO_nation_rating = TATO.groupby('Country')['Customer Satisfaction Rating'].mean().sort_values(ascending=False).index[0]
direct_nation_rating = direct.groupby('Country')['Customer Satisfaction Rating'].mean().sort_values(ascending=False).index[0]
corporate_nation_rating = corporate.groupby('Country')['Customer Satisfaction Rating'].mean().sort_values(ascending=False).index[0]
gds_nation_rating = gds.groupby('Country')['Customer Satisfaction Rating'].mean().sort_values(ascending=False).index[0]

TATO_nation_upselling = TATO.groupby('Country')['Additional Expenditures'].mean().sort_values(ascending=False).index[0]
direct_nation_upselling = direct.groupby('Country')['Additional Expenditures'].mean().sort_values(ascending=False).index[0]
corporate_nation_upselling = corporate.groupby('Country')['Additional Expenditures'].mean().sort_values(ascending=False).index[0]
gds_nation_upselling = gds.groupby('Country')['Additional Expenditures'].mean().sort_values(ascending=False).index[0]

columns_dc = ['TA/TO', 'Direct', 'Corporate', 'GDS']
index_dc = ['Upselling mean', 'Revenues mean', 'Rating mean', 'Length staying mean (days)', ' - N° Weekdays',
            ' - N° Weekend days', 'Nationality highest revenues', 'Nationality highest rating',
            'Nationality highest upselling']

table_dc = pd.DataFrame(data=[
    [TATO_mean, direct_mean, corporate_mean, gds_mean],
    [TATORev_mean, directRev_mean, corporateRev_mean, gdsRev_mean],
    [TATO_rating, direct_rating, corporate_rating, gds_rating],
    [TATO_nights, direct_nights, corporate_nights, gds_nights],
    [TATO_wd, direct_wd, corporate_wd, gds_wd],
    [TATO_we, direct_we, corporate_we, gds_we],
    [TATO_nation_rev, direct_nation_rev, corporate_nation_rev, gds_nation_rev],
    [TATO_nation_rating, direct_nation_rating, corporate_nation_rating, gds_nation_rating],
    [TATO_nation_upselling, direct_nation_upselling, corporate_nation_upselling, gds_nation_upselling]
],
    index=index_dc, columns=columns_dc)

table_dchannel = table_dc.reset_index()

table_dchannel1 = go.Table(
    domain=dict(x=[0, 1],
                y=[0, 0.80]),
    columnwidth=[2, 1, 1, 1],
    header=dict(height=20,
                values=[[''], ['<b>TA/TO</b>'],
                        ['<b>Direct</b>'], ['<b>Corporate</b>'], ['<b>GDS</b>']],
                line=dict(color='rgb(50, 50, 50)'),
                align=['left'],
                font=dict(color=['white'] * 5, size=10),
                fill=dict(color='black')),
    cells=dict(values=[table_dchannel[k].tolist() for k in ['index', 'TA/TO', 'Direct', 'Corporate', 'GDS']],
               line=dict(color='#506784'),
               align=['left'] * 5,
               font=dict(color=['rgb(40, 40, 40)'] * 5, size=10),
               height=20,
               fill=dict(color=['#a9efe8', '#eafbf8']))
)

table_dc_title = go.Table(
    domain=dict(x=[0, .28],
                y=[0.8, 0.99]),
    header=dict(height=45,
                values=['Sub-Segments by Distribution Channel'],
                line=dict(color='white'),
                align=['center'],
                font=dict(color=['black'] * 5, size=16),
                fill=dict(color='white')),
)

""" DATA DONUTS DISTRIBUTION CHANNEL """
data_donuts_dc1 = {
    "values": [TATO_perc, tot_dchannel_perc - TATO_perc],
    "title": "{0:.1%}".format(TATO_perc / (tot_dchannel_perc)),
    "labels": ["TA/TO"],
    "textposition": "inside",
    "domain": {'x': [0.3594, 0.46875],
               'y': [0.8135, 1]},
    "name": "TA/TO",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "rotation": 0,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']}
}

data_donuts_dc2 = {
    "values": [direct_perc, tot_dchannel_perc - direct_perc],
    "labels": ["Direct"],
    "title": "{0:.1%}".format(direct_perc / (tot_dchannel_perc)),
    "textposition": "inside",
    "domain": {'x': [0.53125, 0.640625],
               'y': [0.8135, 1]},
    "name": "Direct",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

data_donuts_dc3 = {
    "values": [corporate_perc, tot_dchannel_perc - corporate_perc],
    "title": "{0:.1%}".format(corporate_perc / (tot_dchannel_perc)),
    "labels": ["Corporate"],
    "textposition": "inside",
    "domain": {'x': [0.703125, 0.8125],
               'y': [0.8135, 1]},
    "name": "Corporate",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

data_donuts_dc4 = {
    "values": [gds_perc, tot_dchannel_perc - gds_perc],
    "title": "{0:.1%}".format(gds_perc / (tot_dchannel_perc)),
    "labels": ["GDS"],
    "domain": {'x': [0.875, 1],
               'y': [0.8135, 1]},
    "name": "GDS",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "rotation": 0,
    "direction": "clockwise",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

# Type of upselling
values_upselling_TATO = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR']].loc[
    hotel_data['Distribution Channel'] == 'TA/TO'].sum().copy()
values_upselling_TATO = values_upselling_TATO.tolist()

values_upselling_direct = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR']].loc[
    hotel_data['Distribution Channel'] == 'Direct'].sum().copy()
values_upselling_direct = values_upselling_direct.tolist()

values_upselling_corporate = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR']].loc[
    hotel_data['Distribution Channel'] == 'Corporate'].sum().copy()
values_upselling_corporate = values_upselling_corporate.tolist()

values_upselling_gds = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR']].loc[
    hotel_data['Distribution Channel'] == 'GDS'].sum().copy()
values_upselling_gds = values_upselling_gds.tolist()

values_upselling_dc = [values_upselling_TATO, values_upselling_direct, values_upselling_corporate, values_upselling_gds]

pie_dc_TATO = {
    "values": values_upselling_TATO,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "TA/TO",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_dc_direct = {
    "values": values_upselling_direct,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Direct",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_dc_corporate = {
    "values": values_upselling_corporate,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Corporate",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_dc_gds = {
    "values": values_upselling_gds,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "GDS",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

values_upselling_pie_dc = [pie_dc_TATO, pie_dc_direct, pie_dc_corporate, pie_dc_gds]

""" DISTRIBUTION CHANNEL UPSELLING VALUES """
ups_TATO_restaurant_rev_mean = round(TATO['Restaurant'].mean(), 0)
ups_direct_restaurant_rev_mean = round(direct['Restaurant'].mean(), 0)
ups_corporate_restaurant_rev_mean = round(corporate['Restaurant'].mean(), 0)
ups_gds_restaurant_rev_mean = round(gds['Restaurant'].mean(), 0)

ups_TATO_bar_rev_mean = round(TATO['Bar'].mean(), 0)
ups_direct_bar_rev_mean = round(direct['Bar'].mean(), 0)
ups_corporate_bar_rev_mean = round(corporate['Bar'].mean(), 0)
ups_gds_bar_rev_mean = round(gds['Bar'].mean(), 0)

ups_TATO_breakfast_rev_mean = round(TATO['Breakfast'].mean(), 0)
ups_direct_breakfast_rev_mean = round(direct['Breakfast'].mean(), 0)
ups_corporate_breakfast_rev_mean = round(corporate['Breakfast'].mean(), 0)
ups_gds_breakfast_rev_mean = round(gds['Breakfast'].mean(), 0)

ups_TATO_other_rev_mean = round(TATO['Other'].mean(), 0)
ups_direct_other_rev_mean = round(direct['Other'].mean(), 0)
ups_corporate_other_rev_mean = round(corporate['Other'].mean(), 0)
ups_gds_other_rev_mean = round(gds['Other'].mean(), 0)

ups_TATO = [ups_TATO_restaurant_rev_mean, ups_TATO_bar_rev_mean, ups_TATO_breakfast_rev_mean, ups_TATO_other_rev_mean]
ups_direct = [ups_direct_restaurant_rev_mean, ups_direct_bar_rev_mean, ups_direct_breakfast_rev_mean,
              ups_direct_other_rev_mean]
ups_corporate = [ups_corporate_restaurant_rev_mean, ups_corporate_bar_rev_mean, ups_corporate_breakfast_rev_mean,
                 ups_corporate_other_rev_mean]
ups_gds = [ups_gds_restaurant_rev_mean, ups_gds_bar_rev_mean, ups_gds_breakfast_rev_mean, ups_gds_other_rev_mean]

ups_tot = hotel_data['Additional Expenditures'].sum()

ups_TATO_restaurant_sum = TATO['Restaurant'].sum()
ups_direct_restaurant_sum = direct['Restaurant'].sum()
ups_corporate_restaurant_sum = corporate['Restaurant'].sum()
ups_gds_restaurant_sum = gds['Restaurant'].sum()

ups_TATO_bar_sum = TATO['Bar'].sum()
ups_direct_bar_sum = direct['Bar'].sum()
ups_corporate_bar_sum = corporate['Bar'].sum()
ups_gds_bar_sum = gds['Bar'].sum()

ups_TATO_breakfast_sum = TATO['Breakfast'].sum()
ups_direct_breakfast_sum = direct['Breakfast'].sum()
ups_corporate_breakfast_sum = corporate['Breakfast'].sum()
ups_gds_breakfast_sum = gds['Breakfast'].sum()

ups_TATO_other_sum = TATO['Other'].sum()
ups_direct_other_sum = direct['Other'].sum()
ups_corporate_other_sum = corporate['Other'].sum()
ups_gds_other_sum = gds['Other'].sum()

ups_restaurant_tot = hotel_data['Restaurant'].sum()
ups_bar_tot = hotel_data['Bar'].sum()
ups_breakfast_tot = hotel_data['Breakfast'].sum()
ups_other_tot = hotel_data['Other'].sum()

ups_TATO_restaurant_perc = "{0:.1%}".format(ups_TATO_restaurant_sum / ups_tot)
ups_direct_restaurant_perc = "{0:.1%}".format(ups_direct_restaurant_sum / ups_tot)
ups_corporate_restaurant_perc = "{0:.1%}".format(ups_corporate_restaurant_sum / ups_tot)
ups_gds_restaurant_perc = "{0:.1%}".format(ups_gds_restaurant_sum / ups_tot)

ups_TATO_bar_perc = "{0:.1%}".format(ups_TATO_bar_sum / ups_tot)
ups_direct_bar_perc = "{0:.1%}".format(ups_direct_bar_sum / ups_tot)
ups_corporate_bar_perc = "{0:.1%}".format(ups_corporate_bar_sum / ups_tot)
ups_gds_bar_perc = "{0:.1%}".format(ups_gds_bar_sum / ups_tot)

ups_TATO_breakfast_perc = "{0:.1%}".format(ups_TATO_breakfast_sum / ups_tot)
ups_direct_breakfast_perc = "{0:.1%}".format(ups_direct_breakfast_sum / ups_tot)
ups_corporate_breakfast_perc = "{0:.1%}".format(ups_corporate_breakfast_sum / ups_tot)
ups_gds_breakfast_perc = "{0:.1%}".format(ups_gds_breakfast_sum / ups_tot)

ups_TATO_other_perc = "{0:.1%}".format(ups_TATO_other_sum / ups_tot)
ups_direct_other_perc = "{0:.1%}".format(ups_direct_other_sum / ups_tot)
ups_corporate_other_perc = "{0:.1%}".format(ups_corporate_other_sum / ups_tot)
ups_gds_other_perc = "{0:.1%}".format(ups_gds_other_sum / ups_tot)

ups_TATO_perc = [ups_TATO_restaurant_perc, ups_TATO_bar_perc, ups_TATO_breakfast_perc, ups_TATO_other_perc]
ups_direct_perc = [ups_direct_restaurant_perc, ups_direct_bar_perc, ups_direct_breakfast_perc, ups_direct_other_perc]
ups_corporate_perc = [ups_corporate_restaurant_perc, ups_corporate_bar_perc, ups_corporate_breakfast_perc,
                      ups_corporate_other_perc]
ups_gds_perc = [ups_gds_restaurant_perc, ups_gds_bar_perc, ups_gds_breakfast_perc, ups_gds_other_perc]

index_table_ups = ['Restaurant', 'Bar', 'Breakfast', 'Other']
columns_table_ups = ['Avg Revenues', 'Absolute %']

table_upselling_dc_TATO = pd.DataFrame(index=index_table_ups,
                                       data={'Avg Revenues': ups_TATO, 'Absolute %': ups_TATO_perc},
                                       columns=columns_table_ups).reset_index()
table_upselling_dc_direct = pd.DataFrame(index=index_table_ups,
                                         data={'Avg Revenues': ups_direct, 'Absolute %': ups_direct_perc},
                                         columns=columns_table_ups).reset_index()
table_upselling_dc_corporate = pd.DataFrame(index=index_table_ups,
                                            data={'Avg Revenues': ups_corporate, 'Absolute %': ups_corporate_perc},
                                            columns=columns_table_ups).reset_index()
table_upselling_dc_gds = pd.DataFrame(index=index_table_ups, data={'Avg Revenues': ups_gds, 'Absolute %': ups_gds_perc},
                                      columns=columns_table_ups).reset_index()

table_upselling_dc_TATO1 = graph_layouts.RightTable(table_upselling_dc_TATO).returning_table()
table_upselling_dc_direct1 = graph_layouts.RightTable(table_upselling_dc_direct).returning_table()
table_upselling_dc_corporate1 = graph_layouts.RightTable(table_upselling_dc_corporate).returning_table()
table_upselling_dc_gds1 = graph_layouts.RightTable(table_upselling_dc_gds).returning_table()
traces_ups_dc = [table_upselling_dc_TATO1, table_upselling_dc_direct1, table_upselling_dc_corporate1,
                 table_upselling_dc_gds1]

updatemenus_dc = list(
    [dict(active=-1,
          buttons=list([
              dict(label='TA/TO',
                   method='update',
                   args=[{'visible': [True, False, False, False]}, ]),
              dict(label='Direct',
                   method='update',
                   args=[{'visible': [False, True, False, False]}, ]),
              dict(label='Corporate',
                   method='update',
                   args=[{'visible': [False, False, True, False]}, ]),
              dict(label='GDS',
                   method='update',
                   args=[{'visible': [False, False, False, True]}, ])
          ]),
          direction='down',
          yanchor='top',
          xanchor='left',
          x=0.5,
          y=.95,
          )
     ])
