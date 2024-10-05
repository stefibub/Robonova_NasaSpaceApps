from dash import Dash, html, Input, Output, no_update, State
from dash_extensions import BeforeAfter
import dash_bootstrap_components as dbc
from flask import send_from_directory

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP])
app.title = "Webb-before-after"


@app.server.route('/assets/<path:filename>')
def serve_image(filename):
    return send_from_directory('assets', filename)


# Images
left_1 = "assets/left_1.png"
left_2 = "assets/deep_field.jpg"
left_3 = "assets/left_3.png"
left_4 = "assets/left_4.png"
left_5 = "assets/left_5.png"
right_1 = "assets/right_1.png"
right_2 = "assets/webb_deep_field.jpg"
right_3 = "assets/right_3.png"
right_4 = "assets/right_4.png"
right_5 = "assets/right_5.png"
audio_src_1 = "assets/1.wav"
audio_src_2 = "assets/2.wav"
audio_src_3 = "assets/3.wav"
audio_src_4 = "assets/4.wav"
audio_src_5 = "assets/5.wav"
audio_src_6 = "assets/6.wav"
audio_src_7 = "assets/7.wav"
audio_src_8 = "assets/8.wav"
audio_src_9 = "assets/9.wav"

# Header
header = html.Div(
    [
        html.H2(
            [
                html.Span("From Hubble to Webb:"),  # First part of the title
                html.Br(),  # Line break
                html.Span("A New Era of Cosmic Discovery"),  # Second part of the title
            ],
            className="display-3",
            style={
                "fontSize": "47px",
                "color": "#ffcc00",
                "textAlign": "center",
                "fontWeight": "bold",
                "textShadow": "0 0 20px #ffcc00, 0 0 30px #ff9900, 0 0 40px #ff6600",
                "letterSpacing": "2px",
                "marginTop": "40px",
                "marginBottom": "30px",
                "fontFamily": "'Orbitron', sans-serif",  # Space/futuristic font
            }
        ),
        html.Div(
            "Explore the evolution of cosmic discovery — compare stunning images from Hubble’s pioneering eye to Webb’s revolutionary gaze.",
            style={
                "fontSize": "20px",
                "color": "#ffffff",
                "textAlign": "center",  # if not insert left
                "marginTop": "20px",
                "marginBottom": "20px",
                "lineHeight": "1.5",  # Adjust line height for better readability
            }
        ),
        html.Div(
            [
                dbc.Button("James VS Webb", color="primary", className="ms-2 text-white-50", id="button-1"),
                dbc.Button("Discover More", color="secondary", className="ms-2 text-white-50", id="button-2"),
            ],
            className="d-flex justify-content-center",  # Bootstrap class to center
        ),

    ],

)


# Function to create before/after slider
def make_before_after(after, before, audio_src):
    return html.Div(
        [
            html.Div(
                [
                    html.P(
                        "Ever wondered what the universe sounds like? Click to hear the hidden music encoded in these stunning visuals!",
                        style={
                            "color": "light",
                            "fontSize": "14px",
                            "maxWidth": "1000px",
                            "marginTop": "5px",
                        }
                    ),
                    html.Audio(id={"type": "audio", "index": audio_src}, src=audio_src, controls=True),
                ],
                style={"textAlign": "center", "marginBottom": "20px"},  # Center-align and add margin
            ),
            BeforeAfter(before={"src": before}, after={"src": after}),
        ],
        style={"marginTop": 50},

    )


# Function to create image display in 2x2 matrix with flip effect
def make_image_matrix(images):
    return html.Div(
        style={
            'display': 'grid',  # Use grid layout
            'gridTemplateColumns': 'repeat(2, 1fr)',  # Create two columns
            'gap': '10px',  # Gap between items
            'maxWidth': '1050px',  # Set a max width for the matrix
            'margin': '0 auto',  # Center the matrix
        },
        children=[
            html.Div(
                className='card',
                style={
                    'height': '512px',
                    "width": '512px',  # Set a fixed height for the cards
                },
                children=[
                    html.Div(
                        className='front',
                        children=[
                            html.Img(src=img['src'], style={'width': '100%', 'height': '100%', 'objectFit': 'cover'})]
                    ),
                    html.Div(
    className='back',
    style={
        'backgroundColor': '#333',  # Background color of the back
        'color': 'white',  # Text color
        'display': 'flex',  # Use flexbox to center the content
        'flexDirection': 'column',  # Arrange items in a column
        'alignItems': 'center',  # Center horizontally
        'justifyContent': 'center',  # Center vertically
        'height': '100%',  # Take full height
        'fontSize': '20px',  # Font size
        'textAlign': 'center',  # Center text alignment
        'padding': '10px',  # Padding for text
    },
    children=[
                        html.Div(
                            [
                                html.Audio(
                                    id={"type": "audio", "index": img['audio_src']},
                                    src=img['audio_src'],
                                    controls=True
                                ),
                                html.Div(
                                    img['text'],
                                    style={
                                        'text-align': 'center',
                                        'margin-top': '10px',
                                        'word-wrap': 'break-word',  # Перенос текста
                                        'width': '100%',  # Ширина контейнера для текста
                                        'max-width': '300px'  # Максимальная ширина контейнера
                                    }
                                )
                            ],
                            style={
                                'display': 'flex',
                                'flex-direction': 'column',
                                'align-items': 'center'
                            }
                        )
                    ]
)
                ],
            )
            for img in images
        ]
    )


