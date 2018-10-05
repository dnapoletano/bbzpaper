# import sys
import matplotlib.pyplot as plt
# import numpy as np
import argparse
import feynman as f

plt.style.use('/Users/Nappo/work/local/mplstyles/root_style.mplstyle')

parser = argparse.ArgumentParser(description='draw feynman diagrams')
parser.add_argument('--channels',default=0,type=int,help='choose channels',dest='channels')

args = parser.parse_args()


def find_xy(x, xya, xyb):
    m = (xyb[1] - xya[1])/(xyb[0] - xya[0])
    return m*(x - xya[0]) + xya[1]


def draw_qq_channels(nogbb=1):
    gluon_style = dict(style='linear loopy', xamp=.03, yamp=.03, nloops=4)

    fig = plt.figure(figsize=(10.,10.))
    ax  = fig.add_axes([0,0,1,1], frameon=False)
    d   = f.Diagram(ax)

    # vertices
    if(nogbb):
        in1  = d.vertex(xy=(.1,.7), marker='')
        in2  = d.vertex(xy=(.1,.3), marker='')
        v1   = d.vertex(xy=(.3,.5))
        v2   = d.vertex(xy=(.6,.5))
        v3   = d.vertex(xy=(.7,find_xy(.7,(.6,.5),(.8,.7))))
        out1 = d.vertex(xy=(.8,.7), marker='')
        out2 = d.vertex(xy=(.8,.3), marker='')
        out3 = d.vertex(xy=(.8,.5), marker='')
        # lines

        q1 = d.line(in1, v1)
        q2 = d.line(v1,in2)
        pr = d.line(v1, v2, **gluon_style)
        hi = d.line(v3, out3, style='wiggly', arrow=False, nwiggles=3)
        q3 = d.line(v2, v3,arrow=False)
        q3 = d.line(v3, out1)
        q4 = d.line(out2,v2)
        q1.text('$q$',fontsize=20,t=0.1,y=0.02)
        q2.text(r'$\bar{q}$',fontsize=20,t=0.9,y=0.02)
        q3.text(r'$b$',fontsize=20,t=0.7,y=0.03)
        q4.text(r'$\bar{b}$',fontsize=20,t=0.3,y=-0.02)
        hi.text(r'$Z$',fontsize=20)
        d.plot()
        plt.savefig('qq_nogbb.pdf')

    else:
        in1  = d.vertex(xy=(.1,.7), marker='')
        in2  = d.vertex(xy=(.1,.3), marker='')
        v1   = d.vertex(xy=(.45,.7))
        v2   = d.vertex(xy=(.45,.3))
        v3   = d.vertex(xy=(.7,.7))
        out1 = d.vertex(xy=(.8,.8), marker='')
        out2 = d.vertex(xy=(.8,.3), marker='')
        out3 = d.vertex(xy=(.8,.6), marker='')
        # lines
        q1 = d.line(in1, v1)
        q2 = d.line(v2,in2)
        pr = d.line(v1, v2)
        hi = d.line(out3,v3)
        q3 = d.line(v1, v3, **gluon_style)
        q3 = d.line(v3, out1)
        q4 = d.line(v2,out2, style='wiggly', arrow=False, nwiggles=3)
        q1.text('$q$',fontsize=20,t=0.1,y=0.02)
        q2.text(r'$\bar{q}$',fontsize=20,t=0.9,y=0.03)
        q3.text(r'$b$',fontsize=20,t=0.8,y=-0.02)
        hi.text(r'$\bar{b}$',fontsize=20,t=0.2,y=-0.01)
        q4.text(r'$Z$',fontsize=20,t=0.8,y=0.05)
        d.plot()
        plt.savefig('qq_gbb.pdf')

    plt.show()

    plt.clf()
    return


def draw_gg_channels():
    gluon_style = dict(style='linear loopy', xamp=.03, yamp=.03, nloops=4)

    fig = plt.figure(figsize=(10.,10.))
    ax  = fig.add_axes([0,0,1,1], frameon=False)
    d   = f.Diagram(ax)

    # vertices
    in1  = d.vertex(xy=(.1,.7), marker='')
    in2  = d.vertex(xy=(.1,.3), marker='')
    v1   = d.vertex(xy=(.3,.5))
    v2   = d.vertex(xy=(.6,.5))
    v3   = d.vertex(xy=(.7,find_xy(.7,(.6,.5),(.8,.7))))
    out1 = d.vertex(xy=(.8,.7), marker='')
    out2 = d.vertex(xy=(.8,.3), marker='')
    out3 = d.vertex(xy=(.8,.5), marker='')
        # lines

    q1 = d.line(in1, v1,**gluon_style)
    q2 = d.line(v1,in2,**gluon_style)
    pr = d.line(v1, v2, **gluon_style)
    hi = d.line(v3, out3, style='wiggly', arrow=False, nwiggles=3)
    q3 = d.line(v2, v3,arrow=False)
    q3 = d.line(v3, out1)
    q4 = d.line(out2,v2)
    q3.text(r'$b$',fontsize=20,t=0.7,y=0.03)
    q4.text(r'$\bar{b}$',fontsize=20,t=0.3,y=-0.02)
    hi.text(r'$Z$',fontsize=20)
    d.plot()
    plt.savefig('ggZbb_s.pdf')
    plt.show()
    plt.clf()
