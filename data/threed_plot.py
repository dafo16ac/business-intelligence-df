import plotly.graph_objs as go

from settings import hotel_data


""" 3D PLOT CLUSTER """
cl0 = hotel_data.loc[hotel_data['IDlabelsClusters'] == 3].copy()  ### nverted number so clusters in descending order
cl1 = hotel_data.loc[hotel_data['IDlabelsClusters'] == 1].copy()
cl2 = hotel_data.loc[hotel_data['IDlabelsClusters'] == 2].copy()
cl3 = hotel_data.loc[hotel_data['IDlabelsClusters'] == 0].copy()
cl4 = hotel_data.loc[hotel_data['IDlabelsClusters'] == 4].copy()
cl5 = hotel_data.loc[hotel_data['IDlabelsClusters'] == 5].copy()

cluster1 = go.Scatter3d(
    x=cl0['Rating'],
    y=cl0['Revenues by day'],
    z=cl0['Upselling'],
    mode='markers',
    showlegend=True,
    name='High TotRev & Rating',  ###
    marker=dict(
        size=3.5,
        color='#a6cee3',
        # colorscale='YlGnBu',
        line=dict(
            color='black',
            width=0.08
        ),
        # opacity=0.96
    )
)

cluster2 = go.Scatter3d(
    x=cl1['Rating'],
    y=cl1['Revenues by day'],
    z=cl1['Upselling'],
    mode='markers',
    showlegend=True,
    name='High Rating',
    marker=dict(
        size=3.5,
        color='#1f78b4',
        # colorscale='YlGnBu',
        line=dict(
            color='black',
            width=0.08
        ),
        # opacity=0.96
    )
)

cluster3 = go.Scatter3d(
    x=cl2['Rating'],
    y=cl2['Revenues by day'],
    z=cl2['Upselling'],
    mode='markers',
    showlegend=True,
    name='High TotRev',
    marker=dict(
        size=3.5,
        color='#b2df8a',
        # colorscale='YlGnBu',
        line=dict(
            color='black',
            width=0.08
        ),
        # opacity=0.96
    )
)

cluster4 = go.Scatter3d(
    x=cl3['Rating'],
    y=cl3['Revenues by day'],
    z=cl3['Upselling'],
    mode='markers',
    showlegend=True,
    name='Medium TotRev & Rating',  ###
    marker=dict(
        size=3.5,
        color='#fb9a99',
        # colorscale='YlGnBu',
        line=dict(
            color='black',
            width=0.08
        ),
        # opacity=0.96
    )
)

cluster5 = go.Scatter3d(
    x=cl4['Rating'],
    y=cl4['Revenues by day'],
    z=cl4['Upselling'],
    mode='markers',
    showlegend=True,
    name='Medium-low TotRev & Rating',
    marker=dict(
        size=3.5,
        color='#e31a1c',
        # colorscale='YlGnBu',
        line=dict(
            color='black',
            width=0.08
        ),
        # opacity=0.96
    )
)

cluster6 = go.Scatter3d(
    x=cl5['Rating'],
    y=cl5['Revenues by day'],
    z=cl5['Upselling'],
    mode='markers',
    showlegend=True,
    name='Low TotRev',
    # hoverinfo='x + y + text',
    marker=dict(
        size=3.5,
        color='#33a02c',
        # colorscale='YlGnBu',
        line=dict(
            color='black',
            width=0.08
        ),
        # opacity=0.96
    )
)

traces_3d = [cluster1, cluster2, cluster3, cluster4, cluster5, cluster6]
