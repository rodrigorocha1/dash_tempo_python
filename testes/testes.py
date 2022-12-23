from dash import Dash, html
import dash_bootstrap_components as dbc
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])
webb_deep_field = "https://user-images.githubusercontent.com/72614349/192781103-2ca62422-2204-41ab-9480-a730fc4e28d7.png"
card = dbc.Card(
    [
        dbc.CardImg(src=webb_deep_field),
        dbc.CardImgOverlay([
            html.H2("James Webb Space Telescope"),
            html.H3("First Images"),
            html.P(
                "Learn how to make an app to compare before and after images of Hubble vs Webb with ~40 lines of Python",
                style={"marginTop":175},
                className="small",
            ),
            dbc.Button("See the App",
                       href="https://jwt.pythonanywhere.com/"),
            dbc.Button(
                [html.I(className="bi bi-github me-2"),
                 "source code"],
                className="ms-2 text-white",
                href="https://github.com/AnnMarieW/webb-compare",
            )
        ])
    ],
    style={"maxWidth": 500},
    className="my-4 text-center text-white"
)
app.layout=dbc.Container(card)
if __name__ == "__main__":
    app.run_server(debug=True)