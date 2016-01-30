#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import numpy as np
from sympy import *

### >>> from NonlinearSolver import *; solver = NonlinearSolver()
class NonlinearSolver():
    def __init__(self):
        self.x = symbols("x")
        print("準備おk")
        print("2分法 => solver.bisection_method(実連続関数, シード値, 誤差)")
        print("ニュートン法 => solver.newton_method(実連続関数, シード値, 誤差, 反復回数)")
        print("割線法 => solver.secant_method(実連続関数, シード値, 誤差, 反復回数)")


    # f(b) * f(a) <= 0 であるかを求める
    def __judge(self, b, a, f):
        former = False if f.subs([(x, b)])>=0 else True
        latter = False if f.subs([(x, a)])>=0 else True
        return former != latter

    # 閉区間[a,b]をランダムに生成
    def __find_pair(self, f):
        a = random.uniform(-21,21)
        b = random.uniform(-21,21)
        return (b, a) if self.__judge(b, a, f) else self.__find_pair(f)

    # 2分法
    def bisection_method(self, f, seed, epsilon):
        try:
            random.seed(seed)
            b, a = self.__find_pair(f)
            def go(b, a, iteration):
                c = (b+a)/2
                print("iteration {0}: \tx={1},\tf(x)={2}".format(iteration, float(c), float(f.subs([(x, c)]))))
                return c if abs(b-a) < epsilon else (go(c, a, iteration+1) if self.__judge(c, a, f) else go(b, c, iteration+1))
            return go(b, a, 0)
        except RuntimeError:
            print("~~~~f(x)=0となる解が存在しないかもしれない~~~~")
        except:
            print("~~~~計算途中で問題が起きた~~~~")

    # ニュートン法
    def newton_method(self, f, seed, epsilon, iter):
            random.seed(seed)
            a = random.uniform(-21,21)
            f_dash = diff(f, self.x)
            def go(a, iteration):
                try:
                    b = a - f.subs([(x, a)]) / f_dash.subs([(x,a)])
                    print("iteration {0}: \tx={1},\tf(x)={2}".format(iteration, float(b), float(f.subs([(x, b)]))))
                    return float(b) if abs(b-a)<epsilon or iter<=iteration else go(b, iteration+1)
                except RuntimeError:
                    print("~~~~f(x)=0となる解が存在しないかもしれない~~~~")
                except:
                    print("~~~~計算途中で問題が起きた~~~~")
            return go(a, 0)

    # 割線法
    def secant_method(self, f, seed, epsilon, iter):
            random.seed(seed)
            a = random.uniform(-21,21) # x_0
            b = random.uniform(-21,21) # x_1
            def go(b, a, iteration):
                try:
                    c = b - ((b-a)*f.subs([(x, b)]))/(f.subs([(x, b)])-f.subs([(x, a)]))
                    print("iteration {0}: \tx={1},\tf(x)={2}".format(iteration, float(c), float(f.subs([(x, c)]))))
                    return float(b) if abs(c-b)<epsilon or iter<=iteration else go(c, b, iteration+1)
                except RuntimeError:
                    print("~~~~f(x)=0となる解が存在しないかもしれない~~~~")
                except:
                    print("~~~~計算途中で問題が起きた~~~~")
            return go(b, a, 0)

x = symbols("x")

if __name__ == '__main__':
        solver = NonlinearSolver()
        print("===Bisection method===")
        print(solver.bisection_method(x**2+3*x+1, 1, 0.00001))
        print("===================")

        print("===Newton method===")
        print(solver.newton_method(x**2+3*x+1, 2, 0.00001, 100))
        print("===================")

        print("===Secant method===")
        print(solver.secant_method(x**2+3*x+1, 2, 0.00001, 100))
        print("===================")
