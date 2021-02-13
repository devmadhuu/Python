class practice01:
    str = ''
    def slicing(self, str, startidx, endindx):
        self.str = str
        return(str[startidx:endindx])

mypractice = practice01()
slicedstr = mypractice.slicing("hello world", 0, 5)
pythonword = mypractice.slicing("python is a powerful language", 0, 6)
newslicedstr = mypractice.slicing("python is powerful language ", -9, -1)
print(slicedstr)
print(pythonword)
print(newslicedstr)

