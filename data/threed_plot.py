import plotly.graph_objs as go
import plotly.express as px
from settings import hotel_data


""" 3D PLOT CLUSTER """
cl0 = hotel_data.loc[hotel_data['Cluster'] == 0].copy()
cl1 = hotel_data.loc[hotel_data['Cluster'] == 1].copy()
cl2 = hotel_data.loc[hotel_data['Cluster'] == 2].copy()
cl3 = hotel_data.loc[hotel_data['Cluster'] == 3].copy()
cl4 = hotel_data.loc[hotel_data['Cluster'] == 4].copy()
cl5 = hotel_data.loc[hotel_data['Cluster'] == 5].copy()
cl6 = hotel_data.loc[hotel_data['Cluster'] == 6].copy()

cl_label_0 = '0. ' + cl0['Cluster Profile'].unique()[0]
cl_label_1 = '1. ' + cl1['Cluster Profile'].unique()[0]
cl_label_2 = '2. ' + cl2['Cluster Profile'].unique()[0]
cl_label_3 = '3. ' + cl3['Cluster Profile'].unique()[0]
cl_label_4 = '4. ' + cl4['Cluster Profile'].unique()[0]
cl_label_5 = '5. ' + cl5['Cluster Profile'].unique()[0]
cl_label_6 = '6. ' + cl6['Cluster Profile'].unique()[0]


cluster0 = go.Scatter3d(
    x=cl6['Customer Satisfaction Rating'],
    y=cl6['ADR'],
    z=cl6['Additional Expenditures by day'],
    mode='markers',
    showlegend=True,
    name=cl_label_0,
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

cluster1 = go.Scatter3d(
    x=cl0['Customer Satisfaction Rating'],
    y=cl0['ADR'],
    z=cl0['Additional Expenditures by day'],
    mode='markers',
    showlegend=True,
    name=cl_label_1,
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
    x=cl1['Customer Satisfaction Rating'],
    y=cl1['ADR'],
    z=cl1['Additional Expenditures by day'],
    mode='markers',
    showlegend=True,
    name=cl_label_2,
    marker=dict(
        size=3.5,
        color='#f7ef99',
        # colorscale='YlGnBu',
        line=dict(
            color='black',
            width=0.08
        ),
        # opacity=0.96
    )
)

cluster3 = go.Scatter3d(
    x=cl2['Customer Satisfaction Rating'],
    y=cl2['ADR'],
    z=cl2['Additional Expenditures by day'],
    mode='markers',
    showlegend=True,
    name=cl_label_3,
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
    x=cl3['Customer Satisfaction Rating'],
    y=cl3['ADR'],
    z=cl3['Additional Expenditures by day'],
    mode='markers',
    showlegend=True,
    name=cl_label_4,
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
    x=cl4['Customer Satisfaction Rating'],
    y=cl4['ADR'],
    z=cl4['Additional Expenditures by day'],
    mode='markers',
    showlegend=True,
    name=cl_label_5,
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
    x=cl5['Customer Satisfaction Rating'],
    y=cl5['ADR'],
    z=cl5['Additional Expenditures by day'],
    mode='markers',
    showlegend=True,
    name=cl_label_6,
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

traces_3d = [cluster0, cluster1, cluster2, cluster3, cluster4, cluster5, cluster6]
