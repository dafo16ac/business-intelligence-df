from datetime import datetime as dt
from textwrap import dedent
import dash_core_components as dcc
from dash.dependencies import Output
import dash_html_components as html

from data.age_values import *
from data.distr_channel_values import *
from data.market_segments_values import *
from data.customer_type_values import *
from data.threed_plot import *
from data.choropleth_map import *
from data.time_series import *
from settings import *

app.title = 'Davide - Strategic Dashboard'
app.layout = html.Div(children=[
    html.Header(children='Market Segmentation Dashboard',
                style={'textAlign': 'center',
                       'color': 'white',
                       'fontSize': 60,
                       'font-weight': 'bold',
                       'backgroundColor': '#96151d'}),

    html.H4(children='''
         Clustering customers based on daily revenues and satisfaction with machine learning
    ''',
            style={'color': 'black',
                   'textAlign': 'center',
                   'backgroundColor': '#fafafa'}),

    dcc.Markdown(dedent(
        '''developed by [Davide Fogarolo](https://www.linkedin.com/in/davide-fogarolo) (first released in 2019)'''),
        style={'textAlign': 'center',
               'color': 'black',
               'fontSize': 12,
               'backgroundColor': '#fafafa'}),

    html.Div([
        dcc.Graph(
            id='3d',  # graph_parameters
            config={'displayModeBar': False},
            figure={'data': traces_3d,
                    'layout': go.Layout(dict(
                        margin=dict(
                            l=0,
                            r=0,
                            b=0,
                            t=0
                        ),

                        legend={'x': 0, 'y': 1},
                        # it has to be traces, I see it hard to insert the data of the column IDlabel
                        # COLOR THEME
                        plot_bgcolor="#fafafa",
                        paper_bgcolor="#fafafa",
                        showlegend=True,
                        scene=dict(
                            xaxis=dict(title='Rating'),
                            yaxis=dict(title='Revenues per day'),
                            zaxis=dict(title='Cross-selling per day'),
                        )
                    ))}, className="seven columns"
        ),

        dcc.Markdown(dedent('''

        **ASSUMPTIONS:** Revenues is determined by volumes and prices. In the hotel industry, the volume of revenues strictly from the rooms is constrained by the maximum number of guests that can be hosted in the facilities, which is then reflected in the ADR metric.
        The ability to charge higher prices, all else equal, depends on customer satisfaction and on the consequent longer term brand perception. 
        In-house up- and cross-selling are other important components in affecting revenue streams.
        The assumption of the present approach is that customer satisfaction, in-house up- and cross-selling can be better explained by behavioural and demographic factors of the customers hosted.
        
        **RATIONALE:** *In order to increase overall revenues volumes while being able to charge higher prices, this model identifies those guests that are most satisfied and most willing to spend in-house.*
        The two features of the model are: (1) daily revenues (sum of cross-selling and room rates revenues), and (2) rating scores satisfaction. The three-dimension graphical solution has been chosen to better decipher the impact of different sources of revenues.
        
        **RESULTS**: The model generates six clusters whose customers are characterized by distinctive level of revenues and rating scores.
        By being able of slicing and dicing the characteristics of the most attractive clusters, management, marketing, 
        and operations departments will have greater business intelligence and better understanding whom to target and on what to invest next. Worth to be noted, this dataset is not representative of real customers, and any pattern identified will depend on the specific case to which is applied.

        '''), className="five columns")
    ], className="row"),

    html.Div([
        html.P("Start by choosing the cluster and the time span you want to analyse",
               style={'font-size': '22px', 'color': 'white', 'textAlign': 'center', 'font-weight': 'bold'},
               className='one row'),
        html.P("    ", className='one column'),

        dcc.RadioItems(
            id='radioItems_clusters',
            options=[
                {'label': 'High TotRev & Rating', 'value': 3},
                {'label': 'High Rating', 'value': 1},
                {'label': 'High TotRev', 'value': 2},
                {'label': 'Medium TotRev & Rating', 'value': 0},
                {'label': 'Medium-low TotRev & Rating', 'value': 4},
                {'label': 'Low TotRev', 'value': 5}],
            labelStyle={'display': 'inline-block', 'font': 15},
            inputStyle={"margin-left": "15px"},  # margin between the select button and the next label
            style={'color': 'white', 'font-size': '12px'},
            className='seven columns'),

        dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=dt(2016, 10, 1),
            max_date_allowed=dt(2016, 11, 30),
            start_date=dt(2016, 10, 1),
            end_date=dt(2016, 11, 30),
            initial_visible_month=dt(2016, 11, 1),
            className='three columns',
            style={'font-size': '11px'}  # not working
        ),
    ], style={'backgroundColor': '#96151d', 'font': 14, 'padding': 10, 'border': '2px red solid', 'borderRadius': 5,
              'margin-bottom': '2rem', 'margin-top': '2rem'},
        className="row"),

    html.Div([
        dcc.Graph(
            id='lines',  # graph_parameters
            config={'displayModeBar': False},
            figure={'data': traces,
                    'layout': layout_scatter_slider},
            className='six columns'
        ),

        html.Div([

            dcc.Dropdown(
                id='dropdown_parameters',
                placeholder="Select the parameter to be geographically displayed",
                options=[{"label": i, "value": i} for i in values_choro[['TOT_revenues', 'Rating', 'Upselling']]]
                , className='one row'),

            dcc.Graph(
                id='map-world',
                config={'displayModeBar': False},
                figure={
                    'data': data_map_revenues,
                    'layout': layout_map},
                className='one row'
            ),
        ], className='six columns'),
    ], className='row'),

    html.Div([

        html.Div([
            dcc.Graph(
                id='tables_block',
                config={'displayModeBar': False},
                figure={'data': [go.Histogram(x=hotel_data['Age'],
                                              marker=dict(color='#3ddcca', ),
                                              text='Guests by Age',
                                              nbinsx=40, ),
                                 table_age1,
                                 data_donuts_age1,
                                 data_donuts_age2,
                                 data_donuts_age3,
                                 data_donuts_age4,
                                 data_donuts_age5,

                                 table_marksegment1,
                                 data_donuts_marks1,
                                 data_donuts_marks2,
                                 data_donuts_marks3,
                                 data_donuts_marks5,
                                 data_donuts_marks6,

                                 table_customer_type1,
                                 data_donuts_cs1,
                                 data_donuts_cs2,
                                 data_donuts_cs3,
                                 data_donuts_cs4,
                                 table_age_title,
                                 table_marks_title,
                                 table_ct_title
                                 ],

                        'layout':
                            go.Layout(showlegend=False,
                                      height=1420,
                                      xaxis=dict(domain=[0.36, 1]),
                                      xaxis1=dict(title='Age Distribution', domain=[0.30, 1]),
                                      xaxis2=dict(domain=[0.22, 0.32]),
                                      xaxis3=dict(domain=[0.33, 0.43]),
                                      xaxis4=dict(domain=[0.44, 0.54]),
                                      xaxis5=dict(domain=[0.55, 0.66]),
                                      xaxis6=dict(domain=[0.55, 0.66]),

                                      yaxis=dict(domain=[0.65, 0.72]),
                                      yaxis1=dict(title='N° of guests', domain=[0.70, .74]),
                                      yaxis2=dict(domain=[0.85, 1]),
                                      yaxis3=dict(domain=[0.70, 1]),
                                      yaxis4=dict(domain=[0.70, 1]),
                                      yaxis5=dict(domain=[0.70, 1]),
                                      yaxis6=dict(domain=[0.70, 1]),

                                      xaxis7=dict(domain=[0.7, 1]),
                                      xaxis8=dict(domain=[0.7, 1]),
                                      xaxis9=dict(domain=[0.30, 0.37]),
                                      xaxis10=dict(domain=[0.38, 0.45]),
                                      xaxis11=dict(domain=[0.44, 0.54]),
                                      xaxis12=dict(domain=[0.55, 0.66]),
                                      xaxis13=dict(domain=[0.55, 0.66]),

                                      yaxis7=dict(domain=[0, 1]),
                                      yaxis8=dict(domain=[0, 1]),
                                      yaxis9=dict(domain=[0.85, 1]),
                                      yaxis10=dict(domain=[0.3, .6]),
                                      yaxis11=dict(domain=[0.3, .6]),
                                      yaxis12=dict(domain=[0.3, .6]),
                                      yaxis13=dict(domain=[0.3, .6]),

                                      xaxis14=dict(domain=[0.7, 1]),
                                      xaxis15=dict(domain=[0.7, 1]),
                                      xaxis16=dict(domain=[0.30, 0.37]),
                                      xaxis17=dict(domain=[0.38, 0.45]),
                                      xaxis18=dict(domain=[0.44, 0.54]),

                                      yaxis14=dict(domain=[0, 1]),
                                      yaxis15=dict(domain=[0, 0.3]),
                                      yaxis16=dict(domain=[0, 0.3]),
                                      yaxis17=dict(domain=[0, 0.3]),
                                      yaxis18=dict(domain=[0, 0.3]),

                                      margin=dict(l=0.15,
                                                  r=0,
                                                  t=0,
                                                  b=0),
                                      plot_bgcolor="#fafafa",
                                      paper_bgcolor="#fafafa",
                                      ),
                        },
                className="six columns",
            )]),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='pie_age',
                    config={'displayModeBar': False},
                    figure={'data': values_upselling_pie_age + traces_ups_age,
                            'layout': dict(height=410, updatemenus=updatemenus_age, showlegend=True,
                                           legend=dict(orientation="h", y=0.25),
                                           plot_bgcolor="#fafafa",
                                           paper_bgcolor="#fafafa",
                                           margin=dict(l=0,
                                                       r=0,
                                                       t=0,
                                                       b=0))},
                ),
            ], className='one row'),

            html.Div([
                html.P("                "
                       ),
            ], className='one row', style={'margin-bottom': '20rem'}),

            html.Div([
                dcc.Graph(
                    id='pie_marks',
                    config={'displayModeBar': False},
                    figure={'data': values_upselling_pie_marks + traces_ups_marks,
                            'layout': dict(height=410, updatemenus=updatemenus_marks, showlegend=True,
                                           legend=dict(orientation="h", y=0.25),
                                           plot_bgcolor="#fafafa",
                                           paper_bgcolor="#fafafa",
                                           margin=dict(l=0,
                                                       r=0,
                                                       t=0,
                                                       b=0))},
                ),
            ], className='one row'),

            html.Div([
                dcc.Graph(
                    id='pie_ct',
                    config={'displayModeBar': False},
                    figure={'data': values_upselling_pie_ct + traces_ups_ct,
                            'layout': dict(height=410, updatemenus=updatemenus_ct, showlegend=True,
                                           legend=dict(orientation="h", y=0.25),
                                           plot_bgcolor="#fafafa",
                                           paper_bgcolor="#fafafa",

                                           margin=dict(l=0,
                                                       r=0,
                                                       t=0,
                                                       b=0))},
                ),
            ], className='one row'),
        ], className='six columns'),
    ], className='one row'),

    html.Div([
        html.Div([
            dcc.Graph(
                id='table_dchannel',
                config={'displayModeBar': False},
                figure={'data': [table_dchannel1,
                                 data_donuts_dc1,
                                 data_donuts_dc2,
                                 data_donuts_dc3,
                                 data_donuts_dc4,
                                 table_dc_title],

                        'layout':
                            go.Layout(showlegend=False,
                                      height=410,
                                      xaxis1=dict(domain=[0.7, 1]),
                                      xaxis2=dict(domain=[0.7, 1]),
                                      xaxis3=dict(domain=[0.30, 0.37]),
                                      xaxis4=dict(domain=[0.38, 0.45]),
                                      xaxis5=dict(domain=[0.44, 0.54]),
                                      xaxis6=dict(domain=[0.44, 0.54]),

                                      yaxis1=dict(domain=[0, 1]),
                                      yaxis2=dict(domain=[0, 0.3]),
                                      yaxis3=dict(domain=[0, 0.3]),
                                      yaxis4=dict(domain=[0, 0.3]),
                                      yaxis5=dict(domain=[0, 0.3]),
                                      yaxis6=dict(domain=[0.44, 0.54]),
                                      margin=dict(l=0.15,
                                                  r=0,
                                                  t=0,
                                                  b=0),
                                      plot_bgcolor="#fafafa",
                                      paper_bgcolor="#fafafa",
                                      ),
                        },

            )], className='six columns'),

        html.Div([
            dcc.Graph(
                id='pie_dc',
                config={'displayModeBar': False},
                figure={'data': values_upselling_pie_dc + traces_ups_dc,
                        'layout': dict(height=410, updatemenus=updatemenus_dc, showlegend=True,
                                       legend=dict(orientation="h", y=0.25),
                                       plot_bgcolor="#fafafa",
                                       paper_bgcolor="#fafafa",
                                       margin=dict(l=0,
                                                   r=0,
                                                   t=0,
                                                   b=0))},
            ),
        ], className='six columns'),
    ], className='one row'),

    html.Div([
        dcc.Markdown(dedent('''



        **Methodological choice**

        Whereas K-means is the most common clustering technique, it also resulted not optimal in this case, because K-means starts from centroids and it is optimal for clusters with a spheroic form.
        In fact, in this model I use Spectral Clustering, which results being much more accurate and substantiating business intuitions.




        **Terminology**

        'Revenues by day': average revenues per customer, considering strictly room revenues.

        'Rating': used to measure guests' satisfaction, it is a rating score between 1-10.

        'Cross'-selling: average daily spenditure, divided by Restaurant, Breakfast, Bar, or Other sources of income.

        'TOT_ADR': sum of Revenues by day and Upselling revenues.

        'TOT_Revenues': TOT_ADR multiplied by the length of staying (nights), expressed in DKK.

        'Travel Companion': guests segmentation according to the objective/companion they are traveling with.

        'Customer type': Type of booking, assuming one of four categories; Contract (i.e. the booking has an allotment associated to it); Group (i.e. the booking is associated to a group); 
        Transient (i.e. the booking is not part of a group or contract, and is not associated to other transient booking); Transient-party (i.e. the booking is transient, but is associated to at least other transient booking).

        'Distribution channel':  the different methods in which bookings for the hotel are made; they are TA/TO (“TA” means “TravelAgents” and “TO” means “TourOperators”); Direct (directly with the hotel); GDS (global distribution system).



        '''))
    ], className='one row')
],
    style={'border-radius': 3}, )

