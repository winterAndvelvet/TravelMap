from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

app = Flask(__name__,static_folder="templates")

def map_base() -> Map:
    c=(
        Map()
        .add("商家A", [list(z) for z in zip(Faker.country, Faker.values())], "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-世界地图"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
            )
            #.render("map_world.html")
        )
    return c

@app.route('/')
def index():
    c = map_base()
    return Markup(c.render_embed())
    #return "hello world"

if __name__ == "__main__":
        app.run()
