import dash
import dash_core_components as dcc
import dash_html_components as html

# Crie uma instância do aplicativo Dash
app = dash.Dash(__name__)

# Defina o layout da sua aplicação
app.layout = html.Div(
    children=[
        html.H1("Minha Dashboard"),
        dcc.Graph(
            id="meu-grafico",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Categoria 1"},
                    {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "Categoria 2"},
                ],
                "layout": {"title": "Gráfico de Exemplo"},
            },
        ),
    ]
)

# Inicie o servidor do Dash
if __name__ == "__main__":
    app.run_server(debug=True)
