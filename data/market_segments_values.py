import plotly.graph_objs as go
from assets import graph_layouts
from settings import hotel_data, pd
from data.age_values import ups_tot, index_age

""" MARKET SEGMENT VALUES """
Solo_Travellers = hotel_data.loc[hotel_data['MarketSegment'] == 'Solo Travellers']
Family = hotel_data.loc[hotel_data['MarketSegment'] == 'Family']
Groups = hotel_data.loc[hotel_data['MarketSegment'] == 'Groups']
Couples = hotel_data.loc[hotel_data['MarketSegment'] == 'Couples']
Business = hotel_data.loc[hotel_data['MarketSegment'] == 'Business']

tot_marks_perc = hotel_data['MarketSegment'].count()
Solo_Travellers_perc = Solo_Travellers['MarketSegment'].count()
Family_perc = Family['MarketSegment'].count()
Groups_perc = Groups['MarketSegment'].count()
Couples_perc = Couples['MarketSegment'].count()
Business_perc = Business['MarketSegment'].count()

Solo_Travellers_mean = round(Solo_Travellers['Upselling'].mean(), ndigits=1)
Family_mean = round(Family['Upselling'].mean(), ndigits=1)
Groups_mean = round(Groups['Upselling'].mean(), ndigits=1)
Couples_mean = round(Couples['Upselling'].mean(), ndigits=1)
Business_mean = round(Business['Upselling'].mean(), ndigits=1)

Solo_TravellersRev_mean = round(Solo_Travellers['Revenues by day'].mean(), ndigits=1)
FamilyRev_mean = round(Family['Revenues by day'].mean(), ndigits=1)
GroupsRev_mean = round(Groups['Revenues by day'].mean(), ndigits=1)
CouplesRev_mean = round(Couples['Revenues by day'].mean(), ndigits=1)
BusinessRev_mean = round(Business['Revenues by day'].mean(), ndigits=1)

Solo_Travellers_rating = round(Solo_Travellers['Rating'].mean(), ndigits=1)
Family_rating = round(Family['Rating'].mean(), ndigits=1)
Groups_rating = round(Groups['Rating'].mean(), ndigits=1)
Couples_rating = round(Couples['Rating'].mean(), ndigits=1)
Business_rating = round(Business['Rating'].mean(), ndigits=1)

Solo_Travellers_nights = round(Solo_Travellers['Nights'].mean(), ndigits=1)
Family_nights = round(Family['Nights'].mean(), ndigits=1)
Groups_nights = round(Groups['Nights'].mean(), ndigits=1)
Couples_nights = round(Couples['Nights'].mean(), ndigits=1)
Business_nights = round(Business['Nights'].mean(), ndigits=1)

Solo_Travellers_wd = round(Solo_Travellers['StaysInWeekNights'].mean(), ndigits=1)
Family_wd = round(Family['StaysInWeekNights'].mean(), ndigits=1)
Groups_wd = round(Groups['StaysInWeekNights'].mean(), ndigits=1)
Couples_wd = round(Couples['StaysInWeekNights'].mean(), ndigits=1)
Business_wd = round(Business['StaysInWeekNights'].mean(), ndigits=1)

Solo_Travellers_we = round(Solo_Travellers['StaysInWeekendNights'].mean(), ndigits=1)
Family_we = round(Family['StaysInWeekendNights'].mean(), ndigits=1)
Groups_we = round(Groups['StaysInWeekendNights'].mean(), ndigits=1)
Couples_we = round(Couples['StaysInWeekendNights'].mean(), ndigits=1)
Business_we = round(Business['StaysInWeekendNights'].mean(), ndigits=1)

Solo_Travellers_nation_rev = \
    Solo_Travellers.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
Family_nation_rev = Family.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
Groups_nation_rev = Groups.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
Couples_nation_rev = Couples.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
Business_nation_rev = Business.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]

Solo_Travellers_nation_rating = Solo_Travellers.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[
    0]
Family_nation_rating = Family.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
Groups_nation_rating = Groups.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
Couples_nation_rating = Couples.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
Business_nation_rating = Business.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]

Solo_Travellers_nation_upselling = \
    Solo_Travellers.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
Family_nation_upselling = Family.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
Groups_nation_upselling = Groups.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
Couples_nation_upselling = Couples.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
Business_nation_upselling = Business.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]

columns_mss = ['Solo_Travellers', 'Family', 'Groups', 'Couples', 'Business']
index_mss = index_age

