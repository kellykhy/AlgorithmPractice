# LRU(Least Recently Used) 구현  https://gomguard.tistory.com/115
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cacheSize = 3

def solution(cacheSize, cities):
    cache = [0] # cache[0]: 실행시간 저장
    for city in cities:
        try:
            if len(cache) > cacheSize: # exception: 1 > 0
                if cache.count(city) == 0: #
                    cache.pop() #
                    cache[0] += 5 # exception-> error(except문으로 이동)
                elif cache.count(city) == 1:
                    cache[0] += 1
                    cache.remove(city)
            else:
                if cache.count(city) == 0:
                    cache[0] += 5
            cache.insert(1, city)
        except:
            cache[0] = 5 * len(cities)
    answer = cache[0]
    return answer

print(solution(cacheSize, cities))