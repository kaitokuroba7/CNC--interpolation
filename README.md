1.项目平台
====

本项目基于python平台设计，适用于python3.6及以上的版本。该项目主要调用了python内置的GUI模块Tkinter，并在其中内嵌了python的海龟绘图（TurtleGraphics）。其主要借鉴的是海龟绘图中的turtle.RawTurtle模块，其特点是轻量化且能嵌入Tkinter中。

2.项目主要功能
====
该项目主要针对数控机床CNC中的插补算法进行模拟，并对课本中仅在第一象限的插补进行扩展。目前，能够实现圆弧以及直线的插补。此外，该插补项目设计了用户交互界面，操作简单。

2.1直线插补功能
---
针对直线插补，用户以标准形式输入任意多个点，并点击“开始绘图”即可开始动态直线绘图以及插补。如输入`[(0,0),(4,3)]`并点击“开始绘图”即可实现`(0,0)`点到`(4,3)`点的直线插补。此外，该直线插补能够实现任意象限的跨越以及任意点对点之间的组合。

2.2圆弧插补功能
----
针对圆弧插补，用户输入圆形坐标，平行于X轴的半径坐标以及平行于Y轴的半径坐标并点击“开始绘图”即可开始动态的圆弧绘制以及插补。如输入`[(0,0),(5,0),(0,5)]`并点击“开始绘图”即可生成以`(0,0)`点为圆心，5为半径，起始坐标为`(5,0)`，终点坐标为`(0,5)`的1/4圆弧插补。该项目的圆弧均以`90°`为单位进行插补，圆心可任意自取。

3.应用功能举例
====

3.1直线插补举例
----
多点直线插补的数控模拟界面如图1所示。其中，蓝色线段为理想直线，红色线段为插补直线。我们输入的多段直线坐标为`[(3,5),(-12,10),(-20,-13),(-6,-8),(6,-8),(19,-19),(7,15),(7,20),(-12,20),(-20,15)]`。这里一共包含了`10`个坐标点，`9`段直线，既有象限与象限之间的跨越，又有水平直线与数值直线的插补，基本能够满足直线插补的所有要求。

<p align="center">
	<img src="https://github.com/kaitokuroba7/CNC--interpolation/blob/master/CNC_1.png" alt="Sample"  width="300" height="300">
	<p align="center">
		<em> 图1 多点直线插补演示界面</em>
	</p>
</p>
                          
3.2圆弧插补举例
----
圆弧插补的演示界面如图2所示。图2中的蓝色圆弧为绘制的理想圆弧，红色线段为插补线段。在该例中，输入的坐标为`[(-4,-3),(11,-3),(-4,12),(-19,-3),(-4,-18),(11,-3)]`，即是以`(-4，-3)`点为圆心，四段圆弧组成的一个整圆。该例子实现了圆弧的跨象限插补，圆心坐标不在原点的插补，以及多个圆弧的拼接。相比课本中例子，该插补体现了本项目更加出色的功能。
 
 <p align="center">
	<img src="https://github.com/kaitokuroba7/CNC--interpolation/blob/master/CNC_2.png" alt="Sample"  width="300" height="300">
	<p align="center">
		<em> 图2 圆弧插补演示界面</em>
	</p>
</p>


4.项目未来计划
====
该项目虽然只是一个课堂大作业，但是确实给了我很多的收获。由于时间有限，目前该项目仍还有很多的缺陷，因此，我希望将来有时间能够完善这个项目。

4.1画板的放大收缩
----
目前的绘图画板是固定的，也就是输入的坐标有其大小限制。这给计算带来了诸多不便。因此，我们希望能够实现画板的大小变化，针对小坐标，画板可以实现收缩，针对大坐标，画板可以实现放大。

4.2任意圆弧角度的输入
----
目前的圆弧插补只能够实现90圆弧及其整数倍圆的插补。而我们需要更加精确的圆弧插补。因此，我们希望未来能够实现任意圆弧角度的插补。使得整个项目的精确的更好。