table_m_s = pd.DataFrame(data=[
    [Solo_Travellers_mean, Family_mean, Groups_mean, Couples_mean, Business_mean],
    [Solo_TravellersRev_mean, FamilyRev_mean, GroupsRev_mean, CouplesRev_mean, BusinessRev_mean],
    [Solo_Travellers_rating, Family_rating, Groups_rating, Couples_rating, Business_rating],
    [Solo_Travellers_nights, Family_nights, Groups_nights, Couples_nights, Business_nights],
    [Solo_Travellers_wd, Family_wd, Groups_wd, Couples_wd, Business_wd],
    [Solo_Travellers_we, Family_we, Groups_we, Couples_we, Business_we],
    [Solo_Travellers_nation_rev, Family_nation_rev, Groups_nation_rev, Couples_nation_rev, Business_nation_rev],
    [Solo_Travellers_nation_rating, Family_nation_rating, Groups_nation_rating, Couples_nation_rating,
     Business_nation_rating],
    [Solo_Travellers_nation_upselling, Family_nation_upselling, Groups_nation_upselling, Couples_nation_upselling,
     Business_nation_upselling]
],
    index=index_mss, columns=columns_mss)

table_marksegment = table_m_s.reset_index()

table_marksegment1 = go.Table(
    domain=dict(x=[0, 1],
                y=[0.30, .53]),
    columnwidth=[2, 1, 1, 1, 1, 1],
    header=dict(height=20,
                values=[[''], ['<b>Solo Travellers</b>'],
                        ['<b>Family</b>'], ['<b>Groups</b>'], ['<b>Couples</b>'], ['<b>Business</b>']],
                line=dict(color='rgb(50, 50, 50)'),
                align=['left'],
                font=dict(color=['white'] * 5, size=10),
                fill=dict(color='black')),
    cells=dict(values=[table_marksegment[k].tolist() for k in
                       ['index', 'Solo_Travellers', 'Family', 'Groups', 'Couples', 'Business']],
               line=dict(color='#506784'),
               align=['left'] * 5,
               font=dict(color=['rgb(40, 40, 40)'] * 5, size=10),
               height=20,
               fill=dict(color=['#a9efe8', '#eafbf8']))
)

table_marks_title = go.Table(
    domain=dict(x=[0, .28],
                y=[0.54, 0.595]),
    header=dict(height=45,
                values=['Segments by Travel Companion'],
                line=dict(color='#fafafa'),
                align=['center'],
                font=dict(color=['black'] * 5, size=16),
                fill=dict(color='#fafafa')
                ))

""" DONUTS MARKET SEGMENT """
data_donuts_marks1 = {
    "values": [Solo_Travellers_perc, tot_marks_perc - Solo_Travellers_perc],
    "title": "{0:.1%}".format(Solo_Travellers_perc / (tot_marks_perc)),
    "labels": ["Solo Travellers"],
    "textposition": "inside",
    "domain": {'x': [0.3125, 0.4375],
               'y': [0.54, 0.59]},
    "name": "Solo Travellers",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']}
}

data_donuts_marks2 = {
    "values": [Family_perc, tot_marks_perc - Family_perc],
    "title": "{0:.1%}".format(Family_perc / (tot_marks_perc)),
    "labels": ["US"],
    "textposition": "inside",
    "domain": {'x': [0.453125, 0.578125],
               'y': [0.54, .59]},
    "name": "Family",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

data_donuts_marks3 = {
    "values": [Groups_perc, tot_marks_perc - Groups_perc],
    "title": "{0:.1%}".format(Groups_perc / (tot_marks_perc)),
    "labels": ["US"],
    "textposition": "inside",
    "domain": {'x': [0.59375, 0.71875],
               'y': [0.54, .59]},
    "name": "Groups",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

data_donuts_marks5 = {
    "values": [Business_perc, tot_marks_perc - Business_perc],
    "title": "{0:.1%}".format(Business_perc / (tot_marks_perc)),
    "labels": ["Business_perc"],
    "textposition": "inside",
    "domain": {'x': [0.734375, 0.859375],
               'y': [0.54, .59]},
    "name": "Business",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']}
}

data_donuts_marks6 = {
    "values": [Couples_perc, tot_marks_perc - Couples_perc],
    "title": "{0:.1%}".format(Couples_perc / (tot_marks_perc)),
    "labels": ["Couples_perc"],
    "textposition": "inside",
    "domain": {'x': [0.875, 1],
               'y': [0.54, .59]},
    "name": "Couples",
    "hoverinfo": "none",
    "hole": .4,
    "pull": 0.03,
    "type": "pie",
    "sort": False,
    "showlegend": False,
    "textinfo": "none",
    'marker': {'colors': ['#dc3d4f', '#a9efe8']},
}

values_upselling_st = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['MarketSegment'] == 'Solo Travellers'].sum()
values_upselling_st = values_upselling_st.tolist()

values_upselling_fam = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['MarketSegment'] == 'Family'].sum()
values_upselling_fam = values_upselling_fam.tolist()

