import turtle
import tkinter as tk
import math

root = tk.Tk()
root.title('数控插补演示界面')
canvas = tk.Canvas(master=root, bd=5, width =850, height =850)
canvas.pack()
turtle = turtle.RawTurtle(canvas)
turtle.hideturtle()


color_1 = (0, 191, 255)
color_2 = (255, 181, 197)
my_step = 20
l1 = tk.Label(root, text="输入坐标 格式[(x0,y0),(x1,y1)...(xn,yn)]")  # 标签
l1.pack(side=tk.LEFT)  # 指定包管理器放置组件
user_text = tk.StringVar()
user_text = tk.Entry(root, textvariable=user_text,width=25)  # 创建文本框
user_text.pack(side=tk.LEFT)
# 设置选择按钮
v1 = tk.IntVar()            # 用来表示按钮是否选中
v2 = tk.IntVar()
c1 = tk.Checkbutton(root, text='直线', variable=v1).pack(side=tk.LEFT)
c2 = tk.Checkbutton(root, text='圆', variable=v2).pack(side=tk.LEFT)


def judge_quadrant(x0, y0, xe, ye):
    x = xe - x0
    y = ye - y0
    if (x > 0) and (y > 0):  # 第一象限
        quadrant = 1
    elif (x < 0) and (y > 0):  # 第二象限
        quadrant = 2
    elif (x < 0) and (y < 0):  # 第三象限
        quadrant = 3
    elif (x > 0) and (y < 0):  # 第四象限
        quadrant = 4
    elif x > 0 and y == 0:
        quadrant = 5  # X轴正方向
    elif x < 0 and y == 0:
        quadrant = 6  # X轴负方向
    elif x == 0 and y > 0:
        quadrant = 7  # Y轴正方向
    elif x == 0 and y < 0:
        quadrant = 8  # Y轴负方向
    return quadrant


def interpolation(quadrant, x0, y0, xe, ye):
    global point
    point = [(x0, y0)]
    x = xe - x0
    y = ye - y0
    fm = 0
    x1 = abs(x)
    y1 = abs(y)
    total = (x1 + y1) / my_step
    cnt = 0
    while cnt < total:
        if quadrant < 5:
            if fm >= 0:
                if quadrant == 1 or quadrant == 4:
                    x0 += my_step
                elif quadrant == 2 or quadrant == 3:
                    x0 -= my_step
                fm = fm - y1
            elif fm < 0:
                if quadrant == 1 or quadrant == 2:
                    y0 += my_step
                elif quadrant == 3 or quadrant == 4:
                    y0 -= my_step
                fm = fm + x1
        else:
            if quadrant == 5:
                x0 += my_step
            elif quadrant == 6:
                x0 -= my_step
            elif quadrant == 7:
                y0 += my_step
            elif quadrant == 8:
                y0 -= my_step
        p = (x0, y0)
        point.append(p)
        cnt += 1


def getuser():  # 该函数用来获得文本框内容
    user = user_text.get()  # 获取文本框内容
    return user


def get_style():
    v_1 = v1.get()
    v_2 = v2.get()
    return v_1, v_2


def get_points(line_path):
    for i in range(0, len(line_path) - 1):
        xo = line_path[i][0] * my_step
        yo = line_path[i][1] * my_step
        print(xo, yo)
        xe = line_path[i + 1][0] * my_step
        ye = line_path[i + 1][1] * my_step
        print(xe, ye)
        quadrant = judge_quadrant(xo, yo, xe, ye)
        print(quadrant)
        interpolation(quadrant, xo, yo, xe, ye)
        return xo, yo, xe, ye


