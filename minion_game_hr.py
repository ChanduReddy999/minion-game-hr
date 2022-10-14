"""minion game hackerrank"""

'''method 1'''

# def minion_game(string):
#     # your code goes here
#     vowels = 'AEIOU'
#     Stuart_score, Kevin_score = 0, 0
#     length = len(string)
#     for start_idx in range(length):
#         score = length - start_idx
#         if string[start_idx] in vowels:
#             Kevin_score += score
#         else:
#             Stuart_score += score
#     if Stuart_score == Kevin_score:
#         print('Draw')
#     if Stuart_score > Kevin_score:
#         print('Stuart {}'.format(Stuart_score))
#     if Stuart_score < Kevin_score:
#         print('Kevin {}'.format(Kevin_score))

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


'''method 2'''

# def minion_game(string):
#    # your code goes here
#     string = string.lower()
#     l = len(string)
#     Kevin_score = 0
#     Stuart_score = 0
    
#     for i in range(l):
#         if string[i] in "aeiou":
#             Kevin_score += l-i
            
#     if l%2 == 0:    
#         Stuart_score = ((l+1)*l//2) - Kevin_score
#     else:
#         Stuart_score = ((l+1)*(l//2)+((l+1)/2)) - Kevin_score    
        
#     if Stuart_score > Kevin_score:
#         print("Stuart {}".format(Stuart_score))
#     elif Stuart_score < Kevin_score:
#         print("Kevin {}".format(Kevin_score))
#     else:
#         print("Draw")

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

