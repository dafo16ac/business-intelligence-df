import plotly.graph_objs as go
from assets import graph_layouts
from settings import hotel_data, pd

""" AGE VALUES """
hotel_data['Age'] = hotel_data['Age'].round(0).copy()

children = hotel_data.loc[hotel_data['Age'] < 18]
adults_32 = hotel_data.loc[(18 <= hotel_data['Age']) & (hotel_data['Age'] <= 32)]
adults_48 = hotel_data.loc[(33 <= hotel_data['Age']) & (hotel_data['Age'] <= 48)]
adults_66 = hotel_data.loc[(49 <= hotel_data['Age']) & (hotel_data['Age'] <= 66)]
adults_plus = hotel_data.loc[hotel_data['Age'] > 66]

tot_age_perc = hotel_data['Age'].count()
children_perc = children['Age'].count()
adults_32_perc = adults_32['Age'].count()
adults_48_perc = adults_48['Age'].count()
adults_66_perc = adults_66['Age'].count()
adults_plus_perc = adults_plus['Age'].count()

children_mean = round(children['Upselling'].mean(), ndigits=1)
adults_32_mean = round(adults_32['Upselling'].mean(), ndigits=1)
adults_48_mean = round(adults_48['Upselling'].mean(), ndigits=1)
adults_66_mean = round(adults_66['Upselling'].mean(), ndigits=1)
adults_plus_mean = round(adults_plus['Upselling'].mean(), ndigits=1)

childrenRev_mean = round(children['Revenues by day'].mean(), ndigits=1)
youngRev_32_mean = round(adults_32['Revenues by day'].mean(), ndigits=1)
adultsRev_48_mean = round(adults_48['Revenues by day'].mean(), ndigits=1)
adultsRev_66_mean = round(adults_66['Revenues by day'].mean(), ndigits=1)
adultsRev_plus_mean = round(adults_plus['Revenues by day'].mean(), ndigits=1)

children_rating = round(children['Rating'].mean(), ndigits=1)
adults_32_rating = round(adults_32['Rating'].mean(), ndigits=1)
adults_48_rating = round(adults_48['Rating'].mean(), ndigits=1)
adults_66_rating = round(adults_66['Rating'].mean(), ndigits=1)
adults_plus_rating = round(adults_plus['Rating'].mean(), ndigits=1)

children_nights = round(children['Nights'].mean(), ndigits=1)
adults_32_nights = round(adults_32['Nights'].mean(), ndigits=1)
adults_48_nights = round(adults_48['Nights'].mean(), ndigits=1)
adults_66_nights = round(adults_66['Nights'].mean(), ndigits=1)
adults_plus_nights = round(adults_plus['Nights'].mean(), ndigits=1)

children_wd = round(children['StaysInWeekNights'].mean(), ndigits=1)
adults_32_wd = round(adults_32['StaysInWeekNights'].mean(), ndigits=1)
adults_48_wd = round(adults_48['StaysInWeekNights'].mean(), ndigits=1)
adults_66_wd = round(adults_66['StaysInWeekNights'].mean(), ndigits=1)
adults_plus_wd = round(adults_plus['StaysInWeekNights'].mean(), ndigits=1)

children_we = round(children['StaysInWeekendNights'].mean(), ndigits=1)
adults_32_we = round(adults_32['StaysInWeekendNights'].mean(), ndigits=1)
adults_48_we = round(adults_48['StaysInWeekendNights'].mean(), ndigits=1)
adults_66_we = round(adults_66['StaysInWeekendNights'].mean(), ndigits=1)
adults_plus_we = round(adults_plus['StaysInWeekendNights'].mean(), ndigits=1)

children_nation_rev = children.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
adults_32_nation_rev = adults_32.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
adults_48_nation_rev = adults_48.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
adults_66_nation_rev = adults_66.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
adults_plus_nation_rev = adults_plus.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]

children_nation_rating = children.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
adults_32_nation_rating = adults_32.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
adults_48_nation_rating = adults_48.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
adults_66_nation_rating = adults_66.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
adults_plus_nation_rating = adults_plus.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]

children_nation_upselling = children.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
adults_32_nation_upselling = adults_32.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
adults_48_nation_upselling = adults_48.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
adults_66_nation_upselling = adults_66.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
adults_plus_nation_upselling = adults_plus.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]