def arc_interpolation(quadrant, sn, xo, yo, x1, y1, total_steps):  # sn 0:逆，1：顺
    fm = 0
    if xo == x1:
        r = abs(y1 - yo)
    else:
        r = abs(x1-xo)
    global point_circle
    point_circle = [(x1, y1)]
    while total_steps != 0:
        if quadrant == 1:
            if sn == 0:  # 1 逆圆
                if math.sqrt((x1-xo)*(x1-xo)+(y1-yo)*(y1-yo)) >= r:
                    x1 -= my_step
                else:
                    y1 += my_step
            else:  # 1 顺圆
                if math.sqrt((x1-xo)*(x1-xo)+(y1-yo)*(y1-yo)) >= r:
                    y1 -= my_step
                else:
                    x1 += my_step
        elif quadrant == 2:
            if sn == 0:  # 1 逆圆
                if math.sqrt((x1-xo)*(x1-xo)+(y1-yo)*(y1-yo)) >= r:
                    y1 -= my_step
                else:
                    x1 -= my_step
            else:
                if math.sqrt((x1-xo)*(x1-xo)+(y1-yo)*(y1-yo)) >= r:
                    x1 += my_step
                else:
                    y1 += my_step
        elif quadrant == 3:
            if sn == 0:  # 1 逆圆
                if math.sqrt((x1-xo)*(x1-xo)+(y1-yo)*(y1-yo)) >= r:
                    x1 += my_step
                else:
                    y1 -= my_step
            else:
                if math.sqrt((x1-xo)*(x1-xo)+(y1-yo)*(y1-yo)) >= r:
                    y1 += my_step
                else:
                    x1 -= my_step
        elif quadrant == 4:
            if sn == 0:  # 1 逆圆
                if math.sqrt((x1-xo)*(x1-xo)+(y1-yo)*(y1-yo)) >= r:
                    y1 += my_step
                else:
                    x1 += my_step
            else:
                if math.sqrt((x1-xo)*(x1-xo)+(y1-yo)*(y1-yo)) >= r:
                    x1 -= my_step
                else:
                    y1 -= my_step
        point_circle.append((x1, y1))
        total_steps -= 1


def judge_quadrant_circle(xo, yo, x1, y1, x2, y2):
    x11 = x1 - xo
    y11 = y1 - yo
    x22 = x2 - xo
    y22 = y2 - yo
    x12 = x11 + x22
    y12 = y11 + y22
    if x12 > 0 and y12 > 0:
        quadrant = 1
    elif x12 < 0 < y12:
        quadrant = 2
    elif x12 < 0 and y12 < 0:
        quadrant = 3
    elif  y12 < 0 < x12:
        quadrant = 4
    return quadrant


def get_points_circle(line_path):
    for i in range(0, len(line_path) - 2):
        xo = line_path[0][0]*my_step
        yo = line_path[0][1]*my_step
        print(xo, yo)
        x1 = line_path[i + 1][0]*my_step
        y1 = line_path[i + 1][1]*my_step

        x2 = line_path[i + 2][0]*my_step
        y2 = line_path[i + 2][1]*my_step
        print(x1, y1, "  ", x2, y2)
        quadrant = judge_quadrant_circle(xo, yo, x1, y1, x2, y2)
        print(quadrant)
        total_steps =(abs(x2 - x1) + abs(y2 - y1)) / my_step
        sn = get_sn(line_path)
        arc_interpolation(quadrant, sn, x1, y1, total_steps)


def draw_line():
    turtle.speed(1)
    turtle.pencolor("#FFC0CB")
    turtle.width(3)
    print(point)
    turtle.goto(point[0])
    turtle.pendown()
    for item in point:
        turtle.goto(item)


def draw_line_circle():
    turtle.speed(1)
    turtle.pencolor("#FFC0CB")
    turtle.width(3)
    turtle.penup()
    print(point_circle)
    turtle.goto(point_circle[0])
    turtle.pendown()
    for item in point_circle:
        turtle.goto(item)


def draw_coordinate():   # 绘制坐标线
    turtle.pencolor("#000000")
    for i in range(40):
        canvas.create_line(-500, int(20 * i), 500, int(20 * i), dash=1, width=1, )
        canvas.create_line(-500, -int(20 * i), 500, -int(20 * i), dash=1, width=1, )
        canvas.create_line(int(20 * i), -500, int(20 * i), 500, dash=1, width=1,)
        canvas.create_line(-int(20 * i), -500, -int(20 * i), 500, dash=1, width=1, )
    canvas.create_line(-500, 0, 500, 0, fill='black', width=3)
    canvas.create_line(0, 500, 0, -500, fill='black', width=3)


def draw_orignalline(xo, yo, xe, ye):  # 绘制理想曲线
    turtle.speed(10)
    turtle.pencolor("#6495ED")
    turtle.width(3)
    turtle.penup()
    turtle.goto(xo, yo)
    turtle.pendown()
    turtle.goto(xe, ye)
    turtle.penup()
    turtle.goto(xo, yo)


