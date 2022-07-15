# LRU(Least Recently Used) 구현
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cache_size = 2
cache = [0] # cache[0]: 실행시간 저장
def calc_cache(cache, string, cache_size):
    try:
        if len(cache) > cache_size: # exception: 1 > 0
            if cache.count(string) == 0: #
                cache.pop() #
                cache[0] += 5 # exception-> error(except문으로 이동)
            elif cache.count(string) == 1:
                cache[0] += 1
                cache.remove(string)
        else:
            if cache.count(string) == 0:
                cache[0] += 5
        cache.insert(1, string)
    except:
        cache[0] = 5 * len(cities)
    finally:
        return cache

for city in cities:
    cache = calc_cache(cache, city, cache_size)

print(cache[0])