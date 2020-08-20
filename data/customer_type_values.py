import plotly.graph_objs as go
from assets import graph_layouts
from settings import hotel_data, pd
from data.age_values import ups_tot, index_age

""" CUSTOMER TYPE VALUES  """
transient = hotel_data.loc[hotel_data['CustomerType'] == 'Transient']
transient_party = hotel_data.loc[hotel_data['CustomerType'] == 'Transient-Party']
contract = hotel_data.loc[hotel_data['CustomerType'] == 'Contract']
group = hotel_data.loc[hotel_data['CustomerType'] == 'Group']

tot_customertype_perc = hotel_data['CustomerType'].count()
transient_perc = transient['CustomerType'].count()
transient_party_perc = transient_party['CustomerType'].count()
contract_perc = contract['CustomerType'].count()
group_perc = group['CustomerType'].count()

transient_mean = round(transient['Upselling'].mean(), ndigits=1)
transient_party_mean = round(transient_party['Upselling'].mean(), ndigits=1)
contract_mean = round(contract['Upselling'].mean(), ndigits=1)
group_mean = round(group['Upselling'].mean(), ndigits=1)

transientRev_mean = round(transient['Revenues by day'].mean(), ndigits=1)
transient_partyRev_mean = round(transient_party['Revenues by day'].mean(), ndigits=1)
contractRev_mean = round(contract['Revenues by day'].mean(), ndigits=1)
groupRev_mean = round(group['Revenues by day'].mean(), ndigits=1)

transient_rating = round(transient['Rating'].mean(), ndigits=1)
transient_party_rating = round(transient_party['Rating'].mean(), ndigits=1)
contract_rating = round(contract['Rating'].mean(), ndigits=1)
group_rating = round(group['Rating'].mean(), ndigits=1)

transient_nights = round(transient['Nights'].mean(), ndigits=1)
transient_party_nights = round(transient_party['Nights'].mean(), ndigits=1)
contract_nights = round(contract['Nights'].mean(), ndigits=1)
group_nights = round(group['Nights'].mean(), ndigits=1)

transient_wd = round(transient['StaysInWeekNights'].mean(), ndigits=1)
transient_party_wd = round(transient_party['StaysInWeekNights'].mean(), ndigits=1)
contract_wd = round(contract['StaysInWeekNights'].mean(), ndigits=1)
group_wd = round(group['StaysInWeekNights'].mean(), ndigits=1)

transient_we = round(transient['StaysInWeekendNights'].mean(), ndigits=1)
transient_party_we = round(transient_party['StaysInWeekendNights'].mean(), ndigits=1)
contract_we = round(contract['StaysInWeekendNights'].mean(), ndigits=1)
group_we = round(group['StaysInWeekendNights'].mean(), ndigits=1)

transient_nation_rev = transient.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
transient_party_nation_rev = \
    transient_party.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
contract_nation_rev = contract.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
group_nation_rev = group.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]

transient_nation_rating = transient.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
transient_party_nation_rating = transient_party.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[
    0]
contract_nation_rating = contract.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
group_nation_rating = group.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]

transient_nation_upselling = transient.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
transient_party_nation_upselling = \
    transient_party.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
contract_nation_upselling = contract.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
group_nation_upselling = group.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]

columns_ct = ['Transient', 'Transient-Party', 'Contract', 'Group']
index_ct = index_age

table_ct = pd.DataFrame(data=[
    [transient_mean, transient_party_mean, contract_mean, group_mean],
    [transientRev_mean, transient_partyRev_mean, contractRev_mean, groupRev_mean],
    [transient_rating, transient_party_rating, contract_rating, group_rating],
    [transient_nights, transient_party_nights, contract_nights, group_nights],
    [transient_wd, transient_party_wd, contract_wd, group_wd],
    [transient_we, transient_party_we, contract_we, group_we],
    [transient_nation_rev, transient_party_nation_rev, contract_nation_rev, group_nation_rev],
    [transient_nation_rating, transient_party_nation_rating, contract_nation_rating, group_nation_rating],
    [transient_nation_upselling, transient_party_nation_upselling, contract_nation_upselling, group_nation_upselling]
],
    index=index_ct, columns=columns_ct)