values_upselling_groups = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['MarketSegment'] == 'Groups'].sum()
values_upselling_groups = values_upselling_groups.tolist()

values_upselling_Business = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['MarketSegment'] == 'Business'].sum()
values_upselling_Business = values_upselling_Business.tolist()

values_upselling_couples = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
    hotel_data['MarketSegment'] == 'Couples'].sum()
values_upselling_couples = values_upselling_couples.tolist()

values_upselling_marks = [values_upselling_st, values_upselling_fam, values_upselling_groups, values_upselling_Business,
                          values_upselling_couples]

pie_marks_st = {
    "values": values_upselling_st,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Solo Travellers",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_marks_fam = {
    "values": values_upselling_fam,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Family",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_marks_groups = {
    "values": values_upselling_groups,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Groups",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_marks_couples = {
    "values": values_upselling_couples,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Couples",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

pie_marks_business = {
    "values": values_upselling_Business,
    "labels": ['Bar', 'Restaurant', 'Other', 'Breakfast', 'ADR'],
    "textposition": "inside",
    "domain": {'x': [0, .64],
               'y': [0.3, .8]},
    "name": "Business",
    "hoverinfo": "values",
    "type": "pie",
    "sort": False,
    "title": 'Aggregated Expenditures per segment selected',
    "textinfo": "none",
    'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f'
                          ]}
}

values_upselling_pie_marks = [pie_marks_st, pie_marks_fam, pie_marks_groups, pie_marks_couples, pie_marks_business]

""" MARKET SEGMENT UPSELLING VALUES """
ups_Solo_Travellers_restaurant_rev_mean = round(Solo_Travellers['Restaurant'].mean(), 0)
ups_Family_restaurant_rev_mean = round(Family['Restaurant'].mean(), 0)
ups_Groups_restaurant_rev_mean = round(Groups['Restaurant'].mean(), 0)
ups_Couples_restaurant_rev_mean = round(Couples['Restaurant'].mean(), 0)
ups_Business_restaurant_rev_mean = round(Business['Restaurant'].mean(), 0)

ups_Solo_Travellers_bar_rev_mean = round(Solo_Travellers['Bar'].mean(), 0)
ups_Family_bar_rev_mean = round(Family['Bar'].mean(), 0)
ups_Groups_bar_rev_mean = round(Groups['Bar'].mean(), 0)
ups_Couples_bar_rev_mean = round(Couples['Bar'].mean(), 0)
ups_Business_bar_rev_mean = round(Business['Bar'].mean(), 0)

ups_Solo_Travellers_breakfast_rev_mean = round(Solo_Travellers['Breakfast'].mean(), 0)
ups_Family_breakfast_rev_mean = round(Family['Breakfast'].mean(), 0)
ups_Groups_breakfast_rev_mean = round(Groups['Breakfast'].mean(), 0)
ups_Couples_breakfast_rev_mean = round(Couples['Breakfast'].mean(), 0)
ups_Business_breakfast_rev_mean = round(Business['Breakfast'].mean(), 0)

ups_Solo_Travellers_other_rev_mean = round(Solo_Travellers['Other'].mean(), 0)
ups_Family_other_rev_mean = round(Family['Other'].mean(), 0)
ups_Groups_other_rev_mean = round(Groups['Other'].mean(), 0)
ups_Couples_other_rev_mean = round(Couples['Other'].mean(), 0)
ups_Business_other_rev_mean = round(Business['Other'].mean(), 0)

ups_Solo_Travellers = [ups_Solo_Travellers_restaurant_rev_mean, ups_Solo_Travellers_bar_rev_mean,
                       ups_Solo_Travellers_breakfast_rev_mean, ups_Solo_Travellers_other_rev_mean]
ups_Family = [ups_Family_restaurant_rev_mean, ups_Family_bar_rev_mean, ups_Family_breakfast_rev_mean,
              ups_Family_other_rev_mean]
ups_Groups = [ups_Groups_restaurant_rev_mean, ups_Groups_bar_rev_mean, ups_Groups_breakfast_rev_mean,
              ups_Groups_other_rev_mean]
