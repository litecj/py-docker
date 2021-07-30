import random

class MenuLunch (object):
    def menu_lunch (self):
        menu = ["김치찌개", "샐러드", "쉐이크", "불백", "삼계탕", "도시락",
                "김밥", "국밥", "아사이볼", "본죽", "비빔밥", "수제비"]
        print(random.choice(menu))

