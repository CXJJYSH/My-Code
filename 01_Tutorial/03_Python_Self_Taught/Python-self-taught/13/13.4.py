class Horse:
    def __init__(self,rider):
        self.rider=rider
class Rider:
    def __init__(self,name):
        self.name=name
mick=Rider("Mick Jagger")
stanley=Horse(mick)
print(stanley.rider.name)