table_customer_type = table_ct.reset_index()

table_customer_type1 = go.Table(
    domain=dict(x=[0, 1],
                y=[0, .228]),
    columnwidth=[2, 1, 1, 1],
    header=dict(height=20,
                values=[[''], ['<b>Transient</b>'],
                        ['<b>Transient Party</b>'], ['<b>Contract</b>'], ['<b>Group</b>']],
                line=dict(color='rgb(50, 50, 50)'),
                align=['left'],
                font=dict(color=['white'] * 5, size=10),
                fill=dict(color='black')),
    cells=dict(values=[table_customer_type[k].tolist() for k in
                       ['index', 'Transient', 'Transient-Party', 'Contract', 'Group']],
               line=dict(color='#506784'),
               align=['left'] * 5,
               font=dict(color=['rgb(40, 40, 40)'] * 5, size=10),
               height=20,
               fill=dict(color=['#a9efe8', '#eafbf8']))
)

table_ct_title = go.Table(
    domain=dict(x=[0, .28],
                y=[0.24, 0.295]),
    header=dict(height=45,
                values=['Segments by Customer Type'],
                line=dict(color='#fafafa'),
                align=['center'],
                font=dict(color=['black'] * 5, size=16),
                fill=dict(color='#fafafa')
                ))

""" DATA DONUTS CUSTOMER TY """
data_donuts_cs1 = {
    "values": [transient_perc, tot_customertype_perc - transient_perc],
    "title": "{0:.1%}".format(transient_perc / (tot_customertype_perc)),
    "labels": ["Transient"],
    "textposition": "inside",
    "domain": {'x': [0.3594, 0.46875],
               'y': [0.24, 0.295]},
    "name": "Transient",
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

data_donuts_cs2 = {
    "values": [transient_party_perc, tot_customertype_perc - transient_party_perc],
    "labels": ["Transient-party"],
    "title": "{0:.1%}".format(transient_party_perc / (tot_customertype_perc)),
    "textposition": "inside",
    "domain": {'x': [0.53125, 0.640625],
               'y': [0.24, 0.295]},
    "name": "Transient Party",
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

data_donuts_cs3 = {
    "values": [contract_perc, tot_customertype_perc - contract_perc],
    "title": "{0:.1%}".format(contract_perc / (tot_customertype_perc)),
    "labels": ["Contract"],
    "textposition": "inside",
    "domain": {'x': [0.703125, 0.8125],
               'y': [0.24, 0.295]},
    "name": "Contract",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

data_donuts_cs4 = {
    "values": [group_perc, tot_customertype_perc - group_perc],
    "title": "{0:.1%}".format(group_perc / (tot_customertype_perc)),
    "labels": ["Group"],
    "domain": {'x': [0.875, 1],
               'y': [0.24, 0.295]},
    "name": "Group",
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
values_upselling_transient = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['CustomerType'] == 'Transient'].sum().copy()
values_upselling_transient = values_upselling_transient.tolist()

values_upselling_transientP = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['CustomerType'] == 'Transient-Party'].sum().copy()
values_upselling_transientP = values_upselling_transientP.tolist()

values_upselling_contract = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['CustomerType'] == 'Contract'].sum().copy()
values_upselling_contract = values_upselling_contract.tolist()

values_upselling_group = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['CustomerType'] == 'Group'].sum().copy()
values_upselling_group = values_upselling_group.tolist()

values_upselling_ct = [values_upselling_transient, values_upselling_transientP, values_upselling_contract,
                       values_upselling_group]