columns_age = ['children', 'adults_32', 'adults_48', 'adults_66', 'adults_plus']
index_age = ['Cross-selling mean', 'Revenues mean', 'Rating mean', 'Length staying mean (days)', ' - N° Weekdays',
             ' - N° Weekend days', 'Nationality highest revenues', 'Nationality highest rating',
             'Nationality highest upselling']

table_a = pd.DataFrame(data=[
    [children_mean, adults_32_mean, adults_48_mean, adults_66_mean, adults_plus_mean],
    [childrenRev_mean, youngRev_32_mean, adultsRev_48_mean, adultsRev_66_mean, adultsRev_plus_mean],
    [children_rating, adults_32_rating, adults_48_rating, adults_66_rating, adults_plus_rating],
    [children_nights, adults_32_nights, adults_48_nights, adults_66_nights, adults_plus_nights],
    [children_wd, adults_32_wd, adults_48_wd, adults_66_wd, adults_plus_wd],
    [children_we, adults_32_we, adults_48_we, adults_66_we, adults_plus_we],
    [children_nation_rev, adults_32_nation_rev, adults_48_nation_rev, adults_66_nation_rev, adults_plus_nation_rev],
    [children_nation_rating, adults_32_nation_rating, adults_48_nation_rating, adults_66_nation_rating,
     adults_plus_nation_rating],
    [children_nation_upselling, adults_32_nation_upselling, adults_48_nation_upselling, adults_66_nation_upselling,
     adults_plus_nation_upselling]

],
    index=index_age, columns=columns_age)

table_age = table_a.reset_index()

table_age1 = go.Table(
    domain=dict(x=[0, 1],
                y=[0.71, .94]),
    columnwidth=[2, 1, 1, 1, 1, 1],
    # columnorder=[0, 1, 2, 3, 4],
    header=dict(height=20,
                values=[[''], ['<b>Children</b>'], ['<b>18-32</b>'], ['<b>33-48</b>'], ['<b>49-66</b>'],
                        ['<b>67+</b>']],
                line=dict(color='rgb(50, 50, 50)'),
                align=['left'],
                font=dict(color=['white'] * 5, size=10),
                fill=dict(color='black')),
    cells=dict(values=[table_age[k].tolist() for k in
                       ['index', 'children', 'adults_32', 'adults_48', 'adults_66', 'adults_plus']],
               line=dict(color='#506784'),
               align=['left'] * 5,
               font=dict(color=['rgb(40, 40, 40)'] * 5, size=10),
               # format = [None] + [", .2f"] * 2 + [',.4f'],
               # prefix = [None] * 2 + ['$', u'\u20BF'],
               # suffix=[None] * 4,
               height=20,
               fill=dict(color=['#a9efe8', '#eafbf8']))
)

table_age_title = go.Table(
    domain=dict(x=[0, .28],
                y=[0.94, 0.995]),
    header=dict(height=35,
                values=['Segments by Age'],
                line=dict(color='#fafafa'),
                align=['center'],
                font=dict(color=['black'] * 5, size=16),
                fill=dict(color='#fafafa')
                ))

""" AGE DONUTS VALUES """
data_donuts_age1 = {
    "values": [children_perc, tot_age_perc - children_perc],
    "title": "{0:.1%}".format(children_perc / (tot_age_perc)),
    "labels": ["Children"],
    "textposition": "inside",
    "domain": {'x': [0.3125, 0.4375],
               'y': [0.95, 1]},
    "name": "Children",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

data_donuts_age2 = {
    "values": [adults_32_perc, tot_age_perc - adults_32_perc],
    "title": "{0:.1%}".format(adults_32_perc / (tot_age_perc)),
    "labels": ["18-32"],
    "textposition": "inside",
    "domain": {'x': [0.453125, 0.578125],
               'y': [0.95, 1]},
    "name": "Adults 18-32",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

data_donuts_age3 = {
    "values": [adults_48_perc, tot_age_perc - adults_48_perc],
    "title": "{0:.1%}".format(adults_48_perc / (tot_age_perc)),
    "labels": ["33-48"],
    "domain": {'x': [0.59375, 0.71875],
               'y': [0.95, 1]},
    "name": "Adults 33-48",
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

data_donuts_age4 = {
    "values": [adults_66_perc, tot_age_perc - adults_66_perc],
    "title": "{0:.1%}".format(adults_66_perc / (tot_age_perc)),
    "labels": ["49-66"],
    "textposition": "inside",
    "domain": {'x': [0.734375, 0.859375],
               'y': [0.95, 1]},
    "name": "Adults 49-66",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

data_donuts_age5 = {
    "values": [adults_plus_perc, tot_age_perc - adults_plus_perc],
    "title": "{0:.1%}".format(adults_plus_perc / (tot_age_perc)),
    "labels": ["67+"],
    "textposition": "inside",
    "domain": {'x': [0.875, 1],
               'y': [0.95, 1]},
    "name": "Adults 67+",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']}
}

values_upselling_children = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['Age'] < 18].sum()
values_upselling_children = values_upselling_children.tolist()

values_upselling_adults32 = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    (18 <= hotel_data['Age']) & (hotel_data['Age'] <= 32)].sum()
values_upselling_adults32 = values_upselling_adults32.tolist()

values_upselling_adults48 = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    (33 <= hotel_data['Age']) & (hotel_data['Age'] <= 48)].sum()
values_upselling_adults48 = values_upselling_adults48.tolist()

values_upselling_adults66 = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    (49 <= hotel_data['Age']) & (hotel_data['Age'] <= 66)].sum()
values_upselling_adults66 = values_upselling_adults66.tolist()

