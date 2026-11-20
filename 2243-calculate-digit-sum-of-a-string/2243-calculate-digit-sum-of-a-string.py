class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:# base case
            return s

        answer_str_array = []
        for i in range(0, len(s), k):
            #print(i)
            summ = 0  # reinit sum to 0
            for x in range(
                i, min(i + k, len(s))
            ):  # from i index (eg.3) to the i+k (eg3+3= 6) or len() of array
                summ += int(s[x])  # calc sum as ints

            answer_str_array.append(str(summ))
            #print("sum", summ, "".join(answer_str_array))

        return self.digitSum("".join(answer_str_array), k) # recusrsive return