ups_Couples = [ups_Couples_restaurant_rev_mean, ups_Couples_bar_rev_mean, ups_Couples_breakfast_rev_mean,
               ups_Couples_other_rev_mean]
ups_Business = [ups_Business_restaurant_rev_mean, ups_Business_bar_rev_mean, ups_Business_breakfast_rev_mean,
                ups_Business_other_rev_mean]

ups_Solo_Travellers_restaurant_sum = Solo_Travellers['Restaurant'].sum()
ups_Family_restaurant_sum = Family['Restaurant'].sum()
ups_Groups_restaurant_sum = Groups['Restaurant'].sum()
ups_Couples_restaurant_sum = Couples['Restaurant'].sum()
ups_Business_restaurant_sum = Business['Restaurant'].sum()

ups_Solo_Travellers_bar_sum = Solo_Travellers['Bar'].sum()
ups_Family_bar_sum = Family['Bar'].sum()
ups_Groups_bar_sum = Groups['Bar'].sum()
ups_Couples_bar_sum = Couples['Bar'].sum()
ups_Business_bar_sum = Business['Bar'].sum()

ups_Solo_Travellers_breakfast_sum = Solo_Travellers['Breakfast'].sum()
ups_Family_breakfast_sum = Family['Breakfast'].sum()
ups_Groups_breakfast_sum = Groups['Breakfast'].sum()
ups_Couples_breakfast_sum = Couples['Breakfast'].sum()
ups_Business_breakfast_sum = Business['Breakfast'].sum()

ups_Solo_Travellers_other_sum = Solo_Travellers['Other'].sum()
ups_Family_other_sum = Family['Other'].sum()
ups_Groups_other_sum = Groups['Other'].sum()
ups_Couples_other_sum = Couples['Other'].sum()
ups_Business_other_sum = Business['Other'].sum()

ups_restaurant_tot = hotel_data['Restaurant'].sum()
ups_bar_tot = hotel_data['Bar'].sum()
ups_breakfast_tot = hotel_data['Breakfast'].sum()
ups_other_tot = hotel_data['Other'].sum()

ups_Solo_Travellers_restaurant_perc = "{0:.1%}".format(ups_Solo_Travellers_restaurant_sum / ups_tot)
ups_Family_restaurant_perc = "{0:.1%}".format(ups_Family_restaurant_sum / ups_tot)
ups_Groups_restaurant_perc = "{0:.1%}".format(ups_Groups_restaurant_sum / ups_tot)
ups_Couples_restaurant_perc = "{0:.1%}".format(ups_Couples_restaurant_sum / ups_tot)
ups_Business_restaurant_perc = "{0:.1%}".format(ups_Business_restaurant_sum / ups_tot)

ups_Solo_Travellers_bar_perc = "{0:.1%}".format(ups_Solo_Travellers_bar_sum / ups_tot)
ups_Family_bar_perc = "{0:.1%}".format(ups_Family_bar_sum / ups_tot)
ups_Groups_bar_perc = "{0:.1%}".format(ups_Groups_bar_sum / ups_tot)
ups_Couples_bar_perc = "{0:.1%}".format(ups_Couples_bar_sum / ups_tot)
ups_Business_bar_perc = "{0:.1%}".format(ups_Business_bar_sum / ups_tot)

ups_Solo_Travellers_breakfast_perc = "{0:.1%}".format(ups_Solo_Travellers_breakfast_sum / ups_tot)
ups_Family_breakfast_perc = "{0:.1%}".format(ups_Family_breakfast_sum / ups_tot)
ups_Groups_breakfast_perc = "{0:.1%}".format(ups_Groups_breakfast_sum / ups_tot)
ups_Couples_breakfast_perc = "{0:.1%}".format(ups_Couples_breakfast_sum / ups_tot)
ups_Business_breakfast_perc = "{0:.1%}".format(ups_Business_breakfast_sum / ups_tot)

ups_Solo_Travellers_other_perc = "{0:.1%}".format(ups_Solo_Travellers_other_sum / ups_tot)
ups_Family_other_perc = "{0:.1%}".format(ups_Family_other_sum / ups_tot)
ups_Groups_other_perc = "{0:.1%}".format(ups_Groups_other_sum / ups_tot)
ups_Couples_other_perc = "{0:.1%}".format(ups_Couples_other_sum / ups_tot)
ups_Business_other_perc = "{0:.1%}".format(ups_Business_other_sum / ups_tot)

ups_Solo_Travellers_perc = [ups_Solo_Travellers_restaurant_perc, ups_Solo_Travellers_bar_perc,
                            ups_Solo_Travellers_breakfast_perc, ups_Solo_Travellers_other_perc]