""" CALLBACKS """


@app.callback(dash.dependencies.Output('lines', 'figure'),
              [dash.dependencies.Input('radioItems_clusters', 'value'),
               dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_time_slider(radioItems_clusters_value, start_date, end_date):
    cl_selected_r = hotel_data.loc[hotel_data['IDlabelsClusters'] == radioItems_clusters_value]

    cl_selected = cl_selected_r[
        (cl_selected_r['TimeArrival'] >= start_date) & (cl_selected_r['TimeArrival'] <= end_date)].copy()

    TimeSeriesDate_callback = cl_selected.groupby(['TimeArrival']).mean()

    revenues_scatter_callback = go.Scatter(x=TimeSeriesDate_callback.index,
                                           y=TimeSeriesDate_callback['TOT_ADR'].rolling(window=3).mean(),
                                           name='Tot Revenues per day',
                                           line=dict(
                                               color=('#dc3d4f'),
                                               width=1.5, ))

    rating_scatter_callback = go.Scatter(x=TimeSeriesDate_callback.index,
                                         y=TimeSeriesDate_callback['Rating'].rolling(window=3).mean(),
                                         name='Rating',
                                         yaxis='y2',
                                         line=dict(
                                             color=('#3DDCCA'),
                                             width=1.5, ))
    traces_callback = [rating_scatter_callback, revenues_scatter_callback]
    figure = {'data': traces_callback, 'layout': layout_scatter_slider}
    return figure


# BLOCK TABLES CALLBACK
@app.callback(dash.dependencies.Output('tables_block', 'figure'),
              [dash.dependencies.Input('radioItems_clusters', 'value'),
               dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_table_blocks(radioItems_clusters_value, start_date, end_date):
    cl_selected_r = hotel_data.loc[hotel_data['IDlabelsClusters'] == radioItems_clusters_value]
    cl_selected = cl_selected_r[
        (cl_selected_r['TimeArrival'] >= start_date) & (cl_selected_r['TimeArrival'] <= end_date)].copy()

    # AGE BLOCK
    children_callback = cl_selected.loc[(cl_selected['Age'] < 18)]
    adults_32_callback = cl_selected.loc[(18 <= cl_selected['Age']) & (cl_selected['Age'] <= 32)]
    adults_48_callback = cl_selected.loc[(33 <= cl_selected['Age']) & (cl_selected['Age'] <= 48)]
    adults_66_callback = cl_selected.loc[(49 <= cl_selected['Age']) & (cl_selected['Age'] <= 66)]
    adults_plus_callback = cl_selected.loc[cl_selected['Age'] > 66]

    tot_age_perc_callback = cl_selected['Age'].count()
    children_perc_callback = children_callback['Age'].count()
    adults_32_perc_callback = adults_32_callback['Age'].count()
    adults_48_perc_callback = adults_48_callback['Age'].count()
    adults_66_perc_callback = adults_66_callback['Age'].count()
    adults_plus_perc_callback = adults_plus_callback['Age'].count()

    children_mean_callback = round(children_callback['Upselling'].mean(), ndigits=1)
    adults_32_mean_callback = round(adults_32_callback['Upselling'].mean(), ndigits=1)
    adults_48_mean_callback = round(adults_48_callback['Upselling'].mean(), ndigits=1)
    adults_66_mean_callback = round(adults_66_callback['Upselling'].mean(), ndigits=1)
    adults_plus_mean_callback = round(adults_plus_callback['Upselling'].mean(), ndigits=1)

    childrenRev_mean_callback = round(children_callback['Revenues by day'].mean(), ndigits=1)
    youngRev_32_mean_callback = round(adults_32_callback['Revenues by day'].mean(), ndigits=1)
    adultsRev_48_mean_callback = round(adults_48_callback['Revenues by day'].mean(), ndigits=1)
    adultsRev_66_mean_callback = round(adults_66_callback['Revenues by day'].mean(), ndigits=1)
    adultsRev_plus_mean_callback = round(adults_plus_callback['Revenues by day'].mean(), ndigits=1)

    children_rating_callback = round(children_callback['Rating'].mean(), ndigits=1)
    adults_32_rating_callback = round(adults_32_callback['Rating'].mean(), ndigits=1)
    adults_48_rating_callback = round(adults_48_callback['Rating'].mean(), ndigits=1)
    adults_66_rating_callback = round(adults_66_callback['Rating'].mean(), ndigits=1)
    adults_plus_rating_callback = round(adults_plus_callback['Rating'].mean(), ndigits=1)

    children_nights_callback = round(children_callback['Nights'].mean(), ndigits=1)
    adults_32_nights_callback = round(adults_32_callback['Nights'].mean(), ndigits=1)
    adults_48_nights_callback = round(adults_48_callback['Nights'].mean(), ndigits=1)
    adults_66_nights_callback = round(adults_66_callback['Nights'].mean(), ndigits=1)
    adults_plus_nights_callback = round(adults_plus_callback['Nights'].mean(), ndigits=1)

    children_wd_callback = round(children_callback['StaysInWeekNights'].mean(), ndigits=1)
    adults_32_wd_callback = round(adults_32_callback['StaysInWeekNights'].mean(), ndigits=1)
    adults_48_wd_callback = round(adults_48_callback['StaysInWeekNights'].mean(), ndigits=1)
    adults_66_wd_callback = round(adults_66_callback['StaysInWeekNights'].mean(), ndigits=1)
    adults_plus_wd_callback = round(adults_plus_callback['StaysInWeekNights'].mean(), ndigits=1)

    children_we_callback = round(children_callback['StaysInWeekendNights'].mean(), ndigits=1)
    adults_32_we_callback = round(adults_32_callback['StaysInWeekendNights'].mean(), ndigits=1)
    adults_48_we_callback = round(adults_48_callback['StaysInWeekendNights'].mean(), ndigits=1)
    adults_66_we_callback = round(adults_66_callback['StaysInWeekendNights'].mean(), ndigits=1)
    adults_plus_we_callback = round(adults_plus_callback['StaysInWeekendNights'].mean(), ndigits=1)

    try:
        children_nation_rev = \
        children_callback.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[
            0]
    except IndexError:
        children_nation_rev = 'null'

    try:
        adults_32_nation_rev = \
            adults_32_callback.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_32_nation_rev = 'null'

    try:
        adults_48_nation_rev = \
            adults_48_callback.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_48_nation_rev = 'null'

    try:
        adults_66_nation_rev = \
            adults_66_callback.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_66_nation_rev = 'null'

    try:
        adults_plus_nation_rev = \
            adults_plus_callback.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_plus_nation_rev = 'null'

    try:
        children_nation_rating = \
        children_callback.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        children_nation_rating = 'null'

    try:
        adults_32_nation_rating = \
        adults_32_callback.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_32_nation_rating = 'null'

    try:
        adults_48_nation_rating = \
        adults_48_callback.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_48_nation_rating = 'null'

    try:
        adults_66_nation_rating = \
        adults_66_callback.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_66_nation_rating = 'null'

    try:
        adults_plus_nation_rating = \
        adults_plus_callback.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[
            0]
    except IndexError:
        adults_plus_nation_rating = 'null'

    try:
        children_nation_upselling = \
        children_callback.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[
            0]
    except IndexError:
        children_nation_upselling = 'null'

    try:
        adults_32_nation_upselling = \
            adults_32_callback.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_32_nation_upselling = 'null'

    try:
        adults_48_nation_upselling = \
            adults_48_callback.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_48_nation_upselling = 'null'

    try:
        adults_66_nation_upselling = \
            adults_66_callback.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_66_nation_upselling = 'null'

    try:
        adults_plus_nation_upselling = \
            adults_plus_callback.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        adults_plus_nation_upselling = 'null'

    columns_age = ['children', 'adults_32', 'adults_48', 'adults_66', 'adults_plus']
    index_age = ['Cross-selling mean', 'Revenues mean', 'Rating mean', 'Length staying mean (days)', ' - N° Weekdays',
                 ' - N° Weekend days', 'Nationality highest revenues', 'Nationality highest rating',
                 'Nationality highest upselling']

    table_a = pd.DataFrame(data=[
        [children_mean_callback, adults_32_mean_callback, adults_48_mean_callback, adults_66_mean_callback,
         adults_plus_mean_callback],
        [childrenRev_mean_callback, youngRev_32_mean_callback, adultsRev_48_mean_callback, adultsRev_66_mean_callback,
         adultsRev_plus_mean_callback],
        [children_rating_callback, adults_32_rating_callback, adults_48_rating_callback, adults_66_rating_callback,
         adults_plus_rating_callback],
        [children_nights_callback, adults_32_nights_callback, adults_48_nights_callback, adults_66_nights_callback,
         adults_plus_nights_callback],
        [children_wd_callback, adults_32_wd_callback, adults_48_wd_callback, adults_66_wd_callback,
         adults_plus_wd_callback],
        [children_we_callback, adults_32_we_callback, adults_48_we_callback, adults_66_we_callback,
         adults_plus_we_callback],
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
        header=dict(height=20,
                    values=[[''], ['<b>Children</b>'],
                            ['<b>18-32</b>'], ['<b>33-48</b>'], ['<b>49-66</b>'], ['<b>67+</b>']],
                    line=dict(color='rgb(50, 50, 50)'),
                    align=['left'],
                    font=dict(color=['white'] * 5, size=10),
                    fill=dict(color='black')),
        cells=dict(values=[table_age[k].tolist() for k in
                           ['index', 'children', 'adults_32', 'adults_48', 'adults_66', 'adults_plus']],
                   line=dict(color='#506784'),
                   align=['left'] * 5,
                   font=dict(color=['rgb(40, 40, 40)'] * 5, size=10),
                   height=20,
                   fill=dict(color=['#a9efe8', '#eafbf8']))
    )

    data_donuts_age1 = {
        "values": [children_perc_callback, tot_age_perc_callback - children_perc_callback],
        "title": "{0:.1%}".format(children_perc_callback / (tot_age_perc_callback)),
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
        "values": [adults_32_perc_callback, tot_age_perc_callback - adults_32_perc_callback],
        "title": "{0:.1%}".format(adults_32_perc_callback / (tot_age_perc_callback)),
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
        "values": [adults_48_perc_callback, tot_age_perc_callback - adults_48_perc_callback],
        "title": "{0:.1%}".format(adults_48_perc_callback / (tot_age_perc_callback)),
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
        "values": [adults_66_perc_callback, tot_age_perc_callback - adults_66_perc_callback],
        "title": "{0:.1%}".format(adults_66_perc_callback / (tot_age_perc_callback)),
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
        "values": [adults_plus_perc_callback, tot_age_perc_callback - adults_plus_perc_callback],
        "title": "{0:.1%}".format(adults_plus_perc_callback / (tot_age_perc_callback)),
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

    # MARKET SEGMENT BLOCK
    Solo_Travellers = cl_selected.loc[cl_selected['MarketSegment'] == 'Solo Travellers']
    Family = cl_selected.loc[cl_selected['MarketSegment'] == 'Family']
    Groups = cl_selected.loc[cl_selected['MarketSegment'] == 'Groups']
    Couples = cl_selected.loc[cl_selected['MarketSegment'] == 'Couples']
    Business = cl_selected.loc[cl_selected['MarketSegment'] == 'Business']

    tot_marks_perc = cl_selected['MarketSegment'].count()
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

    try:
        Solo_Travellers_nation_rev = \
            Solo_Travellers.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Solo_Travellers_nation_rev = 'null'

    try:
        Family_nation_rev = Family.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Family_nation_rev = 'null'

    try:
        Groups_nation_rev = Groups.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Groups_nation_rev = 'null'

    try:
        Couples_nation_rev = Couples.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Couples_nation_rev = 'null'

    try:
        Business_nation_rev = Business.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[
            0]
    except IndexError:
        Business_nation_rev = 'null'

    try:
        Solo_Travellers_nation_rating = \
            Solo_Travellers.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Solo_Travellers_nation_rating = 'null'

    try:
        Family_nation_rating = Family.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Family_nation_rating = 'null'

    try:
        Groups_nation_rating = Groups.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Groups_nation_rating = 'null'

    try:
        Couples_nation_rating = Couples.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Couples_nation_rating = 'null'

    try:
        Business_nation_rating = Business.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Business_nation_rating = 'null'

    try:
        Solo_Travellers_nation_upselling = \
            Solo_Travellers.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Solo_Travellers_nation_upselling = 'null'

    try:
        Family_nation_upselling = Family.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Family_nation_upselling = 'null'

    try:
        Groups_nation_upselling = Groups.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Groups_nation_upselling = 'null'

    try:
        Couples_nation_upselling = Couples.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        Couples_nation_upselling = 'null'

    try:
        Business_nation_upselling = Business.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[
            0]
    except IndexError:
        Business_nation_upselling = 'null'

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

    # CUSTOMER TYPE BLOCK
    transient = cl_selected.loc[cl_selected['CustomerType'] == 'Transient']
    transient_party = cl_selected.loc[cl_selected['CustomerType'] == 'Transient-Party']
    contract = cl_selected.loc[cl_selected['CustomerType'] == 'Contract']
    group = cl_selected.loc[cl_selected['CustomerType'] == 'Group']

    tot_customertype_perc = cl_selected['CustomerType'].count()
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

    try:
        transient_nation_rev = \
            transient.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        transient_nation_rev = 'null'

    try:
        transient_party_nation_rev = \
            transient_party.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        transient_party_nation_rev = 'null'

    try:
        contract_nation_rev = contract.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[
            0]
    except IndexError:
        contract_nation_rev = 'null'

    try:
        group_nation_rev = group.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        group_nation_rev = 'null'

    try:
        transient_nation_rating = transient.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        transient_nation_rating = 'null'

    try:
        transient_party_nation_rating = \
            transient_party.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        transient_party_nation_rating = 'null'

    try:
        contract_nation_rating = contract.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        contract_nation_rating = 'null'

    try:
        group_nation_rating = group.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        group_nation_rating = 'null'

    try:
        transient_nation_upselling = \
            transient.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        transient_nation_upselling = 'null'

    try:
        transient_party_nation_upselling = \
            transient_party.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        transient_party_nation_upselling = 'null'

    try:
        contract_nation_upselling = contract.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[
            0]
    except IndexError:
        contract_nation_upselling = 'null'

    try:
        group_nation_upselling = group.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        group_nation_upselling = 'null'

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
        [transient_nation_upselling, transient_party_nation_upselling, contract_nation_upselling,
         group_nation_upselling]
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

    block_tables = {'data': [go.Histogram(x=cl_selected['Age'],
                                          marker=dict(color='#3ddcca', ),
                                          text='Guests by Age',
                                          nbinsx=40, ),
                             table_age1,
                             data_donuts_age1,
                             data_donuts_age2,
                             data_donuts_age3,
                             data_donuts_age4,
                             data_donuts_age5,

                             table_marksegment1,
                             data_donuts_marks1,
                             data_donuts_marks2,
                             data_donuts_marks3,
                             data_donuts_marks5,
                             data_donuts_marks6,

                             table_customer_type1,
                             data_donuts_cs1,
                             data_donuts_cs2,
                             data_donuts_cs3,
                             data_donuts_cs4,
                             table_age_title,
                             table_marks_title,
                             table_ct_title
                             ],

                    'layout':
                        go.Layout(showlegend=False,
                                  height=1420,
                                  xaxis=dict(domain=[0.36, 1]),
                                  xaxis1=dict(title='Age', domain=[0.30, 1]),
                                  xaxis2=dict(domain=[0.22, 0.32]),
                                  xaxis3=dict(domain=[0.33, 0.43]),
                                  xaxis4=dict(domain=[0.44, 0.54]),
                                  xaxis5=dict(domain=[0.55, 0.66]),
                                  xaxis6=dict(domain=[0.55, 0.66]),

                                  yaxis=dict(domain=[0.65, 0.72]),
                                  yaxis1=dict(title='N° of guests', domain=[0.70, 0.74]),
                                  yaxis2=dict(domain=[0.85, 1]),
                                  yaxis3=dict(domain=[0.70, 1]),
                                  yaxis4=dict(domain=[0.70, 1]),
                                  yaxis5=dict(domain=[0.70, 1]),
                                  yaxis6=dict(domain=[0.70, 1]),

                                  xaxis7=dict(domain=[0.7, 1]),
                                  xaxis8=dict(domain=[0.7, 1]),
                                  xaxis9=dict(domain=[0.30, 0.37]),
                                  xaxis10=dict(domain=[0.38, 0.45]),
                                  xaxis11=dict(domain=[0.44, 0.54]),
                                  xaxis12=dict(domain=[0.55, 0.66]),
                                  xaxis13=dict(domain=[0.55, 0.66]),

                                  yaxis7=dict(domain=[0, 1]),
                                  yaxis8=dict(domain=[0, 1]),
                                  yaxis9=dict(domain=[0.85, 1]),
                                  yaxis10=dict(domain=[0.3, .6]),
                                  yaxis11=dict(domain=[0.3, .6]),
                                  yaxis12=dict(domain=[0.3, .6]),
                                  yaxis13=dict(domain=[0.3, .6]),

                                  xaxis14=dict(domain=[0.7, 1]),
                                  xaxis15=dict(domain=[0.7, 1]),
                                  xaxis16=dict(domain=[0.30, 0.37]),
                                  xaxis17=dict(domain=[0.38, 0.45]),
                                  xaxis18=dict(domain=[0.44, 0.54]),

                                  yaxis14=dict(domain=[0, 1]),
                                  yaxis15=dict(domain=[0, 0.3]),
                                  yaxis16=dict(domain=[0, 0.3]),
                                  yaxis17=dict(domain=[0, 0.3]),
                                  yaxis18=dict(domain=[0, 0.3]),

                                  margin=dict(l=0.15, r=0, t=0, b=0),
                                  plot_bgcolor="#fafafa",
                                  paper_bgcolor="#fafafa",
                                  ),
                    }
    return block_tables


# MARKS BLOCK PIE
@app.callback(dash.dependencies.Output('pie_marks', 'figure'),
              [dash.dependencies.Input('radioItems_clusters', 'value'),
               dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_pie_marks(radioItems_clusters_value, start_date, end_date):
    cl_selected_r = hotel_data.loc[hotel_data['IDlabelsClusters'] == radioItems_clusters_value]
    cl_selected = cl_selected_r[
        (cl_selected_r['TimeArrival'] >= start_date) & (cl_selected_r['TimeArrival'] <= end_date)]

    values_upselling_st = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['MarketSegment'] == 'Solo Travellers'].sum()
    values_upselling_st = values_upselling_st.tolist()

    values_upselling_fam = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['MarketSegment'] == 'Family'].sum()
    values_upselling_fam = values_upselling_fam.tolist()

    values_upselling_groups = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['MarketSegment'] == 'Groups'].sum()
    values_upselling_groups = values_upselling_groups.tolist()

    values_upselling_Business = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['MarketSegment'] == 'Business'].sum()
    values_upselling_Business = values_upselling_Business.tolist()

    values_upselling_couples = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['MarketSegment'] == 'Couples'].sum()
    values_upselling_couples = values_upselling_couples.tolist()

    values_upselling_marks = [values_upselling_st, values_upselling_fam, values_upselling_groups,
                              values_upselling_Business, values_upselling_couples]

    updatemenus_marks = list(
        [dict(active=-1,
              buttons=list([
                  dict(label='Solo Travellers',
                       method='update',
                       args=[{'visible': [True, False, False, False, False]}]),
                  dict(label='Family',
                       method='update',
                       args=[{'visible': [False, True, False, False, False]}]),
                  dict(label='Groups',
                       method='update',
                       args=[{'visible': [False, False, True, False, False]}]),
                  dict(label='Couples',
                       method='update',
                       args=[{'visible': [False, False, False, True, False]}]),
                  dict(label='Business',
                       method='update',
                       args=[{'visible': [False, False, False, False, True]}])
              ]),
              direction='down',
              yanchor='top',
              xanchor='left',
              x=0.5,
              y=.95,
              )
         ])

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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
    }

    values_upselling_pie_marks = [pie_marks_st, pie_marks_fam, pie_marks_groups, pie_marks_couples, pie_marks_business]

    """ MARKET SEGMENT UPSELLING VALUES """
    Solo_Travellers = cl_selected.loc[cl_selected['MarketSegment'] == 'Solo Travellers']
    Family = cl_selected.loc[cl_selected['MarketSegment'] == 'Family']
    Groups = cl_selected.loc[cl_selected['MarketSegment'] == 'Groups']
    Couples = cl_selected.loc[cl_selected['MarketSegment'] == 'Couples']
    Business = cl_selected.loc[cl_selected['MarketSegment'] == 'Business']

    tot_marks_perc = cl_selected['MarketSegment'].count()
    Solo_Travellers_perc = Solo_Travellers['MarketSegment'].count()
    Family_perc = Family['MarketSegment'].count()
    Groups_perc = Groups['MarketSegment'].count()
    Couples_perc = Couples['MarketSegment'].count()
    Business_perc = Business['MarketSegment'].count()

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

    ups_tot = cl_selected['Upselling'].sum()

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
    ups_Family_perc = [ups_Family_restaurant_perc, ups_Family_bar_perc, ups_Family_breakfast_perc,
                       ups_Family_other_perc]
    ups_Groups_perc = [ups_Groups_restaurant_perc, ups_Groups_bar_perc, ups_Groups_breakfast_perc,
                       ups_Groups_other_perc]
    ups_Couples_perc = [ups_Couples_restaurant_perc, ups_Couples_bar_perc, ups_Couples_breakfast_perc,
                        ups_Couples_other_perc]
    ups_Business_perc = [ups_Business_restaurant_perc, ups_Business_bar_perc, ups_Business_breakfast_perc,
                         ups_Business_other_perc]

    index_table_ups = ['Restaurant', 'Bar', 'Breakfast', 'Other']
    columns_table_ups = ['Avg Revenues', 'Absolute %']

    table_upselling_marks_Solo_Travellers = pd.DataFrame(index=index_table_ups,
                                                         data={'Avg Revenues': ups_Solo_Travellers,
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

    table_upselling_marks_Solo_Travellers1 = graph_layouts.RightTable(
        table_upselling_marks_Solo_Travellers).returning_table()
    table_upselling_marks_Family1 = graph_layouts.RightTable(table_upselling_marks_Family).returning_table()
    table_upselling_marks_Groups1 = graph_layouts.RightTable(table_upselling_marks_Groups).returning_table()
    table_upselling_marks_Couples1 = graph_layouts.RightTable(table_upselling_marks_Couples).returning_table()
    table_upselling_marks_Business1 = graph_layouts.RightTable(table_upselling_marks_Business).returning_table()

    traces_ups_marks = [table_upselling_marks_Solo_Travellers1, table_upselling_marks_Family1,
                        table_upselling_marks_Groups1, table_upselling_marks_Couples1, table_upselling_marks_Business1]

    figure_marks = {'data': values_upselling_pie_marks + traces_ups_marks,
                    'layout': dict(height=410, updatemenus=updatemenus_marks, showlegend=True,
                                   legend=dict(orientation="h", y=0.25),
                                   plot_bgcolor="#fafafa",
                                   paper_bgcolor="#fafafa", margin=dict(l=0,
                                                                        r=0,
                                                                        t=0,
                                                                        b=0))}
    return figure_marks


# AGE CALLBACK
@app.callback(dash.dependencies.Output('pie_age', 'figure'),
              [dash.dependencies.Input('radioItems_clusters', 'value'),
               dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_pie_age(radioItems_clusters_value, start_date, end_date):
    cl_selected_r = hotel_data.loc[hotel_data['IDlabelsClusters'] == radioItems_clusters_value]
    cl_selected = cl_selected_r[
        (cl_selected_r['TimeArrival'] >= start_date) & (cl_selected_r['TimeArrival'] <= end_date)]
    # cl_selected['TimeArrival'] = pd.to_datetime(cl_selected['TimeArrival'])

    cl_selected['Age'] = cl_selected['Age'].round(0).copy()

    children = cl_selected.loc[cl_selected['Age'] < 18]
    adults_32 = cl_selected.loc[(18 <= cl_selected['Age']) & (cl_selected['Age'] <= 32)]
    adults_48 = cl_selected.loc[(33 <= cl_selected['Age']) & (cl_selected['Age'] <= 48)]
    adults_66 = cl_selected.loc[(49 <= cl_selected['Age']) & (cl_selected['Age'] <= 66)]
    adults_plus = cl_selected.loc[cl_selected['Age'] > 66]

    ups_tot = cl_selected['Upselling'].sum()
    tot_age_perc = cl_selected['Age'].count()
    children_perc = children['Age'].count()
    adults_32_perc = adults_32['Age'].count()
    adults_48_perc = adults_48['Age'].count()
    adults_66_perc = adults_66['Age'].count()
    adults_plus_perc = adults_plus['Age'].count()

    values_upselling_children = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['Age'] < 18].sum()
    values_upselling_children = values_upselling_children.tolist()

    values_upselling_adults32 = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        (18 <= cl_selected['Age']) & (cl_selected['Age'] <= 32)].sum()
    values_upselling_adults32 = values_upselling_adults32.tolist()

    values_upselling_adults48 = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        (33 <= cl_selected['Age']) & (cl_selected['Age'] <= 48)].sum()
    values_upselling_adults48 = values_upselling_adults48.tolist()

    values_upselling_adults66 = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        (49 <= cl_selected['Age']) & (cl_selected['Age'] <= 66)].sum()
    values_upselling_adults66 = values_upselling_adults66.tolist()

    values_upselling_adultsplus = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['Age'] > 66].sum()
    values_upselling_adultsplus = values_upselling_adultsplus.tolist()

    values_upselling_age = [values_upselling_children, values_upselling_adults32, values_upselling_adults48,
                            values_upselling_adults66, values_upselling_adultsplus]

    updatemenus_age = list(
        [dict(active=-1,
              buttons=list([
                  dict(label='Children',
                       method='update',
                       args=[{'visible': [True, False, False, False, False]}]),
                  dict(label='18-32',
                       method='update',
                       args=[{'visible': [False, True, False, False, False]}]),
                  dict(label='33-48',
                       method='update',
                       args=[{'visible': [False, False, True, False, False]}]),
                  dict(label='49-66',
                       method='update',
                       args=[{'visible': [False, False, False, True, False]}]),
                  dict(label='67+',
                       method='update',
                       args=[{'visible': [False, False, False, False, True]}])
              ]),
              direction='down',
              yanchor='top',
              xanchor='left',
              x=0.5,
              y=.95,
              )
         ])

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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
    }

    values_upselling_pie_age = [pie_age_child, pie_age_adults32, pie_age_adults48, pie_age_adults66, pie_age_adultsplus]

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
                       args=[{'visible': [True, False, False, False, False]}]),
                  dict(label='18-32',
                       method='update',
                       args=[{'visible': [False, True, False, False, False]}]),
                  dict(label='33-48',
                       method='update',
                       args=[{'visible': [False, False, True, False, False]}]),
                  dict(label='49-66',
                       method='update',
                       args=[{'visible': [False, False, False, True, False]}]),
                  dict(label='67+',
                       method='update',
                       args=[{'visible': [False, False, False, False, True]}])
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

    figure_age = {'data': values_upselling_pie_age + traces_ups_age,
                  'layout': dict(height=410, updatemenus=updatemenus_age, showlegend=True,
                                 legend=dict(orientation="h", y=0.25),
                                 plot_bgcolor="#fafafa",
                                 paper_bgcolor="#fafafa",
                                 margin=dict(l=0,
                                             r=0,
                                             t=0,
                                             b=0))}
    return figure_age


