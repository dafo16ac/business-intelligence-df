import plotly.graph_objs as go
from settings import hotel_data, pd

""" CHOROPLETH VALUES """
values_choro = pd.DataFrame(
    hotel_data.groupby('Country')[['ADR Adjusted', 'Customer Satisfaction Rating']].mean()).reset_index().copy()

values_choro_count = pd.DataFrame(
    hotel_data.groupby('Country')[['ADR Adjusted']].count()).reset_index().copy()

values_choro_sum = pd.DataFrame(
    hotel_data.groupby('Country')[['ADR Adjusted']].sum()).reset_index().copy()

values_choro['N° Clients (count)'] = values_choro_count['ADR Adjusted']
values_choro['ADR Adjusted (total sum)'] = values_choro_sum['ADR Adjusted']
values_choro.rename(columns={'ADR Adjusted': 'ADR Adjusted (mean)', 'Customer Satisfaction Rating': 'Customer Satisfaction Rating (mean)'}, inplace=True)


data_map_revenues = [go.Choropleth(
    locations=values_choro['Country'],
    z=values_choro['ADR Adjusted (mean)'],
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
)]

data_map_rating = [go.Choropleth(
    locations=values_choro['Country'],
    z=values_choro['Customer Satisfaction Rating (mean)'],
    # text = final_hotel['Country'],
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
)]

data_map_upselling = [go.Choropleth(
    locations=values_choro['Country'],
    z=values_choro['ADR Adjusted (total sum)'],
    # text = final_hotel['Country'],
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
        title='Aggregated ADR'),
)]


data_map_count = [go.Choropleth(
    locations=values_choro['Country'],
    z=values_choro['N° Clients (count)'],
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
        #tickprefix='DKK',
        title='N° Clients'),
)]



data_map = [data_map_revenues, data_map_rating, data_map_upselling, data_map_count]

layout_map = go.Layout(
    title=go.layout.Title(text='Guests Nationality by selected Metric'),
    legend=dict(orientation="h"),
    geo=go.layout.Geo(
        showframe=False,
        showcoastlines=False,
        showcountries=True,
        countrywidth=0.2,
        domain=dict(x=[0, 1],
                    y=[0, .94]),
        projection=go.layout.geo.Projection(
            type='equirectangular'
        )
    ),
    # height=400,
    # updatemenus=updatemenus_choro,
    # COLOR THEME
    plot_bgcolor="#fafafa",
    paper_bgcolor="#fafafa",
)
