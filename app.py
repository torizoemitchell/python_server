
from flask import Flask
import temperature_graph

#create application instance
app = Flask(__name__ )

@app.route('/')
def Index():
    return temperature_graph.make_graph()


# app.run()
