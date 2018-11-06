import math
import numpy as np
from collections import defaultdict


class Cache:
    def __init__(self, addrSize, cacheSize, blockSize, associativity, address):
        self.cacheSize = int(cacheSize)
        self.blockSize = int(blockSize)
        self.associativity = int(associativity)
        self.cacheBlocks = math.ceil(self.cacheSize/self.blockSize)
        self.address = address
        self.addrSize = int(addrSize)
        self.cache = np.zeros((self.cacheBlocks, self.blockSize), dtype='U32')
        self.sets = int(self.cacheBlocks / self.associativity)
        self.tag_array = np.zeros((self.sets, self.associativity), dtype='U32')
        self.access = 0

    def buildCache(self):
        hitCount = 0
        offset_length = math.ceil(math.log2(self.blockSize))
        index_length = (math.ceil(math.log2(self.sets)))
        tag_length = self.addrSize - (offset_length + index_length)
        print("|", tag_length, "|", index_length, "|", offset_length, "|")

        for addr in self.address:
            binAddr = (bin(int(addr, 16))[2:].zfill(self.addrSize))
            addr_tag = binAddr[:tag_length]
            addr_index = binAddr[tag_length:-offset_length]
            hitCount += self.isInCache(addr_index, addr_tag)

        return hitCount, self.access

    def isInCache(self, index, tag):
        if index != '':
            index = int(index, 2)
        else:
            index = 0
        tag = str(hex(int(tag, 2))[2:])
        dirty_bit_dict = defaultdict(lambda: defaultdict(int))
        hit_count = 0
        miss_count = 0
        self.access += 1
        #print("tag: ", tag)
        #print("index: ", index)
        #print(self.associativity)
        for wayID in range(self.associativity):
            #print("line:", wayID)
            dirty_bit_dict[index][wayID] = 0
            if tag == self.tag_array[index, wayID]:
                #print("Hit")
                hit_count += 1
                if dirty_bit_dict[index][wayID] < 4:
                    dirty_bit_dict[index][wayID] += 1

            else:
                #print("Miss")
                miss_count += 1
                if dirty_bit_dict[index][wayID] < 4:
                    dirty_bit_dict[index][wayID] += 1

        if miss_count == self.associativity:
            #checking for cache blocks to replace or fill with
            self.cacheMissHandler(index, tag, dirty_bit_dict)

        return hit_count

    def cacheMissHandler(self, index, tag, dirty_bit_dict):
        spots = self.associativity

        for wayID in range(self.associativity):
            if len(self.tag_array[index][wayID]) > 0:
                if spots == 0:
                    block_index, block_way = self.replaceBlock(dirty_bit_dict, index)
                    self.tag_array[block_index][block_way] = tag
                else:
                    spots -= 1

            else:
                self.tag_array[index][wayID] = tag
                break

    def replaceBlock(self, dirty_bit_dict, index):
        status_bits = []
        for i in range(self.associativity):
            status_bits.append([index, i, dirty_bit_dict[index][i]])

        block = max(status_bits[2])
        id = status_bits[2].index(block)
        block_index = status_bits[0][id]
        block_way = status_bits[1][id]

        return block_index, block_way