values_upselling_adultsplus = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['Age'] > 66].sum()
values_upselling_adultsplus = values_upselling_adultsplus.tolist()

values_upselling_age = [values_upselling_children, values_upselling_adults32, values_upselling_adults48,
                        values_upselling_adults66, values_upselling_adultsplus]

pie_age_child = {
    "values": values_upselling_children,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Children",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']},
}

pie_age_adults32 = {
    "values": values_upselling_adults32,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "18-32",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_age_adults48 = {
    "values": values_upselling_adults48,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "33-48",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_age_adults66 = {
    "values": values_upselling_adults66,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "49-66",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_age_adultsplus = {
    "values": values_upselling_adultsplus,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "67+",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

values_upselling_pie_age = [pie_age_child, pie_age_adults32, pie_age_adults48, pie_age_adults66, pie_age_adultsplus]

""" AGE UPSELLING TABLE """
# AGE UPSELLING TABLES - MEAN
ups_children_restaurant_rev_mean = round(children['Restaurant'].mean(), 0)
ups_adults_32_restaurant_rev_mean = round(adults_32['Restaurant'].mean(), 0)
ups_adults_48_restaurant_rev_mean = round(adults_48['Restaurant'].mean(), 0)
ups_adults_66_restaurant_rev_mean = round(adults_66['Restaurant'].mean(), 0)
ups_adults_plus_restaurant_rev_mean = round(adults_plus['Restaurant'].mean(), 0)

ups_children_bar_rev_mean = round(children['Bar'].mean(), 0)
ups_adults_32_bar_rev_mean = round(adults_32['Bar'].mean(), 0)
ups_adults_48_bar_rev_mean = round(adults_48['Bar'].mean(), 0)
ups_adults_66_bar_rev_mean = round(adults_66['Bar'].mean(), 0)
ups_adults_plus_bar_rev_mean = round(adults_plus['Bar'].mean(), 0)

ups_children_breakfast_rev_mean = round(children['Breakfast'].mean(), 0)
ups_adults_32_breakfast_rev_mean = round(adults_32['Breakfast'].mean(), 0)
ups_adults_48_breakfast_rev_mean = round(adults_48['Breakfast'].mean(), 0)
ups_adults_66_breakfast_rev_mean = round(adults_66['Breakfast'].mean(), 0)
ups_adults_plus_breakfast_rev_mean = round(adults_plus['Breakfast'].mean(), 0)

ups_children_other_rev_mean = round(children['Other'].mean(), 0)
ups_adults_32_other_rev_mean = round(adults_32['Other'].mean(), 0)
ups_adults_48_other_rev_mean = round(adults_48['Other'].mean(), 0)
ups_adults_66_other_rev_mean = round(adults_66['Other'].mean(), 0)
ups_adults_plus_other_rev_mean = round(adults_plus['Other'].mean(), 0)

ups_children = [ups_children_restaurant_rev_mean, ups_children_bar_rev_mean, ups_children_breakfast_rev_mean,
                ups_children_other_rev_mean]
ups_adults_32 = [ups_adults_32_restaurant_rev_mean, ups_adults_32_bar_rev_mean, ups_adults_32_breakfast_rev_mean,
                 ups_adults_32_other_rev_mean]
ups_adults_48 = [ups_adults_48_restaurant_rev_mean, ups_adults_48_bar_rev_mean, ups_adults_48_breakfast_rev_mean,
                 ups_adults_48_other_rev_mean]
ups_adults_66 = [ups_adults_66_restaurant_rev_mean, ups_adults_66_bar_rev_mean, ups_adults_66_breakfast_rev_mean,
                 ups_adults_66_other_rev_mean]
ups_adults_plus = [ups_adults_plus_restaurant_rev_mean, ups_adults_plus_bar_rev_mean,
                   ups_adults_plus_breakfast_rev_mean, ups_adults_plus_other_rev_mean]

# AGE UPSELLING TABLES - SUM
ups_children_restaurant_sum = children['Restaurant'].sum()
ups_adults_32_restaurant_sum = adults_32['Restaurant'].sum()
ups_adults_48_restaurant_sum = adults_48['Restaurant'].sum()
ups_adults_66_restaurant_sum = adults_66['Restaurant'].sum()
ups_adults_plus_restaurant_sum = adults_plus['Restaurant'].sum()

ups_children_bar_sum = children['Bar'].sum()
ups_adults_32_bar_sum = adults_32['Bar'].sum()
ups_adults_48_bar_sum = adults_48['Bar'].sum()
ups_adults_66_bar_sum = adults_66['Bar'].sum()
ups_adults_plus_bar_sum = adults_plus['Bar'].sum()

ups_children_breakfast_sum = children['Breakfast'].sum()
ups_adults_32_breakfast_sum = adults_32['Breakfast'].sum()
ups_adults_48_breakfast_sum = adults_48['Breakfast'].sum()
ups_adults_66_breakfast_sum = adults_66['Breakfast'].sum()
ups_adults_plus_breakfast_sum = adults_plus['Breakfast'].sum()

ups_children_other_sum = children['Other'].sum()
ups_adults_32_other_sum = adults_32['Other'].sum()
ups_adults_48_other_sum = adults_48['Other'].sum()
ups_adults_66_other_sum = adults_66['Other'].sum()
ups_adults_plus_other_sum = adults_plus['Other'].sum()

ups_tot = hotel_data['Upselling'].sum()

ups_restaurant_tot = hotel_data['Restaurant'].sum()
ups_bar_tot = hotel_data['Bar'].sum()
ups_breakfast_tot = hotel_data['Breakfast'].sum()
ups_other_tot = hotel_data['Other'].sum()

ups_children_restaurant_perc = "{0:.1%}".format(ups_children_restaurant_sum / ups_tot)
ups_adults_32_restaurant_perc = "{0:.1%}".format(ups_adults_32_restaurant_sum / ups_tot)
ups_adults_48_restaurant_perc = "{0:.1%}".format(ups_adults_48_restaurant_sum / ups_tot)
ups_adults_66_restaurant_perc = "{0:.1%}".format(ups_adults_66_restaurant_sum / ups_tot)
ups_adults_plus_restaurant_perc = "{0:.1%}".format(ups_adults_plus_restaurant_sum / ups_tot)

ups_children_bar_perc = "{0:.1%}".format(ups_children_bar_sum / ups_tot)
ups_adults_32_bar_perc = "{0:.1%}".format(ups_adults_32_bar_sum / ups_tot)
ups_adults_48_bar_perc = "{0:.1%}".format(ups_adults_48_bar_sum / ups_tot)
ups_adults_66_bar_perc = "{0:.1%}".format(ups_adults_66_bar_sum / ups_tot)
ups_adults_plus_bar_perc = "{0:.1%}".format(ups_adults_plus_bar_sum / ups_tot)

ups_children_breakfast_perc = "{0:.1%}".format(ups_children_breakfast_sum / ups_tot)
ups_adults_32_breakfast_perc = "{0:.1%}".format(ups_adults_32_breakfast_sum / ups_tot)
ups_adults_48_breakfast_perc = "{0:.1%}".format(ups_adults_48_breakfast_sum / ups_tot)
ups_adults_66_breakfast_perc = "{0:.1%}".format(ups_adults_66_breakfast_sum / ups_tot)
ups_adults_plus_breakfast_perc = "{0:.1%}".format(ups_adults_plus_breakfast_sum / ups_tot)

ups_children_other_perc = "{0:.1%}".format(ups_children_other_sum / ups_tot)
ups_adults_32_other_perc = "{0:.1%}".format(ups_adults_32_other_sum / ups_tot)
ups_adults_48_other_perc = "{0:.1%}".format(ups_adults_48_other_sum / ups_tot)
ups_adults_66_other_perc = "{0:.1%}".format(ups_adults_66_other_sum / ups_tot)
ups_adults_plus_other_perc = "{0:.1%}".format(ups_adults_plus_other_sum / ups_tot)

ups_children_perc = [ups_children_restaurant_perc, ups_children_bar_perc, ups_children_breakfast_perc,
                     ups_children_other_perc]
ups_adults_32_perc = [ups_adults_32_restaurant_perc, ups_adults_32_bar_perc, ups_adults_32_breakfast_perc,
                      ups_adults_32_other_perc]
ups_adults_48_perc = [ups_adults_48_restaurant_perc, ups_adults_48_bar_perc, ups_adults_48_breakfast_perc,
                      ups_adults_48_other_perc]
ups_adults_66_perc = [ups_adults_66_restaurant_perc, ups_adults_66_bar_perc, ups_adults_66_breakfast_perc,
                      ups_adults_66_other_perc]
ups_adults_plus_perc = [ups_adults_plus_restaurant_perc, ups_adults_plus_bar_perc, ups_adults_plus_breakfast_perc,
                        ups_adults_plus_other_perc]

# columns_ups_age = ['Children','18-32','33-48','49']
index_table_ups = ['Restaurant', 'Bar', 'Breakfast', 'Other']
columns_table_ups = ['Avg Revenues', 'Absolute %']

table_upselling_age_children = pd.DataFrame(index=index_table_ups,
                                            data={'Avg Revenues': ups_children, 'Absolute %': ups_children_perc},
                                            columns=columns_table_ups).reset_index()
table_upselling_age_adults_32 = pd.DataFrame(index=index_table_ups,
                                             data={'Avg Revenues': ups_adults_32, 'Absolute %': ups_adults_32_perc},
                                             columns=columns_table_ups).reset_index()
table_upselling_age_adults_48 = pd.DataFrame(index=index_table_ups,
                                             data={'Avg Revenues': ups_adults_48, 'Absolute %': ups_adults_48_perc},
                                             columns=columns_table_ups).reset_index()
table_upselling_age_adults_66 = pd.DataFrame(index=index_table_ups,
                                             data={'Avg Revenues': ups_adults_66, 'Absolute %': ups_adults_66_perc},
                                             columns=columns_table_ups).reset_index()
table_upselling_age_adults_plus = pd.DataFrame(index=index_table_ups, data={'Avg Revenues': ups_adults_plus,
                                                                            'Absolute %': ups_adults_plus_perc},
                                               columns=columns_table_ups).reset_index()

updatemenus_age = list(
    [dict(active=-1,
          buttons=list([
              dict(label='Children',
                   method='update',
                   args=[{'visible': [True, False, False, False, False]}, ]),
              dict(label='18-32',
                   method='update',
                   args=[{'visible': [False, True, False, False, False]}, ]),
              dict(label='33-48',
                   method='update',
                   args=[{'visible': [False, False, True, False, False]}, ]),
              dict(label='49-66',
                   method='update',
                   args=[{'visible': [False, False, False, True, False]}, ]),
              dict(label='67+',
                   method='update',
                   args=[{'visible': [False, False, False, False, True]}, ])
          ]),
          direction='down',
          yanchor='top',
          xanchor='left',
          x=0.5,
          y=.95,
          )
     ])

table_upselling_age_children1 = graph_layouts.RightTable(table_upselling_age_children).returning_table()
table_upselling_age_adults_321 = graph_layouts.RightTable(table_upselling_age_adults_32).returning_table()
table_upselling_age_adults_481 = graph_layouts.RightTable(table_upselling_age_adults_48).returning_table()
table_upselling_age_adults_661 = graph_layouts.RightTable(table_upselling_age_adults_66).returning_table()
table_upselling_age_adults_plus1 = graph_layouts.RightTable(table_upselling_age_adults_plus).returning_table()

traces_ups_age = [table_upselling_age_children1, table_upselling_age_adults_321, table_upselling_age_adults_481,
                  table_upselling_age_adults_661, table_upselling_age_adults_plus1]
