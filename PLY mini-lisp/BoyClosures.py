class boy(object):
    def f(self):
        data = {
            "name" : "firstname",
            "$name" : lambda x : data.update({"name": x}),
            "age" : 0,
            "$age" : lambda x : data.update({"age": x}),
            "type" : "funny",
            "$type" : lambda x : data.update({"type": x}),
            "height" : "6'0",
            "$height" : lambda x : data.update({"height": x}),
            "eyeColor" : "blue",
            "$eyeColor" : lambda x : data.update({"eyeColor": x}),
            "major" : "undecided",
            "$major" : lambda x : data.update({"major": x})
        }

        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)

class funnyBoy(object):
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

class boringBoy(object):
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

class smartBoy(object):
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

class stupidBoy(object):
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

def createBoy():
    dude = boy()
    dude.run('$name')('Mike')
    profile(dude)
    return dude

def profile(self):
    print
    print "Here is"+self.run('name')+":"
    print 'Name:', self.run('age')
    print 'First impression:' + boy.run('type')
    print 'Height:', self.run('height')
    print 'Eyes:' + self.run('eyeColor')
    print 'Major:' + self.run('major')

boy1 = funnyBoy()
boy2 = boringBoy()
boy3 = smartBoy()
boy4 = stupidBoy()

createBoy()