# CT callback
@app.callback(dash.dependencies.Output('pie_ct', 'figure'),
              [dash.dependencies.Input('radioItems_clusters', 'value'),
               dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_pie_ct(radioItems_clusters_value, start_date, end_date):
    cl_selected_r = hotel_data.loc[hotel_data['IDlabelsClusters'] == radioItems_clusters_value]
    cl_selected = cl_selected_r[
        (cl_selected_r['TimeArrival'] >= start_date) & (cl_selected_r['TimeArrival'] <= end_date)]

    transient = cl_selected.loc[cl_selected['CustomerType'] == 'Transient']
    transient_party = cl_selected.loc[cl_selected['CustomerType'] == 'Transient-Party']
    contract = cl_selected.loc[cl_selected['CustomerType'] == 'Contract']
    group = cl_selected.loc[cl_selected['CustomerType'] == 'Group']

    # Customer type pie
    values_upselling_transient = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['CustomerType'] == 'Transient'].sum().copy()
    values_upselling_transient = values_upselling_transient.tolist()

    values_upselling_transientP = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['CustomerType'] == 'Transient-Party'].sum().copy()
    values_upselling_transientP = values_upselling_transientP.tolist()

    values_upselling_contract = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['CustomerType'] == 'Contract'].sum().copy()
    values_upselling_contract = values_upselling_contract.tolist()

    values_upselling_group = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        cl_selected['CustomerType'] == 'Group'].sum().copy()
    values_upselling_group = values_upselling_group.tolist()

    updatemenus_ct = list(
        [dict(active=-1,
              buttons=list([
                  dict(label='Transient',
                       method='update',
                       args=[{'visible': [True, False, False, False]},
                             ]),
                  dict(label='Transient-Party',
                       method='update',
                       args=[{'visible': [False, True, False, False]},
                             ]),
                  dict(label='Contract',
                       method='update',
                       args=[{'visible': [False, False, True, False]},
                             ]),
                  dict(label='Group',
                       method='update',
                       args=[{'visible': [False, False, False, True]},
                             ])
              ]),
              direction='down',
              yanchor='top',
              xanchor='left',
              x=0.5,
              y=.95, )
         ])

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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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

    ups_tot = cl_selected['Upselling'].sum()

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

    figure_ct = {'data': values_upselling_pie_ct + traces_ups_ct,
                 'layout': dict(height=410, updatemenus=updatemenus_ct, showlegend=True,
                                legend=dict(orientation="h", y=0.25),
                                plot_bgcolor="#fafafa",
                                paper_bgcolor="#fafafa",
                                margin=dict(l=0,
                                            r=0,
                                            t=0,
                                            b=0))}
    return figure_ct