pie_ct_transient = {
    "values": values_upselling_transient,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Transient",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_ct_transientP = {
    "values": values_upselling_transientP,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Transient-Party",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_ct_contract = {
    "values": values_upselling_contract,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Contract",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_ct_group = {
    "values": values_upselling_group,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Group",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

values_upselling_pie_ct = [pie_ct_transient, pie_ct_transientP, pie_ct_contract, pie_ct_group]

""" CUSTOMER TYPE UPSELLING VALUES """
ups_transient_restaurant_rev_mean = round(transient['Restaurant'].mean(), 0)
ups_transient_party_restaurant_rev_mean = round(transient_party['Restaurant'].mean(), 0)
ups_contract_restaurant_rev_mean = round(contract['Restaurant'].mean(), 0)
ups_group_restaurant_rev_mean = round(group['Restaurant'].mean(), 0)

ups_transient_bar_rev_mean = round(transient['Bar'].mean(), 0)
ups_transient_party_bar_rev_mean = round(transient_party['Bar'].mean(), 0)
ups_contract_bar_rev_mean = round(contract['Bar'].mean(), 0)
ups_group_bar_rev_mean = round(group['Bar'].mean(), 0)

ups_transient_breakfast_rev_mean = round(transient['Breakfast'].mean(), 0)
ups_transient_party_breakfast_rev_mean = round(transient_party['Breakfast'].mean(), 0)
ups_contract_breakfast_rev_mean = round(contract['Breakfast'].mean(), 0)
ups_group_breakfast_rev_mean = round(group['Breakfast'].mean(), 0)

ups_transient_other_rev_mean = round(transient['Other'].mean(), 0)
ups_transient_party_other_rev_mean = round(transient_party['Other'].mean(), 0)
ups_contract_other_rev_mean = round(contract['Other'].mean(), 0)
ups_group_other_rev_mean = round(group['Other'].mean(), 0)

ups_transient = [ups_transient_restaurant_rev_mean, ups_transient_bar_rev_mean, ups_transient_breakfast_rev_mean,
                 ups_transient_other_rev_mean]
ups_transient_party = [ups_transient_party_restaurant_rev_mean, ups_transient_party_bar_rev_mean,
                       ups_transient_party_breakfast_rev_mean, ups_transient_party_other_rev_mean]
ups_contract = [ups_contract_restaurant_rev_mean, ups_contract_bar_rev_mean, ups_contract_breakfast_rev_mean,
                ups_contract_other_rev_mean]
ups_group = [ups_group_restaurant_rev_mean, ups_group_bar_rev_mean, ups_group_breakfast_rev_mean,
             ups_group_other_rev_mean]

ups_transient_restaurant_sum = transient['Restaurant'].sum()
ups_transient_party_restaurant_sum = transient_party['Restaurant'].sum()
ups_contract_restaurant_sum = contract['Restaurant'].sum()
ups_group_restaurant_sum = group['Restaurant'].sum()

ups_transient_bar_sum = transient['Bar'].sum()
ups_transient_party_bar_sum = transient_party['Bar'].sum()
ups_contract_bar_sum = contract['Bar'].sum()
ups_group_bar_sum = group['Bar'].sum()

ups_transient_breakfast_sum = transient['Breakfast'].sum()
ups_transient_party_breakfast_sum = transient_party['Breakfast'].sum()
ups_contract_breakfast_sum = contract['Breakfast'].sum()
ups_group_breakfast_sum = group['Breakfast'].sum()

ups_transient_other_sum = transient['Other'].sum()
ups_transient_party_other_sum = transient_party['Other'].sum()
ups_contract_other_sum = contract['Other'].sum()
ups_group_other_sum = group['Other'].sum()

ups_restaurant_tot = hotel_data['Restaurant'].sum()
ups_bar_tot = hotel_data['Bar'].sum()
ups_breakfast_tot = hotel_data['Breakfast'].sum()
ups_other_tot = hotel_data['Other'].sum()

ups_transient_restaurant_perc = "{0:.1%}".format(ups_transient_restaurant_sum / ups_tot)
ups_transient_party_restaurant_perc = "{0:.1%}".format(ups_transient_party_restaurant_sum / ups_tot)
ups_contract_restaurant_perc = "{0:.1%}".format(ups_contract_restaurant_sum / ups_tot)
ups_group_restaurant_perc = "{0:.1%}".format(ups_group_restaurant_sum / ups_tot)

ups_transient_bar_perc = "{0:.1%}".format(ups_transient_bar_sum / ups_tot)
ups_transient_party_bar_perc = "{0:.1%}".format(ups_transient_party_bar_sum / ups_tot)
ups_contract_bar_perc = "{0:.1%}".format(ups_contract_bar_sum / ups_tot)
ups_group_bar_perc = "{0:.1%}".format(ups_group_bar_sum / ups_tot)

ups_transient_breakfast_perc = "{0:.1%}".format(ups_transient_breakfast_sum / ups_tot)
ups_transient_party_breakfast_perc = "{0:.1%}".format(ups_transient_party_breakfast_sum / ups_tot)
ups_contract_breakfast_perc = "{0:.1%}".format(ups_contract_breakfast_sum / ups_tot)
ups_group_breakfast_perc = "{0:.1%}".format(ups_group_breakfast_sum / ups_tot)

ups_transient_other_perc = "{0:.1%}".format(ups_transient_other_sum / ups_tot)
ups_transient_party_other_perc = "{0:.1%}".format(ups_transient_party_other_sum / ups_tot)
ups_contract_other_perc = "{0:.1%}".format(ups_contract_other_sum / ups_tot)
ups_group_other_perc = "{0:.1%}".format(ups_group_other_sum / ups_tot)

ups_transient_perc = [ups_transient_restaurant_perc, ups_transient_bar_perc, ups_transient_breakfast_perc,
                      ups_transient_other_perc]
ups_transient_party_perc = [ups_transient_party_restaurant_perc, ups_transient_party_bar_perc,
                            ups_transient_party_breakfast_perc, ups_transient_party_other_perc]
ups_contract_perc = [ups_contract_restaurant_perc, ups_contract_bar_perc, ups_contract_breakfast_perc,
                     ups_contract_other_perc]
ups_group_perc = [ups_group_restaurant_perc, ups_group_bar_perc, ups_group_breakfast_perc, ups_group_other_perc]

index_table_ups = ['Restaurant', 'Bar', 'Breakfast', 'Other']
columns_table_ups = ['Avg Revenues', 'Absolute %']

table_upselling_ct_transient = pd.DataFrame(index=index_table_ups,
                                            data={'Avg Revenues': ups_transient, 'Absolute %': ups_transient_perc},
                                            columns=columns_table_ups).reset_index()
table_upselling_ct_transient_party = pd.DataFrame(index=index_table_ups, data={'Avg Revenues': ups_transient_party,
                                                                               'Absolute %': ups_transient_party_perc},
                                                  columns=columns_table_ups).reset_index()
table_upselling_ct_contract = pd.DataFrame(index=index_table_ups,
                                           data={'Avg Revenues': ups_contract, 'Absolute %': ups_contract_perc},
                                           columns=columns_table_ups).reset_index()
table_upselling_ct_group = pd.DataFrame(index=index_table_ups,
                                        data={'Avg Revenues': ups_group, 'Absolute %': ups_group_perc},
                                        columns=columns_table_ups).reset_index()

table_upselling_ct_transient1 = graph_layouts.RightTable(table_upselling_ct_transient).returning_table()
table_upselling_ct_transient_party1 = graph_layouts.RightTable(table_upselling_ct_transient_party).returning_table()
table_upselling_ct_contract1 = graph_layouts.RightTable(table_upselling_ct_contract).returning_table()
table_upselling_ct_group1 = graph_layouts.RightTable(table_upselling_ct_group).returning_table()

traces_ups_ct = [table_upselling_ct_transient1, table_upselling_ct_transient_party1, table_upselling_ct_contract1,
                 table_upselling_ct_group1]

updatemenus_ct = list(
    [dict(active=-1,
          buttons=list([
              dict(label='Transient',
                   method='update',
                   args=[{'visible': [True, False, False, False]}, ]),
              dict(label='Transient-Party',
                   method='update',
                   args=[{'visible': [False, True, False, False]}, ]),
              dict(label='Contract',
                   method='update',
                   args=[{'visible': [False, False, True, False]}, ]),
              dict(label='Group',
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
