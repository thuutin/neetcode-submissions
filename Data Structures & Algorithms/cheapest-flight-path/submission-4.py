class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k >= 0
        # src, dst: there are some valid answers?
        # node is (airport, # of stops)
        # distance is the price
        # edge is a flight
        # stops also count dst and src
        adj = defaultdict(list)
        for u, v, p in flights:
            adj[u].append((v, p))
        pq = [(0, 1, src)]
        prices = defaultdict(lambda : 1001 * len(flights))
        prices[(1, src)] = 0
        k += 2
        while pq:
            price, stops, airport = heapq.heappop(pq)
            node = stops, airport
            if prices[node] < price:
                continue
            if airport == dst:
                return price
            for neibour, flight_price in adj[airport]:
                if prices[(stops + 1, neibour)] < price + flight_price:
                    continue
                if stops + 1 > k:
                    continue
                prices[(stops + 1, neibour)] = price + flight_price
                heapq.heappush(pq, (price + flight_price, stops + 1, neibour))
        return -1

