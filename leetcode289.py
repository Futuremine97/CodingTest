class Solution:
          
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J) 
                                  #counter 써서 index, value 해쉬 테이블 
                                  for i, j in live
                                  for I in range(i-1, i+2)# 총 range len 이 3개
                                  for J in range(j-1, j+2)# 총 3개
                                  if I != i or J != j
                                 # if 옵션에 대해서만 수행.중심점 제외. )
        return {ij #위치 리턴 
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}#합이 3개혹은 2개 & ij 가 Live 에 있을 때.

                                
                                  
    def gameOfLife(self, board):
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live }  
                                  # 딕셔너리 live 생성
                                  
        live = self.gameOfLifeInfinite(live) #live 의 위치 생성 
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live) # row 생성 