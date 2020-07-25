import os,re
def get_filelist(path):
    Filelist = []
    for home, dirs, files in os.walk(path):
        Filelist.append(home.replace('\\', '/'))
    return Filelist


if __name__ == "__main__":
    path ='./src/'
    Filelist = list(set(get_filelist(path)))
    Filelist.sort()
    Filelist = [k for k in Filelist if not '.ipynb_checkpoints' in k]
    Filelist.remove(path)
    
    f = open('./README.md','w')
    f.write('# myLeetcode\nLeetcode刷题记录，自202006\n\n')

    for file in Filelist:
        if re.match(path+r'.+?/.+?',file):  ## 有更深一层，如 ./src/Hash/1_两数之和
            f.write('- ['+file.split('/')[-1]+']('+file+')\n' )
        else:   ## 无更深一层，如 ./src/Hash
            f.write('\n### ['+file.split('/')[-1]+']('+file+')\n' )
    f.close()
