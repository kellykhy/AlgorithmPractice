# LRU(Least Recently Used) 구현  https://gomguard.tistory.com/115
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
cacheSize = 2

def solution(cacheSize, cities):
    cache = [0] # cache[0]: 실행시간 저장
    cities = [city.lower() for city in cities]
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    for city in cities:
        if len(cache) > cacheSize:
            if cache.count(city) == 0:
                cache.pop()
                cache[0] += 5
            elif cache.count(city) == 1:
                cache[0] += 1
                cache.remove(city)
        else:
            if cache.count(city) == 0:
                cache[0] += 5
            elif cache.count(city) == 1:
                cache[0] += 1
                cache.remove(city)
        cache.insert(1, city)
    answer = cache[0]
    return answer

print(solution(cacheSize, cities))