import os,re
def get_filelist(path):
    Filelist = []
    for home, dirs, files in os.walk(path):
        Filelist.append(home.replace('\\', '/'))
    return Filelist

def generateRM(path):
    Filelist = list(set(get_filelist(path)))
    Filelist.sort()
    Filelist = [k for k in Filelist if not '.ipynb_checkpoints' in k]
    Filelist.remove(path)
    
    if path == './Leetcode/':
        f = open('./README.md','w')
        f.write('# myLeetcode\nLeetcode刷题记录，自202006\n\n')
    else:
        f = open('./README.md','a')
        f.write('# 剑指Offer\n剑指Offer刷题记录，自202007\n\n')

    for file in Filelist:
        if re.match(path+r'.+?/.+?',file):  ## 有更深一层，如 ./Leetcode/Hash/1_两数之和
            f.write('- ['+file.split('/')[-1]+']('+file+')\n' )
        else:   ## 无更深一层，如 ./Leetcode/Hash
            f.write('\n### ['+file.split('/')[-1]+']('+file+')\n' )
    f.write('\n\n' )
    f.close()

if __name__ == "__main__":
    LC = './Leetcode/'
    NC = './Newcoder/'
    generateRM(LC)
    generateRM(NC)