class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = int(((1 + 8 * candies) ** (1 / 2) - 1) / 2)
        rounds = n // num_people
        last_round = n % num_people

        s = [0] * num_people
        s[last_round] = candies - ((n + 1) * n) // 2
        cur_handout = rounds * num_people + 1
        for i in range(last_round):
            s[i] = cur_handout
            cur_handout += 1

        if rounds > 0:
            cur_handout = (2 + (rounds - 1) * num_people) * rounds // 2
            for i in range(num_people):
                s[i] += cur_handout
                cur_handout += rounds

        return s