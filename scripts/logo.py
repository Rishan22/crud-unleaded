import math, random

def gen(name):
    random.seed(hash(name))
    phi = (1 + 5 ** 0.5) / 2
    shapes = ["circle","triangle","rhombus"]
    shape = random.choice(shapes)
    pts = []
    for i in range(10):
        t = i * 0.5
        r = phi ** (t / (2*math.pi))
        x = r * math.cos(t)
        y = r * math.sin(t)
        pts.append((x,y))
    svg = ["<svg viewBox='0 0 100 100'>"]
    for i,(x,y) in enumerate(pts):
        cx = 50 + x*20
        cy = 50 + y*20
        if shape=="circle":
            svg.append(f"<circle cx='{cx}' cy='{cy}' r='{3+i%4}'/>")
        elif shape=="triangle":
            svg.append(f"<polygon points='{cx},{cy} {cx+4},{cy+6} {cx-4},{cy+6}'/>")
        else:
            svg.append(f"<rect x='{cx}' y='{cy}' width='5' height='5' transform='rotate(45 {cx} {cy})'/>")
    svg.append("</svg>")
    return "".join(svg)
