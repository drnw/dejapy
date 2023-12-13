#!python

import panel as pn
from apps.deja import demo as deja_demo

apps = {
    "demo": deja_demo,
}

pn.serve(
    apps,
    port=5130,
    websocket_origin=["dejapy.tilix.ai", "localhost:5130"],
    autoreload=True,
    dev=True,
    show=True,
)
