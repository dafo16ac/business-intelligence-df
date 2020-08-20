import plotly.graph_objs as go


class Table:
    def __init__(self, dataset):
        self.dataset = dataset


class RightTable(Table):
    def returning_table(self):
        table = go.Table(
            domain=dict(x=[0.65, 1],
                        y=[0.35, 0.80]),
            header=dict(height=20,
                        values=[[''], ['<b>Daily mean Expenditure</b>'], ['<b>% over all Clusters<b>']],
                        line=dict(color='rgb(50, 50, 50)'),
                        align=['left'],
                        font=dict(color=['white'] * 5, size=8),
                        fill=dict(color='black')),
            cells=dict(
                values=[self.dataset[k].tolist() for k in ['index', 'Avg Revenues', 'Absolute %']],
                line=dict(color='#506784'),
                align=['left'] * 0,
                font=dict(color=['rgb(40, 40, 40)'] * 5, size=10),
                height=20,
                fill=dict(color=['#A9EFE8', '#EAFBF8']))
        )

        return table


class LeftTable(Table):
    def returning_table(self, domain_y, header_values, cell_values):
        table = go.Table(
            domain=dict(x=[0, 1],
                        y=domain_y),
            columnwidth=[2, 1, 1, 1, 1, 1, 1, 1, 1],
            header=dict(height=20,
                        values=header_values,
                        line=dict(color='rgb(50, 50, 50)'),
                        align=['left'],
                        font=dict(color=['white'] * 5, size=10),
                        fill=dict(color='black')),
            cells=dict(values=[self.dataset[k].tolist() for k in cell_values],
                       line=dict(color='#506784'),
                       align=['left'] * 5,
                       font=dict(color=['rgb(40, 40, 40)'] * 5, size=10),
                       height=20,
                       fill=dict(color=['#a9efe8', '#eafbf8']))
        )
        return table