ups_Family_perc = [ups_Family_restaurant_perc, ups_Family_bar_perc, ups_Family_breakfast_perc, ups_Family_other_perc]
ups_Groups_perc = [ups_Groups_restaurant_perc, ups_Groups_bar_perc, ups_Groups_breakfast_perc, ups_Groups_other_perc]
ups_Couples_perc = [ups_Couples_restaurant_perc, ups_Couples_bar_perc, ups_Couples_breakfast_perc,
                    ups_Couples_other_perc]
ups_Business_perc = [ups_Business_restaurant_perc, ups_Business_bar_perc, ups_Business_breakfast_perc,
                     ups_Business_other_perc]

index_table_ups = ['Restaurant', 'Bar', 'Breakfast', 'Other']
columns_table_ups = ['Avg Revenues', 'Absolute %']

table_upselling_marks_Solo_Travellers = pd.DataFrame(index=index_table_ups, data={'Avg Revenues': ups_Solo_Travellers,
                                                                                  'Absolute %': ups_Solo_Travellers_perc},
                                                     columns=columns_table_ups).reset_index()
table_upselling_marks_Family = pd.DataFrame(index=index_table_ups,
                                            data={'Avg Revenues': ups_Family, 'Absolute %': ups_Family_perc},
                                            columns=columns_table_ups).reset_index()
table_upselling_marks_Groups = pd.DataFrame(index=index_table_ups,
                                            data={'Avg Revenues': ups_Groups, 'Absolute %': ups_Groups_perc},
                                            columns=columns_table_ups).reset_index()
table_upselling_marks_Couples = pd.DataFrame(index=index_table_ups,
                                             data={'Avg Revenues': ups_Couples, 'Absolute %': ups_Couples_perc},
                                             columns=columns_table_ups).reset_index()
table_upselling_marks_Business = pd.DataFrame(index=index_table_ups,
                                              data={'Avg Revenues': ups_Business, 'Absolute %': ups_Business_perc},
                                              columns=columns_table_ups).reset_index()

table_upselling_marks_Solo_Travellers1 = graph_layouts.RightTable(table_upselling_marks_Solo_Travellers).returning_table()
table_upselling_marks_Family1 = graph_layouts.RightTable(table_upselling_marks_Family).returning_table()
table_upselling_marks_Groups1 = graph_layouts.RightTable(table_upselling_marks_Groups).returning_table()
table_upselling_marks_Couples1 = graph_layouts.RightTable(table_upselling_marks_Couples).returning_table()
table_upselling_marks_Business1 = graph_layouts.RightTable(table_upselling_marks_Business).returning_table()

traces_ups_marks = [table_upselling_marks_Solo_Travellers1, table_upselling_marks_Family1,
                    table_upselling_marks_Groups1, table_upselling_marks_Couples1, table_upselling_marks_Business1]

updatemenus_marks = list(
    [dict(active=-1,
          buttons=list([
              dict(label='Solo Travellers',
                   method='update',
                   args=[{'visible': [True, False, False, False, False]}, ]),
              dict(label='Family',
                   method='update',
                   args=[{'visible': [False, True, False, False, False]}, ]),
              dict(label='Groups',
                   method='update',
                   args=[{'visible': [False, False, True, False, False]}, ]),
              dict(label='Couples',
                   method='update',
                   args=[{'visible': [False, False, False, True, False]}, ]),
              dict(label='Business',
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


""" NEEDED ?? """
layout_donuts_marks = {
    "title": "Guests by market segment",
    "grid": {"rows": 1, "columns": 6},
    'height': 450,
    # 'autosize':False, Risk that doesn't work in other devices

    "annotations": [
        {"font": {"size": 15},
         "showarrow": False,
         "text": "27",
         "x": 0.15,
         "y": 0.5
         },

        {"font": {"size": 15},
         "showarrow": False,
         "text": "27",
         "x": 0.15,
         "y": 0.5
         },

        {"font": {"size": 15},
         "showarrow": False,
         "text": "27",
         "x": 0.15,
         "y": 0.5
         },
        {"font": {"size": 15},
         "showarrow": False,
         "text": "27",
         "x": 0.15,
         "y": 0.5
         },

        {"font": {"size": 15},
         "showarrow": False,
         "text": "27",
         "x": 0.15,
         "y": 0.5
         },

        {"font": {"size": 15},
         "showarrow": False,
         "text": "27",
         "x": 0.15,
         "y": 0.5
         },
    ]
}
