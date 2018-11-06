This is the README for the Cache Simulator. This simulator is fully configurable to split and unified caches with any chosen associativity, cache and block sizes. This cache simulator works reading a memory access trace file and simulating the cache behaviour based on the user-chosen cache paraemters.

This cache Associativity can be tuned from direct to fully set-associative :  
		-----------------------------		
		| set size  | associativity |
		-----------------------------
		|    1      | direct        |
		|    2      | 2-way         |
		|    "      |  "            | 
		|    "      |  "            |
		|    "      |  "            |
		|cacheblocks| fully         |
		-----------------------------
