# ------------------------------------------------------
# 等加速度
# @note 
#   - date    : 2022.01.18 - 02:37 (JST)
#   - version : python 3.7
#   - アクションものの放物線パラメータを調整したい用に作った
#   - 指定turnにY=0になるようなaを割り出したかったが、時間がないので取り急ぎprint
#   - なんちゃって知識しかないので、あとで勉強して拡充しておく
# ------------------------------------------------------
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def accelerate_v(v, a, t):
	return v + a * t

def accelerate_s(v, a, t):
	return v * t + a * t * t * 0.5

class vec3:
	def __init__(self, _x = 0.0, _y = 0.0, _z = 0.0):
		self.x = _x
		self.y = _y
		self.z = _z
	
	def accelerate_v(self, a, t):
		self.x = accelerate_v(self.x, a.x, t)
		self.y = accelerate_v(self.y, a.y, t)
		self.z = accelerate_v(self.z, a.z, t)
	
	def accelerate_s(self, a, t):
		return vec3(
			accelerate_s(self.x, a.x, t), 
			accelerate_s(self.y, a.y, t), 
			accelerate_s(self.z, a.z, t)
		)

	def add(self, a):
		self.x += a.x
		self.y += a.y
		self.z += a.z
	
	def max(self, m):
		self.x = max(self.x, m.x)
		self.y = max(self.y, m.y)
		self.z = max(self.z, m.z)

v0     = vec3(0, 0.00125, 0.0005)
a      = vec3(0, -0.00000030625, -0.00000005)
v0_min = vec3(0, -1, 0)
turn   = 120
velocity  = vec3()
translate = vec3()

v_x = []
v_y = []
zero_1st = False
for t in range(turn):
	if t == 0:
		velocity  = v0
	else :
		velocity.accelerate_v(a, t)
	trans = v0.accelerate_s(a, t)
	trans.max(v0_min)
	translate.add(trans)
	v_x.append(translate.z)
	v_y.append(translate.y)
	if trans.y < 0 and zero_1st == False:
		print(str(t) + ": zero")
		zero_1st = True

plt.plot(v_x, v_y)
plt.show()