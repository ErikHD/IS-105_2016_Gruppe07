import timeit

#lager en liste med 1000tall, legger needle midt i listen
haystack = range(1000)
needle = 500

def search_fast(haystack, needle):
    for item in haystack:
    	if item == needle:
        	return True
    return False

def search_slow(haystack, needle): 
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value

#setter opp timer og printer ut
timeFast = timeit.Timer(stmt='search_fast(haystack, needle)', setup='from __main__ import search_fast, haystack, needle')
timeSlow = timeit.Timer(stmt='search_slow(haystack, needle)', setup='from __main__ import search_slow, haystack, needle')


print timeFast.timeit()
print timeSlow.timeit()
