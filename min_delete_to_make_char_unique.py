from  collections import Counter
class Solution:
    def create_dict(self,s):
        dict_1 = dict()
        for char in s:
            if char not in dict_1.keys():
                dict_1[char] = 1
            else:
                dict_1[char] += 1

        return dict_1

    def using_counter_dict(self,s):
        #in dict_1, creating a dictionary using a method
        dict_1=self.create_dict(s)
        # in dict_2, creating a dictionary using Counter Module
        dict_2=Counter(s)
        count=0
        set_counter=set()
        for ele in dict_2:
            cur_len=dict_2[ele]
            if cur_len in set_counter:
                for i in range(1,cur_len+1):
                    #count += 1
                    if cur_len-i not in set_counter:
                        count += 1
                        set_counter.add(dict_2[ele]-i)
                        break

            else:
                set_counter.add(dict_2[ele])
        #print(set_counter)
        return count




sol = Solution()
s="ceabaacb"
print(sol.using_counter_dict(s))