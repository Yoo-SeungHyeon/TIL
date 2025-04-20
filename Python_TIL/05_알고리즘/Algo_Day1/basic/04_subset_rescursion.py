# def generate_subset(depth, included):
#     if depth == len(input_list):
#         cnt_subset = [input_list[i] for i in range(len(input_list)) if included[i]]
#         subsets.append(current_subset)
#         return
#     included[depth] = False
#     generate_subset(depth+1, included)
#     included[depth] = True
#     generate_subset(depth+1, included)

# input_list = [1, 2, 3]
# subsets = []
# init_included = [False] * len(input_list)
# generate_subset(0, init_included)
# print(subsets)

'''
재귀적으로도 가능하나 이진수로 카운팅 하는 것이 더 편하다.
'''