class Solution1:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    # Runtime: 572 ms
    def exist(self, board, word):

        row_num = len(board)
        col_num = len(board[0])
        if len(word) == 0:
            return True

        for i in range(row_num):
            for j in range(col_num):
                if word[0] == board[i][j]:
                    if len(word) > 1:
                        state = self.help_fun(board, word, i, j, 1, [[i, j]])
                    else:
                        state = True
                    if state:
                        return state

        return False

    def get_neigh(self, row_num, col_num, i, j):



        neigh_point = []
        if j < col_num-1:
            neigh_point.append([i,j+1])
        if j > 0:
            neigh_point.append([i,j-1])
        if i > 0:
            neigh_point.append([i-1,j])
        if i < row_num-1:
            neigh_point.append([i+1,j])


        return neigh_point

    def help_fun(self, board, word, i, j, begin, word_idx):
        row_num = len(board)
        col_num = len(board[0])

        if begin == (len(word)-1):

            neigh_list = self.get_neigh(row_num, col_num, i, j)
            for [p, q] in neigh_list:
                if word[begin] == board[p][q] and (not([p, q] in word_idx)):

                    return True

            return False

        else:
            state = False
            neigh_list = self.get_neigh(row_num, col_num, i, j)

            for [p, q] in neigh_list:

                if word[begin] == board[p][q] and (not([p, q] in word_idx)):
                    word_idx.append([p, q])
                    state = self.help_fun(board, word, p, q, begin+1, word_idx)
                    if not state:
                        word_idx.pop()
                    if state:
                        return state
            return state


class Solution2:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    # running time:312 ms
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for k in range(len(board)):
            board[k] = list(board[k])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i, j):
                    return True
        return False

    def exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True

            #board[i] = board[i][:j] + "#" + board[i][j+1:]
            board[i][j] = ' '

            if i > 0 and self.exist_helper(board, word[1:], i - 1, j):
                return True
            if i < len(board)-1 and self.exist_helper(board, word[1:], i + 1, j):
                return True
            if j > 0 and self.exist_helper(board, word[1:], i, j - 1):
                return True
            if j < len(board[0])-1 and self.exist_helper(board, word[1:], i, j + 1):
                return True

            #board[i] = board[i][:j] + word[0] + board[i][j+1:]
            board[i][j] = word[0]
            return False
        else:
            return False





if __name__ == '__main__':

    result = Solution2().exist(["b","a","b"], "bbabab")
    #result = Solution2().exist(["CAA", "AAA", "BCD"], "ABC")
    print result










