class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        num_of_cities = len(locations)
		
        shorted_paths = [-1] * num_of_cities
        import heapq
        heap = [(0, finish)]
        while heap: # dijkstra's algorithm
            fuel_used, city = heapq.heappop(heap)
            if shorted_paths[city] >= 0 and shorted_paths[city] <= fuel_used:
                continue
            shorted_paths[city] = fuel_used
            for next_city in range(num_of_cities):
                if next_city == city: continue
                fuel_cost = abs(locations[next_city] - locations[city])
                if shorted_paths[next_city] < 0 or shorted_paths[next_city] > fuel_used + fuel_cost:
                    heapq.heappush(heap, (fuel_used + fuel_cost, next_city))
					
        @lru_cache(None)
        def travel(city, fuel): # top down dp
            if fuel < shorted_paths[city]: return 0 # if not enough fuel to go back to final
            count = city == finish
            for next_city in range(num_of_cities):
                if next_city == city: continue
                fuel_cost = abs(locations[next_city] - locations[city])
                if fuel_cost <= fuel:
                    count = (count + travel(next_city, fuel - fuel_cost)) % MOD
            return count
        return travel(start, fuel)