buttons = html.Div(
    [
        dbc.Button(
            [html.I(className="bi bi-book me-2"), "webbtelescope.org"],
            color="light",
            className="text-white-50",
            href="https://webbtelescope.org/news/first-images/gallery",
        ),
        dbc.Button(
            [html.I(className="bi bi-globe me-2"), "Our HackAthlone Team"],
            color="light",
            className="ms-2 text-white-50",
            href="https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/robonova/",
        ),
        html.Div(
            [
                # "Reference: ",
                html.A(
                    "Credits",
                    href="https://github.com/AnnMarieW/webb-compare",
                    target="_blank",
                    style={"color": "light", "textDecoration": "underline"},
                ),
            ],
            style={
                "textAlign": "right",  # Align the text to the right
                "marginTop": "8px",  # Add space above the text
                "color": "light",  # Set text color
            },
        ),
    ],
    style={
        "textAlign": "right",  # Center the buttons at the bottom
        "marginTop": "40px",  # Add space above the buttons
        "paddingBottom": "20px",  # Add padding below for spacing at the bottom
    }
)
# Initial tabs
tabs = dbc.Tabs(
    id="tabs",
    children=[
        dbc.Tab(make_before_after(right_1, left_1, audio_src_1), label="Soul Nebula"),
        dbc.Tab(make_before_after(right_2, left_2, audio_src_2), label="Galaxy Cluster SMACS 0723"),
        dbc.Tab(make_before_after(right_3, left_3, audio_src_3), label="Eagle Nebula"),
        dbc.Tab(make_before_after(right_4, left_4, audio_src_4), label="Carina Nebula"),
        dbc.Tab(make_before_after(right_5, left_5, audio_src_5), label="Southern Ring Nebula"),
    ],
    className="mt-5",
)

# Layout with header and tabs
app.layout = dbc.Container([header, tabs, buttons], style={"maxWidth": 1000})


# Callback to handle button click
@app.callback(
    [Output("tabs", "children"),
     Output("button-1", "n_clicks"),
     Output("button-2", "n_clicks"),
     Output("button-1", "color"),
     Output("button-2", "color")],
    [Input("button-1", "n_clicks"),
     Input("button-2", "n_clicks")],
    [State("tabs", "children")]
)
def update_tab_content(n_clicks_1, n_clicks_2, current_tabs):
    # Default initial state (Button 1)
    default_tabs = [
        dbc.Tab(make_before_after(right_1, left_1, audio_src_1), label="Galaxy Cluster SMACS 0723"),
        dbc.Tab(make_before_after(right_2, left_2, audio_src_2), label="Cartwheel Galaxy"),
        dbc.Tab(make_before_after(right_3, left_3, audio_src_3), label="Stephans Quintet"),
        dbc.Tab(make_before_after(right_4, left_4, audio_src_4), label="Carina Nebula"),
        dbc.Tab(make_before_after(right_5, left_5, audio_src_5), label="Southern Ring Nebula"),
    ]

    # Define texts for images
    images = [
        {'src': '/assets/image_1.png', 'text': r"Wolf-Rayet star WR 124 in near- and mid-infrared light, revealing diffraction spikes and a surrounding nebula of gas and dust. Spanning 10 light-years, the nebula’s asymmetric ejections form clumps resembling tadpoles. Background stars and galaxies add depth, while filters assign red, green, and blue to different infrared wavelengths, balancing the star’s brightness with the fainter material.", 'audio_src': audio_src_6},
        {'src': '/assets/image_2.png', 'text': r"Ring Nebula (M57) in remarkable detail, revealing intricate structures and dense globules rich in molecular hydrogen. The inner region contains very hot gas, while the main shell has a thin ring of carbon-based molecules (PAHs). Concentric arcs beyond the main ring are likely caused by the central star’s interaction with a low-mass companion. Studying the nebula helps astronomers learn more about the star that formed it.", 'audio_src': audio_src_7},
        {'src': '/assets/image3_new.png', 'text': r"Supernova remnant Cassiopeia A (Cas A) in stunning detail. Bright orange and pink clumps in the inner shell contain sulfur, oxygen, argon, and neon, showing how the star shattered upon exploding. The outer shell resembles smoke, where material from the explosion hits surrounding gas, emitting synchrotron radiation. Light echoes, especially in the bottom right, show light from the explosion warming distant dust.", 'audio_src': audio_src_8},
        {'src': '/assets/webb.png', 'text': r"The James Webb Space Telescope’s near-infrared image of Arp 142 reveals faint dust lanes and a bright core in the Penguin galaxy. An upside-down “U” shape of stars and gas connects the merging galaxies, while the Egg galaxy shines intensely with diffraction spikes. The background teems with distant galaxies, visible thanks to Webb's enhanced sensitivity to infrared light.",'audio_src': audio_src_9}
    ]

    modified_tabs = make_image_matrix(images)

    # Handle button clicks and switch between default and modified tabs
    if n_clicks_2 and n_clicks_2 > 0:
        return modified_tabs, 0, 0, "secondary", "primary"  # Update button colors
    elif n_clicks_1 and n_clicks_1 > 0:
        return default_tabs, 0, 0, "primary", "secondary"  # Update button colors

    return current_tabs, 0, 0, "primary", "secondary"  # Default colors


if __name__ == "__main__":
    app.run_server(debug=True)
