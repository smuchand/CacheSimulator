import TraceHandler as th
from Cache import Cache
import sys


class CacheSimulator:
    def __init__(self, filename, addrSize, cacheModel, associativity):
        self.cacheModel = cacheModel
        self.associativity = associativity
        self.filename = filename
        self.addrSize = addrSize

        if self.cacheModel == '0':
            self.cacheSize = input('Enter Cache Size: ')
            #cacheSize
            self.blockSize = input('Enter Cache-block Size: ')
            #blockSize

        elif self.cacheModel == '1':
            self.icacheSize = input('Enter Instruction-Cache Size:')
            self.dcacheSize = input('Enter Data-Cache Size:')
            self.blockSize = input('Enter Cache-block Size: ')

    def simulate(self):

        #model '0' is unified
        iaddress = []
        daddress = []
        if self.cacheModel == '0':
            address = th.trace_handler(self.cacheModel, self.filename)
            cache = Cache(self.addrSize, self.cacheSize, self.blockSize, self.associativity, address)
            hitCount, totalAccesses, = cache.buildCache()
            self.display(totalAccesses, hitCount)

        #Split cache
        elif self.cacheModel == '1':
            access_type, address = th.trace_handler(self.cacheModel, self.filename)
            for i in range(len(access_type)):
                if access_type[i] == '2':
                    iaddress.append(address[i])

                elif access_type[i] == '1' or '0':
                    daddress.append(address[i])

            icache = Cache(self.addrSize, self.icacheSize, self.blockSize, self.associativity, iaddress)
            ihitCount, itotalAccesses, = icache.buildCache()

            dcache = Cache(self.addrSize, self.dcacheSize, self.blockSize, self.associativity, daddress)
            dhitCount, dtotalAccesses = dcache.buildCache()

            totalAccesses = itotalAccesses + dtotalAccesses
            hitCount = ihitCount + dhitCount
            self.display(totalAccesses, hitCount)

    def display(self, totalAccesses, hitCount):
        print("Total Accesses: ", totalAccesses)
        print("Hits: ", hitCount)
        print("Misses: ", (totalAccesses-hitCount))


if __name__ == '__main__':
    if len(sys.argv) == 5:
        CS = CacheSimulator(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        CS.simulate()
