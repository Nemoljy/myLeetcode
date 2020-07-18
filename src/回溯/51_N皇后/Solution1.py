## 1 先全排列，并在过程中判断对角线
class Solution(object):
    def solveNQueens(self, n):

        def check_diag(track_l):  ## 相比全排列，多一个对角线判断
            diag1,diag2 = [],[]
            for k in range(len(track_l)):
                tmp1 = track_l[k] + k
                tmp2 = track_l[k] - k
                if tmp1 in diag1 or tmp2 in diag2:
                    return False
                    break
                diag1.append(tmp1)
                diag2.append(tmp2)
            return True

        def trackback(n,track):
            if not check_diag(track):
                return

            if len(track) == n:
                res.append(track[:])
                return

            for i in range(1,n+1):
                if i in track:
                    continue
                track.append(i)
                trackback(n,track)
                track.remove(i)

        def result_str(track_l):
            str_l = []
            for i in track_l:
                row = '.' * n
                str_l.append(row[:i-1]+'Q'+row[i:])

            return str_l


        n = 4
        res = []
        trackback(n,[])
        result = [result_str(k) for k in res]
        return result