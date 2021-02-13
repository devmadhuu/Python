class practice01:
    str = ''
    def slicing(self, str, startidx, endindx):
        self.str = str
        return(str[startidx:endindx])

mypractice = practice01()
slicedstr = mypractice.slicing("hello world", 0, 5)
print(slicedstr)

