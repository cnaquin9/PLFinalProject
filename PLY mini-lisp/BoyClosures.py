class boy(object):
    def f(self):
        data = {
            "name" : "Jimbo",
            "$name" : lambda x : data.update({"name": x}),
            "age" : 19,
            "$age" : lambda x : data.update({"age": x}),
            "type" : "Funny",
            "$type" : lambda x : data.update({"type": x}),
            "height" : "6'0",
            "$height" : lambda x : data.update({"height": x}),
            "eyeColor" : "Blue",
            "$eyeColor" : lambda x : data.update({"eyeColor": x}),
            "major" : "Undecided",
            "$major" : lambda x : data.update({"major": x})
        }

        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)

class funnyBoy(boy):
    def f(self):
        data = {
            "type" : "funny",
            "$type" : lambda x : data.update({"type", x}),
            "major" : "RTF",
            "$major" : lambda x : data.update({"major", x})
        }

        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return super(funnyBoy, self).run(d)
        return cf
    run = f(1)

class boringBoy(boy):
    def f(self):
        data = {
            "type" : "boring",
            "$type" : lambda x : data.update({"type", x}),
            "major" : "history",
            "$major" : lambda x : data.update({"major", x})
        }

        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return super(boringBoy, self).run(d)
        return cf
    run = f(1)

class smartBoy(boy):
    def f(self):
        data = {
            "type" : "smart",
            "$type" : lambda x : data.update({"type", x}),
            "major" : "engineering",
            "$major" : lambda x : data.update({"major", x})
        }

        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return super(smartBoy, self).run(d)
        return cf
    run = f(1)

class stupidBoy(boy):
    def f(self):
        data = {
            "type" : "stupid",
            "$type" : lambda x : data.update({"type", x}),
            "major" : "liberal arts",
            "$major" : lambda x : data.update({"major", x})
        }

        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return super(stupidBoy, self).run(d)
        return cf
    run = f(1)


def makeBoyfriend():
    boy = funnyBoy()
    boy.run('$name')('Mark')
    boy.run('$age')(21)
    boy.run('$height')('6 foot 2')
    boy.run('$eyeColor')('Green, like emeralds or something')
    print ("")
    print ("QTP2T <3:")
    profile(boy)
    print ("")

def profile(self):
    print 'Name: ', self.run('name')
    print 'Age: ', self.run('age')
    print 'First impression: ' + self.run('type')
    print 'Height:', self.run('height')
    print 'Eyes: ' + self.run('eyeColor')
    print 'Major: ' + self.run('major')

def makeFriends():
    b1,b2,b3 = boringBoy(), smartBoy(), stupidBoy()
    a = [b1, b2, b3]
    print ("")
    print "These guys aren't boyfriend material:"
    names = ["Tom", "Jerry", "Eugene"]
    ages = ["19", "30", "2...6?"]
    ec = ["Black like his soul", "Not good", "Red"]
    heights = ['too short', 'too tall', 'just right but still not good for some reason']
    for i in range(len(a)):
        a[i].run('$name')(names[i])
        a[i].run('$age')(ages[i])
        a[i].run('$height')(heights[i])
        a[i].run('$eyeColor')(ec[i])
        profile(a[i])
        print ("")