# t-channel

    fig = plt.figure(figsize=(10.,10.))
    ax  = fig.add_axes([0,0,1,1], frameon=False)
    d   = f.Diagram(ax)

    in1  = d.vertex(xy=(.1,.7), marker='')
    in2  = d.vertex(xy=(.1,.3), marker='')
    v1   = d.vertex(xy=(.45,.7))
    v2   = d.vertex(xy=(.45,.3))
    v3   = d.vertex(xy=(.45,.5))
    out1 = d.vertex(xy=(.8,.7), marker='')
    out2 = d.vertex(xy=(.8,.3), marker='')
    out3 = d.vertex(xy=(.8,.5), marker='')
        # lines
    q1 = d.line(in1, v1,**gluon_style)
    q2 = d.line(v2,in2,**gluon_style)
    pr = d.line(v2, v3)
    pr = d.line(v3, v1)
    # hi = d.line(out3,v3)
    q3 = d.line(v1,out1)
    q4 = d.line(out2,v2)
    hi = d.line(v3,out3, style='wiggly', arrow=False, nwiggles=3)
    q3.text(r'$b$',fontsize=20,t=0.9,y=-0.04)
    q4.text(r'$\bar{b}$',fontsize=20,t=0.1,y=-0.01)
    hi.text(r'$Z$',fontsize=20,t=0.9,y=0.05)
    d.plot()
    plt.savefig('ggZbb_t.pdf')
    plt.show()
    plt.clf()
    return


def draw_lo_channels():
    fig = plt.figure(figsize=(10.,10.))
    ax  = fig.add_axes([0,0,1,1], frameon=False)
    d   = f.Diagram(ax)

    in1  = d.vertex(xy=(.1,.7), marker='')
    in2  = d.vertex(xy=(.1,.3), marker='')
    v1   = d.vertex(xy=(.4,.5))
    out1 = d.vertex(xy=(.8,.5), marker='')
    q1 = d.line(in1, v1)
    q2 = d.line(v1,in2)
    hi = d.line(v1, out1, style='wiggly', arrow=False, nwiggles=3)
    q1.text('$b$',fontsize=20,t=0.1,y=0.02)
    q2.text(r'$\bar{b}$',fontsize=20,t=0.9,y=-0.02)
    hi.text(r'$Z$',fontsize=20)
    d.plot()

    plt.savefig('bbZ.pdf')

    plt.show()

    plt.clf()
    return


def draw_nlo_channels():
    gluon_style = dict(style='linear loopy', xamp=.03, yamp=.03, nloops=4)
    fig = plt.figure(figsize=(10.,10.))
    ax  = fig.add_axes([0,0,1,1], frameon=False)
    d   = f.Diagram(ax)
    in1  = d.vertex(xy=(.1,.7), marker='')
    in2  = d.vertex(xy=(.1,.3), marker='')
    v1   = d.vertex(xy=(.45,.7))
    v2   = d.vertex(xy=(.45,.3))
    # v3   = d.vertex(xy=(.7,.7))
    out1 = d.vertex(xy=(.8,.7), marker='')
    out2 = d.vertex(xy=(.8,.3), marker='')
    q1 = d.line(in1, v1)
    q2 = d.line(v2,in2)
    pr = d.line(v1, v2)
    q3 = d.line(v1, out1, **gluon_style)
    q4 = d.line(v2,out2, style='wiggly', arrow=False, nwiggles=3)
    q1.text('$b$',fontsize=20,t=0.1,y=0.02)
    q2.text(r'$\bar{b}$',fontsize=20,t=0.9,y=-0.02)
    q4.text(r'$Z$',fontsize=20,t=0.8,y=0.05)
    d.plot()
    plt.savefig('bbZg.pdf')

    plt.show()

    plt.clf()
    return


def draw_bg_channels():
    gluon_style = dict(style='linear loopy', xamp=.03, yamp=.03, nloops=4)
    fig = plt.figure(figsize=(10.,10.))
    ax  = fig.add_axes([0,0,1,1], frameon=False)
    d   = f.Diagram(ax)
    in1  = d.vertex(xy=(.1,.7), marker='')
    in2  = d.vertex(xy=(.1,.3), marker='')
    v1   = d.vertex(xy=(.45,.7))
    v2   = d.vertex(xy=(.45,.3))
    # v3   = d.vertex(xy=(.7,.7))
    out1 = d.vertex(xy=(.8,.7), marker='')
    out2 = d.vertex(xy=(.8,.3), marker='')
    q1 = d.line(v1,out1)
    q2 = d.line(v2,in2)
    pr = d.line(v1, v2)
    q3 = d.line(in1,v1, **gluon_style)
    q4 = d.line(v2,out2, style='wiggly', arrow=False, nwiggles=3)
    q1.text('$b$',fontsize=20,t=0.9,y=0.02)
    q2.text(r'$\bar{b}$',fontsize=20,t=0.9,y=-0.02)
    q4.text(r'$Z$',fontsize=20,t=0.8,y=0.05)
    d.plot()
    plt.savefig('bgZb.pdf')

    plt.show()

    plt.clf()
    return

draw_qq_channels(nogbb=0)
draw_qq_channels(nogbb=1)
draw_gg_channels()
draw_lo_channels()
draw_nlo_channels()
draw_bg_channels()