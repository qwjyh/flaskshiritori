def iskatahira(strj):
    #日本語チェック用
    hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん"
    katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴ"

    #文字列の中身がすべてカタカナかひらがなの場合のみTrueを返す
    return all([ch in katakana or ch in hiragana for ch in strj])

# # 判定
# class Judgement():
#     word_list = []

#     def __init__(self):
#         self.word_list = []
#         print("created judge instance")
    
#     def judge(self, word):
#         # 最後の文字が「ん」「ン」
#         if word[-1] == "ん" or word[-1] == "ン":
#             status = 1  # 終了
#             return status
        
#         # 日本語チェック(かな)
#         if iskatahira(word):
#             # 最初の入力
#             if self.word_list == []:    
#                 self.word_list.append(word)
#                 status = 0
#                 return status
#             elif word[0] == self.word_list[-1][-1]:
#                 for words in self.word_list:
#                     # 重複チェック
#                     if words == word:
#                         status = 3
#                         return status
#                 # ジャッジをパス
#                 self.word_list.append(word)
#                 status = 0
#                 return status
#             else:
#                 status = 2 # つながってない
#         else:
#             status = 4 # 日本語じゃない