import pandas as pd
from graphics import *

def main():
    win= GraphWin("CheapEats", 1000, 600)
    data = pd.read_csv("data.csv")

    welcome = Text(Point(500,280),"Welcome to CheapEats")
    welcome.setSize(36)
    welcome.setStyle("bold")
    welcome.setFace("courier")
    welcome.draw(win)

    zct = Text(Point(500,320),"please enter your zipcode below")
    zct.setSize(18)
    zct.setStyle("normal")
    zct.setFace("courier")
    zct.draw(win)

    zc = Entry(Point(500, 400), 6)
    zc.setSize(15)
    zc.setText("")
    zc.setFill("white")
    zc.setFace("courier")
    zc.draw(win)

    gor = Rectangle(Point(486,430),Point(514,450))
    gor.setFill("black")
    gor.setOutline("black")
    gor.draw(win)

    gob = Text(Point(500,440),"Go")
    gob.setSize(16)
    gob.setStyle("bold")
    gob.setFace("courier")
    gob.setFill('white')
    gob.draw(win)

    win.getMouse()

    zip = int(zc.getText())

    while zip not in data['ZIPCODE'].unique():
        waring = Text(Point(500, 500), "sorry, no available restaurants in your area, click to retry")
        waring.setSize(14)
        waring.setFace("courier")
        waring.draw(win)
        win.getMouse()
        zc.setText("")
        waring.undraw()
        win.getMouse()
        zip = int(zc.getText())

    welcome.undraw()
    zct.undraw()
    zc.undraw()
    gor.undraw()
    gob.undraw()

    df = data.loc[data['ZIPCODE'] == zip]
    restaurant = df['RESTNAME']
    discount = df['DISCOUNT']
    dp = list(map("{}%".format, discount))

    title = Text(Point(500,130),zip)
    title.setSize(25)
    title.setFace("courier")
    title.draw(win)

    rt = Text(Point(300,200),"Restaurant")
    rt.setSize(30)
    rt.setFace("courier")
    rt.setStyle("bold")
    rt.draw(win)

    dt = Text(Point(700, 200), "Discount")
    dt.setSize(30)
    dt.setFace("courier")
    dt.setStyle("bold")
    dt.draw(win)

    c = 280
    for a in restaurant:
        b = Text(Point(300,c),a)
        b.setSize(20)
        b.setFace("courier")
        b.draw(win)
        c+=40

    f = 280
    for d in dp:
        e = Text(Point(700, f), d)
        e.setSize(20)
        e.setFace("courier")
        e.draw(win)
        f += 40

    comment = Text(Point(500,560),"press 'e' to exit the program, press 'a' to enter another zipcode")
    comment.setSize(15)
    comment.setFace("courier")
    comment.draw(win)

    ip = win.getKey()
    if ip == 'a':
        win.close()
        main()
    elif ip == 'e':
        win.close()



main()