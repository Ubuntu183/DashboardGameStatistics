import dash_bootstrap_components as dbc

from dash import Dash, Input, Output, dcc, html
from pages import overall, platforms, genres, info

external_stylesheets = [dbc.themes.UNITED, '/assets/custom.css']
app = Dash(__name__, external_stylesheets=external_stylesheets,  use_pages=True)
app.config.suppress_callback_exceptions = True

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20%",
    "padding": "2rem 1rem",
    "background-color": "#e9ecef",
    "text-align": "center",
}

CONTENT_STYLE = {
    "margin-left": "20%",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

NAVLINK_STYLE = {
    "padding": "0.9rem 0.5rem",
    "font-size": "1.1rem"
}

sidebar = html.Div(
    [
        html.H2("Статистика выпущенных видеоигр", className="display-6"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Общая статистика", href="/", active="exact", style=NAVLINK_STYLE),
                dbc.NavLink("Платформы", href="/page-1", active="exact", style=NAVLINK_STYLE),
                dbc.NavLink("Жанры", href="/page-2", active="exact", style=NAVLINK_STYLE),
                dbc.NavLink("О проекте", href="/page-3", active="exact", style=NAVLINK_STYLE),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])

def render_page_content(pathname):
    if pathname == "/":
        return overall.layout
    elif pathname == "/page-1":
        return platforms.layout
    elif pathname == "/page-2":
        return genres.layout
    elif pathname == "/page-3":
        return info.layout
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == '__main__':
        app.run_server(debug=True)