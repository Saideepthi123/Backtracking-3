class Solution(object):
    # tc : O(m*n*4^L) helper function :  we check all 4 directions for each letter of thr word so we wil have 4^L and we traverse through the whoel board and in worst case perfrom the dfs at every cell which is m*n*dfs complexity
    # sc : O(L) recrussive stack space 
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.result = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]: # found the starting element of the word in the board 
                    self.helper(board,i,j,1,word) # starting letter can be foudn multiple times but once the word is foudn we wont check other paths

        return self.result


    def helper(self,board,i,j,idx,word): # idx is for which letter in word to track 
        # base 
        if idx == len(word): # means we have found the whole word 
           self.result = True
           return

        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        board[i][j] = "#" # as we are using this cell we mark this as visited 

        # action 
        for dir in dirs:
            neighbor_row = dir[0] + i
            neighbor_col = dir[1] + j

            if 0 <= neighbor_row < len(board) and 0 <= neighbor_col < len(board[0]) and board[neighbor_row][neighbor_col] == word[idx]:
                # recurse
                self.helper(board,neighbor_row, neighbor_col, idx+1,word)

        # backtrack
        # once we have process the nod neighbors and didnt fin the word then we explore the parent and look other neighbors 
        # but befpre that we have to undo markng the cell as visted and return back its original value which word[idx-1] as idx has been moved one pointer in the for loop so the original leter is word[idx-1]
        board[i][j] = word[idx-1]

        