# DISTRIBUTION CHANNEL callback
@app.callback(dash.dependencies.Output('table_dchannel', 'figure'),
              [dash.dependencies.Input('radioItems_clusters', 'value'),
               dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_table_dchannel(radioItems_clusters_value, start_date, end_date):
    cl_selected_r = hotel_data.loc[hotel_data['IDlabelsClusters'] == radioItems_clusters_value]
    cl_selected = cl_selected_r[
        (cl_selected_r['TimeArrival'] >= start_date) & (cl_selected_r['TimeArrival'] <= end_date)]

    TATO = cl_selected.loc[cl_selected['DistributionChannel'] == 'TA/TO']
    direct = cl_selected.loc[cl_selected['DistributionChannel'] == 'Direct']
    corporate = cl_selected.loc[cl_selected['DistributionChannel'] == 'Corporate']
    gds = cl_selected.loc[cl_selected['DistributionChannel'] == 'GDS']

    tot_dchannel_perc = cl_selected['DistributionChannel'].count()
    TATO_perc = TATO['DistributionChannel'].count()
    direct_perc = direct['DistributionChannel'].count()
    corporate_perc = corporate['DistributionChannel'].count()
    gds_perc = gds['DistributionChannel'].count()

    TATO_mean = round(TATO['Upselling'].mean(), ndigits=1)
    direct_mean = round(direct['Upselling'].mean(), ndigits=1)
    corporate_mean = round(corporate['Upselling'].mean(), ndigits=1)
    gds_mean = round(gds['Upselling'].mean(), ndigits=1)

    TATORev_mean = round(TATO['Revenues by day'].mean(), ndigits=1)
    directRev_mean = round(direct['Revenues by day'].mean(), ndigits=1)
    corporateRev_mean = round(corporate['Revenues by day'].mean(), ndigits=1)
    gdsRev_mean = round(gds['Revenues by day'].mean(), ndigits=1)

    TATO_rating = round(TATO['Rating'].mean(), ndigits=1)
    direct_rating = round(direct['Rating'].mean(), ndigits=1)
    corporate_rating = round(corporate['Rating'].mean(), ndigits=1)
    gds_rating = round(gds['Rating'].mean(), ndigits=1)

    TATO_nights = round(TATO['Nights'].mean(), ndigits=1)
    direct_nights = round(direct['Nights'].mean(), ndigits=1)
    corporate_nights = round(corporate['Nights'].mean(), ndigits=1)
    gds_nights = round(gds['Nights'].mean(), ndigits=1)

    TATO_wd = round(TATO['StaysInWeekNights'].mean(), ndigits=1)
    direct_wd = round(direct['StaysInWeekNights'].mean(), ndigits=1)
    corporate_wd = round(corporate['StaysInWeekNights'].mean(), ndigits=1)
    gds_wd = round(gds['StaysInWeekNights'].mean(), ndigits=1)

    TATO_we = round(TATO['StaysInWeekendNights'].mean(), ndigits=1)
    direct_we = round(direct['StaysInWeekendNights'].mean(), ndigits=1)
    corporate_we = round(corporate['StaysInWeekendNights'].mean(), ndigits=1)
    gds_we = round(gds['StaysInWeekendNights'].mean(), ndigits=1)

    try:
        TATO_nation_rev = TATO.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        TATO_nation_rev = 'null'

    try:
        direct_nation_rev = direct.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        direct_nation_rev = 'null'

    try:
        corporate_nation_rev = \
            corporate.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        corporate_nation_rev = 'null'

    try:
        gds_nation_rev = gds.groupby('Country')['Revenues by day'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        gds_nation_rev = 'null'

    try:
        TATO_nation_rating = TATO.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        TATO_nation_rating = 'null'

    try:
        direct_nation_rating = direct.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        direct_nation_rating = 'null'

    try:
        corporate_nation_rating = corporate.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        corporate_nation_rating = 'null'

    try:
        gds_nation_rating = gds.groupby('Country')['Rating'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        gds_nation_rating = 'null'

    try:
        TATO_nation_upselling = TATO.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        TATO_nation_upselling = 'null'

    try:
        direct_nation_upselling = direct.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        direct_nation_upselling = 'null'

    try:
        corporate_nation_upselling = \
            corporate.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        corporate_nation_upselling = 'null'

    try:
        gds_nation_upselling = gds.groupby('Country')['Upselling'].mean().sort_values(ascending=False).index[0]
    except IndexError:
        gds_nation_upselling = 'null'

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
                    values=['Segments by Distribution Channel'],
                    line=dict(color='#fafafa'),
                    align=['center'],
                    font=dict(color=['black'] * 5, size=16),
                    fill=dict(color='#fafafa')
                    ))

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

    figure_dc = {'data': [table_dchannel1,
                          data_donuts_dc1,
                          data_donuts_dc2,
                          data_donuts_dc3,
                          data_donuts_dc4,
                          table_dc_title, ],
                 'layout':
                     go.Layout(showlegend=False,
                               height=410,
                               margin=dict(l=0.15, r=0, t=0, b=0),
                               plot_bgcolor="#fafafa",
                               paper_bgcolor="#fafafa",
                               ),
                 }
    return figure_dc


# DISTRIBUTION CHANNEL callback
@app.callback(dash.dependencies.Output('pie_dc', 'figure'),
              [dash.dependencies.Input('radioItems_clusters', 'value'),
               dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_pie_dc(radioItems_clusters_value, start_date, end_date):
    cl_selected_r = hotel_data.loc[hotel_data['IDlabelsClusters'] == radioItems_clusters_value]
    cl_selected = cl_selected_r[
        (cl_selected_r['TimeArrival'] >= start_date) & (cl_selected_r['TimeArrival'] <= end_date)]

    TATO = cl_selected.loc[cl_selected['DistributionChannel'] == 'TA/TO']
    direct = cl_selected.loc[cl_selected['DistributionChannel'] == 'Direct']
    corporate = cl_selected.loc[cl_selected['DistributionChannel'] == 'Corporate']
    gds = cl_selected.loc[cl_selected['DistributionChannel'] == 'GDS']

    # Type of upselling
    values_upselling_TATO = cl_selected[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        hotel_data['DistributionChannel'] == 'TA/TO'].sum().copy()
    values_upselling_TATO = values_upselling_TATO.tolist()

    values_upselling_direct = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        hotel_data['DistributionChannel'] == 'Direct'].sum().copy()
    values_upselling_direct = values_upselling_direct.tolist()

    values_upselling_corporate = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        hotel_data['DistributionChannel'] == 'Corporate'].sum().copy()
    values_upselling_corporate = values_upselling_corporate.tolist()

    values_upselling_gds = hotel_data[['Bar', 'Restaurant', 'Other', 'Breakfast', 'Revenues by day']].loc[
        hotel_data['DistributionChannel'] == 'GDS'].sum().copy()
    values_upselling_gds = values_upselling_gds.tolist()

    values_upselling_dc = [values_upselling_TATO, values_upselling_direct, values_upselling_corporate,
                           values_upselling_gds]

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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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
        'marker': {'colors': ['#ffcb94', '#6cff99', '#c5bef1', '#a9efe8', '#dc3d4f']}
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

    ups_TATO = [ups_TATO_restaurant_rev_mean, ups_TATO_bar_rev_mean, ups_TATO_breakfast_rev_mean,
                ups_TATO_other_rev_mean]
    ups_direct = [ups_direct_restaurant_rev_mean, ups_direct_bar_rev_mean, ups_direct_breakfast_rev_mean,
                  ups_direct_other_rev_mean]
    ups_corporate = [ups_corporate_restaurant_rev_mean, ups_corporate_bar_rev_mean, ups_corporate_breakfast_rev_mean,
                     ups_corporate_other_rev_mean]
    ups_gds = [ups_gds_restaurant_rev_mean, ups_gds_bar_rev_mean, ups_gds_breakfast_rev_mean, ups_gds_other_rev_mean]

    ups_tot = hotel_data['Upselling'].sum()

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
    ups_direct_perc = [ups_direct_restaurant_perc, ups_direct_bar_perc, ups_direct_breakfast_perc,
                       ups_direct_other_perc]
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
    table_upselling_dc_gds = pd.DataFrame(index=index_table_ups,
                                          data={'Avg Revenues': ups_gds, 'Absolute %': ups_gds_perc},
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
              # pad = {'r': 10, 't': 10},
              x=0.5,
              y=.95,
              )
         ])

    figure_dc = {'data': values_upselling_pie_dc + traces_ups_dc,
                 'layout': dict(height=410, updatemenus=updatemenus_dc, showlegend=True,
                                legend=dict(orientation="h", y=0.25),
                                plot_bgcolor="#fafafa",
                                paper_bgcolor="#fafafa",
                                margin=dict(l=0,
                                            r=0,
                                            t=0,
                                            b=0))}
    return figure_dc


