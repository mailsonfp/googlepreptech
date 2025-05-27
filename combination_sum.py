class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global_output = []
        current_candidates = []

        def backtracking(current_sum, next_possible_candidate_index, current_candidates):
            # stack 0: next_possible_candidate_index = 0
            # stack 0: current_sum = 0
            # stack 0: cucurrent_candidates = []
            # stack 1: next_possible_candidate_index = 0
            # stack 1: current_sum = 2
            # stack 1: current_candidates = [2]
            # stack 2: next_possible_candidate_index = 0
            # stack 2: current_sum = 4
            # stack 2: current_candidates = [2,2]
            # stack 3: next_possible_candidate_index = 0
            # stack 3: current_sum = 6
            # stack 3: current_candidates = [2,2,2]
            # stack 4: next_possible_candidate_index = 1
            # stack 4: current_sum = 6
            # stack 4: current_candidates = [2,2,2]
            print(f"entrada - current_sum: {current_sum}")
            number = candidates[next_possible_candidate_index]
            current_sum += number
            print(f"primeira soma - current_sum: {current_sum}")
            # stack 0: number = 2
            # stack 0: current_sum = 2
            # stack 1: number = 2
            # stack 1: current_sum = 4
            # stack 2: number = 2
            # stack 2: current_sum = 6
            # stack 2: number = 2
            # stack 2: current_sum = 8
            # stack 2: number = 3
            # stack 2: current_sum = 9

            # stack 0: current_sum = 2 != 7
            # stack 1: current_sum = 4 != 7
            # stack 2: current_sum = 6 != 7
            # stack 3: current_sum = 8 > 7
            # stack 4: current_sum = 9 > 7
            if current_sum > target:
                return
            elif current_sum == target:
                current_candidates.append(number)
                global_output.append(current_candidates)
                current_candidates = []
                return

            current_candidates.append(number)
            # stack 0: current_candidates = [2]
            # stack 1: current_candidates = [2,2]
            # stack 2: current_candidates = [2,2,2]
            backtracking(current_sum, next_possible_candidate_index, current_candidates)
            print(f"retorno bactracking - current_sum: {current_sum}")

            # stack 2: current_candidates = [2,2,2]
            next_possible_candidate_index += 1
            for next_possible_candidate_index in range(len(candidates)):
                # stack 2: current_sum = 6, next_possible_candidate_index = 1, current_candidates=[2,2,2]
                backtracking(current_sum, next_possible_candidate_index, current_candidates)

        backtracking(0, 0, current_candidates)

        return global_output