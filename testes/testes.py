import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import flask
import glob
import os

image_directory = '../assets/'
list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
static_image_route = '/assets/'
print(list_of_images)
app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id='image-dropdown',
        options=[{'label': i, 'value': i} for i in list_of_images],
        value=list_of_images[0]
    ),

    dbc.CardImg(
        id='image',
        top=True,
        style={"opacity": 0.5,
               'height': '39vh'},
    )

])


@app.callback(
    dash.dependencies.Output('image', 'src'),
    [dash.dependencies.Input('image-dropdown', 'value')])
def update_image_src(value):
    print('update_image_src', value)
    return static_image_route + value


# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server
@app.server.route('{}<image_path>.png'.format(static_image_route))
def serve_image(image_path):
    print('serve_image',image_path)
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory, image_name)


if __name__ == '__main__':
    app.run_server(debug=True)