@app.callback(Output('map-world', 'figure'),
              [dash.dependencies.Input('radioItems_clusters', 'value'),
               dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date'),
               dash.dependencies.Input('dropdown_parameters', 'value')])
def show_map(radioItems_clusters_value, start_date, end_date, dropdown_parameters_value, ):
    cl_selected_r = hotel_data.loc[hotel_data['IDlabelsClusters'] == radioItems_clusters_value]
    cl_selected = cl_selected_r[
        (cl_selected_r['TimeArrival'] >= start_date) & (cl_selected_r['TimeArrival'] <= end_date)]
    values_choro_r = pd.DataFrame(
        cl_selected.groupby('Country')[['TOT_revenues', 'Rating', 'Upselling']].mean()).reset_index().copy()
    values_choro_selected = pd.DataFrame(values_choro_r[['Country', dropdown_parameters_value]])

    fig = {'data':
               [go.Choropleth(locations=values_choro_selected['Country'],
                              z=values_choro_selected[dropdown_parameters_value],
                              locationmode="country names",
                              showscale=False,
                              colorscale=[
                                  [0, "rgb(5, 10, 172)"],
                                  [0.35, "rgb(40, 60, 190)"],
                                  [0.5, "rgb(70, 100, 245)"],
                                  [0.6, "rgb(90, 120, 245)"],
                                  [0.7, "rgb(106, 137, 247)"],
                                  [1, "rgb(220, 220, 220)"]
                              ],
                              autocolorscale=True,
                              reversescale=False,
                              marker=dict(
                                  line=dict(
                                      color='rgb(180,180,180)',
                                      width=0.5
                                  )),
                              colorbar=go.choropleth.ColorBar(
                                  thickness=18,
                                  tickprefix='DKK',
                                  title='Aggregated Revenues'),
                              )],

           'layout': layout_map}
    return fig


if __name__ == '__main__':
    app.run_server(debug=debug)
