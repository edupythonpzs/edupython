#pip install matplotlib
#pip install bottle
#pip install pyyaml
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import math
import json
from shutil import copyfile

from bottle import route, run, template, static_file, request, post, get, redirect


import yaml



config = yaml.safe_load(open("config.yml"))

print config

def dominanta(A):
    x = None
    count = 0
    for i in A:
        if count == 0:
            x = i
            count += 1
        elif i == x:
            count += 1
        else:
            count -= 1
    return x


users_data = []
x_list = []
y_list = []

fig=plt.figure(1)
fig2=plt.figure(1)

@route('/')
def index():
    redirect("/index.html")

@route('/genPLT/<i1>/<i2>/')
def gen_plt(i1, i2):
    users_data.append({"z1": i1, "z2": i2});
    print users_data
    z1 = i1
    z2 = i2
    print "wyliczone z1", z1, "z2", z2
    exec(open("plt.py").read())
    return json.dumps(users_data)

@route('/getHISTORY')
def get_history():
    return json.dumps(users_data)

@route('/resetPlt')
def reset_plt():
    if(len(users_data)!=0):
        del users_data[:]
    if(len(x_list)!=0):
        del x_list[:]
    if(len(y_list)!=0):
        del y_list[:]
    plt.clf()
    copyfile('plt-clear.png', 'plt.png')
    return "ok"

@route('/<filename:re:.*\.html>')
def send_html(filename):
    return static_file(filename, root='', mimetype='text/html')

@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='images', mimetype='image/png')

@route('/plt.png')
def send_image_plt():
    return static_file("plt.png", root='', mimetype='image/png')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


run(host='127.0.0.1', port=config['port'])

ax2=fig2.add_subplot(111)
ax2.xaxis.set_label_coords(0.9,0.1)
ax2.yaxis.set_label_coords(0.,1.02)
plt2.xlabel(r"$x\,[m]$", fontsize=12)
plt2.ylabel(r"$ y\,[m]$", fontsize=12, rotation=0) 
plt2.ylim(-0.04,0.04)
plt2.savefig('plt-clear.png', dpi=400)