def get_sn(line_path):
    sn = 0
    for i in range(0, len(line_path) - 2):
        xo = line_path[i][0]*my_step
        yo = line_path[i][1]*my_step
        print(xo, yo)
        x1 = line_path[i + 1][0]*my_step
        y1 = line_path[i + 1][1]*my_step
        x2 = line_path[i + 2][0]*my_step
        y2 = line_path[i + 2][1]*my_step
    quadrant = judge_quadrant_circle(xo, yo, x1, y1, x2, y2)
    if quadrant == 1 and x1-xo == 0:
        sn = 1
    elif quadrant == 1 and x2-xo == 0:
        sn = 0
    if quadrant == 2 and x1 - xo == 0:
        sn = 0
    elif quadrant == 2 and x2 - xo == 0:
        sn = 1
    if quadrant == 3 and x1 - xo == 0:
        sn = 1
    elif quadrant == 3 and x2 - xo == 0:
        sn = 0
    if quadrant == 4 and x1 - xo == 0:
        sn = 0
    elif quadrant == 4 and x2 - xo == 0:
        sn = 1
    return sn


def draw_ideal_circle(xo, yo, x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.setheading(0)
    turtle.speed(10)
    turtle.pencolor("#6495ED")
    turtle.width(3)
    quadrant = judge_quadrant_circle(xo, yo, x1, y1, x2, y2)
    radius = abs((y1 + x1) - (xo + yo))
    if quadrant == 1:  # 第一象限
        turtle.penup()
        if (x1-xo) == 0 and (x2-xo) > 0:
            turtle.goto(x2, y2)
        else:
            turtle.goto(x1, y1)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(radius, 90)

    elif quadrant == 2:  # 第二象限
        turtle.penup()
        if (y1-yo) == 0 and (y2-yo) > 0:
            turtle.goto(x2, y2)
        else:
            turtle.goto(x1, y1)
        turtle.left(180)
        turtle.pendown()
        turtle.circle(radius, 90)

    elif quadrant == 3:   # 第三象限
        turtle.penup()
        if (x1-xo) < 0 and (x2-xo) == 0:
            turtle.goto(x1, y1)
        else:
            turtle.goto(x2, y2)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(radius, 90)

    elif quadrant == 4:   # 第四象限
        turtle.penup()
        turtle.penup()
        if (y1 - yo) < 0 and (y2 - yo) == 0:
            turtle.goto(x1, y1)
        else:
            turtle.goto(x2, y2)
        turtle.pendown()
        turtle.circle(radius, 90)


def draw_whole():
    line, circle = get_style()
    if line == 1 and circle == 0:
        turtle.clear()
        line_path = eval(getuser())
        for i in range(0, len(line_path)-1):
            xo = line_path[i][0]*my_step
            yo = line_path[i][1]*my_step
            xe = line_path[i+1][0]*my_step
            ye = line_path[i+1][1]*my_step
            draw_orignalline(xo, yo, xe, ye)
            quadrant = judge_quadrant(xo, yo, xe, ye)
            interpolation(quadrant, xo, yo, xe, ye)
            draw_line()
    elif line == 0 and circle == 1:
        turtle.clear()
        line_path = eval(getuser())
        for i in range(0, len(line_path) - 2):
            xo = line_path[0][0] * my_step
            yo = line_path[0][1] * my_step
            print(xo, yo)
            x1 = line_path[i + 1][0] * my_step
            y1 = line_path[i + 1][1] * my_step

            x2 = line_path[i + 2][0] * my_step
            y2 = line_path[i + 2][1] * my_step
            print(x1, y1, "  ", x2, y2)
            draw_ideal_circle(xo, yo, x1, y1, x2, y2)
            quadrant = judge_quadrant_circle(xo, yo, x1, y1, x2, y2)
            print(quadrant)
            total_steps = (abs(x2 - x1) + abs(y2 - y1)) / my_step
            sn = get_sn(line_path)
            arc_interpolation(quadrant, sn, xo, yo, x1, y1, total_steps)
            draw_line_circle()


def clear():
    turtle.clear()


tk.Button(master=root, text="开始绘图", command=draw_whole).pack(side=tk.LEFT)
tk.Button(master=root, text="清除图形", command=clear).pack(side=tk.LEFT)
draw_coordinate()  # 绘制坐标先
tk.mainloop()

