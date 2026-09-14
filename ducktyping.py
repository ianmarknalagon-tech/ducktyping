class Textfile:
    def read(self):
        return "Content a text file"

class NetworkStream:
    def read(self):
        return "Data streamed from a network"

class MemoryBuffer:
    def read(self):
        return "Bytes  stored in memory"

def show_contents(source):
    if hasattr(source, "read"):
        print(source.read())
    else:
        print("this object Can't be read")
        
for s in [Textfile(), NetworkStream(), MemoryBuffer()]:
    show_contents(s)
