class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data_len = len(data)
        i = 0
        while i < data_len:
            num = data[i]
            num_binary = '{0:08b}'.format(num)
            num_chars = 0
            for char in num_binary:
                if char == '1':
                    num_chars += 1
                    continue
                break
            
            if num_chars == 1 or num_chars > 4:
                return False
            num_chars = num_chars - 1 if num_chars > 1 else 0
            check_till = i + num_chars
            if check_till >= data_len:
                return False
            for j in range(i + 1, check_till + 1):
                curr_num = data[j]
                curr_num_binary = '{0:08b}'.format(curr_num)
                if curr_num_binary[:2] != '10':
                    return False
            
            i = check_till + 1
        return True
