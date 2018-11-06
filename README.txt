--------------------------------------------------README for the Cache Simulator-----------------------------------------------------------



This cache simulator can simulate both split and unified caches with configurable associativity, cache-size and block-size. This is trace-based and hence a memory access trace file should be parsed as an input parameter along with the cache configurations. The trace file has to be in below format.

It should have two fields: 'Access Type' and 'Address'.
2 0                           #This is an instruction fetch at hex address 0.
0 1000                        #This is a data read at hex address 1000.
1 70f60888		      #This is a data write at hex address 70f60888.

An example trace file named trace.din extracted using dineroIV cache simulator is used to test this simulator which is available in this repository.
 
The simulator should be run using the following command:
--------------------------------------------------------------------------
$ python3 main.py <tracefile> <Address size> <cache model> <associativity>
--------------------------------------------------------------------------
In the above command, the Address size is 32-bit or 64-bit or any address size, cache model is configurable to 'unified' or 'split' and the cache associativity parameter can be tuned from direct to fully set-associative which is the set-size:  
		-----------------------------		
		| set size   | associativity |
		-----------------------------
		|    1       | direct        |
		|    2       | 2-way         |
		|    "       |  "            | 
		|    "       |  "            |
		|    "       |  "            |
		|cacheblocks"| fully         |
		-----------------------------
("where cacheblocks is total number of blocks inside the cache)
