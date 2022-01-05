# https://practice.geeksforgeeks.org/problems/squares-in-nn-chessboard1801/1

class Solution:
    def squaresInChessBoard(self, N):
         # code here
         sq=0
         for i in range(1,N+1):
             sq+=i*i
         return sq 
