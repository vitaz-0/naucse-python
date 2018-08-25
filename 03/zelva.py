from turtle import forward, left, right, shape, exitonclick
from turtle import penup, pendown

shape('turtle')


def obdelnik():
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)


for i in range(4):
    obdelnik()
    right(30)


exitonclick()


# def carka(delka):
#     forward(delka)
#
#
# def mezera(delka):
#     penup()
#     forward(delka)
#     pendown()
#
#
# def cm(c, m):
#     carka(c)
#     mezera(m)
#
#
# def cara(delka_cary):
#     carka_d = 7
#     mezera_d = 3
#     pocet_carek = delka_cary / (carka_d + mezera_d)
#     print('POCET: '+str(pocet_carek))
#     i = 0
#     while i < pocet_carek:
#         print("I: "+str(i))
#         carka_d = carka_d + 0.5
#         mezera_d = mezera_d + 0.5
#         cm(carka_d, mezera_d)
#         i = i + 1
#
#
# cara(100)
# exitonclick()
