import pyglet, time, argparse
from random import randint
import render, dot, configuration, renderqueue, scene

parse = argparse.ArgumentParser()
parse.add_argument("configfile")
args = parse.parse_args()

config = configuration.read_config(configuration.open_config(args.configfile))

conf = pyglet.gl.Config(sample_buffers=1, samples=4)
window = pyglet.window.Window(width=config['window']['width'], height=config['window']['height'], config=conf)
pyglet.gl.glClearColor(*config['window']['bgcolor'], 1)

width, height = 1250, 650
window = pyglet.window.Window(width=width, height=height)


rqueue = renderqueue.RenderQueue(window)
scene.display_scene(window, config, "fast", rqueue, True)
# demo fast, medium, and slow

def update(dt):
    pass

pyglet.clock.schedule_interval(update, 1/240)

@window.event
def on_draw():
    window.clear()
    for i in range(10):
        x = randint(0,width)
        y = randint(0,height)
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (x, y)),
                ('c3B', (255, 255, 255))
            )
    rqueue.render()

pyglet.app.run()