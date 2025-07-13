class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()

        count = 0
        i = j = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                # Match found
                count += 1
                i += 1
                j += 1
            else:
                # Try next trainer
                j += 1

        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 10]))  # Example test case
    print(sol.matchPlayersAndTrainers([1, 2, 3], [1, 2, 3]))  # Example test case
    print(sol.matchPlayersAndTrainers([5, 6], [1, 2, 3, 4]))  # Example test case
    print(sol.matchPlayersAndTrainers([10, 20], [15, 25]))  # Example test case
