import piskvorky

win_x = "---------XOX--XXX---"
win_o = "---XOX--OXOXOOO--X--"
draw = "XOXOXOXOXOXOXOXOXOXO"
unfinished = "--XOXOXOXOXOXOXOXO--"


def test_eval():
    assert piskvorky.eval(win_x) == "X"
    assert piskvorky.eval(win_o) == "O"
    assert piskvorky.eval(draw) == "!"
    assert piskvorky.eval(unfinished) == "-"
