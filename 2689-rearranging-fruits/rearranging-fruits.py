class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        total = basket1 + basket2
        count = Counter(total)
        
        # Check for feasibility
        for freq in count.values():
            if freq % 2 != 0:
                return -1
        
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        
        # Fruits to move from basket1 and basket2
        to_move1 = []
        to_move2 = []
        
        for fruit in count.keys():
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                to_move1.extend([fruit] * (diff // 2))
            elif diff < 0:
                to_move2.extend([fruit] * (-diff // 2))
        
        # No need to swap if already equal
        if not to_move1:
            return 0
        
        to_move1.sort()
        to_move2.sort(reverse=True)  # Pair smallest with largest
        
        min_cost_fruit = min(total)
        total_cost = 0
        
        for a, b in zip(to_move1, to_move2):
            direct_cost = min(a, b)
            double_swap_cost = 2 * min_cost_fruit
            total_cost += min(direct_cost, double_swap_cost)
        
        return total_cost
