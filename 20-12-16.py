###def p():
###   m=input()
###   s=m.split()    mm={}    for c in s :        if c in mm:            mm[c]+=1
###       else:
###           mm[c]=1
###   return mm
###print("Please enter 'print_file_stats()'")
###def print_file_stats(fname):
###    s=open(fname,'r',errors='ignore' ).read()
###    num_chars=len(s)
###    num_lines=s.count('\n')
###    keep={'.',' ','-'}
###    s=''.join(c for c in s if c in keep or c.isalpha())
###    ss=[k for k in s if k !=' ']
###    lenthwords=len(ss)
###    unt=s.split()
###    num_words=len(unt) 
###    num_avewords=lenthwords/num_words
###    num_difwords=len(set(unt))
###    b={}
###    for i in unt:
###        if i in b:
###            b[i]+=1
###        else:
###            b[i]=1
###    lst=[(n,b[n]) for n in b]
###    lst.sort(key=lambda x:x[1],reverse=True)
###    print("The file '%s' has: "%fname)
###    print("    %s charater"% num_chars)
###    print("    %s lines"%num_lines)
###    print("    %s words"%num_words)
###    print("    %s diferentwords"%num_difwords)
###    print("    %s averagewordslenth"%num_avewords)
###    print("\nThe top 10 most frequent words are:")
###    l = 1
###    for count,word in lst[:10]:
###        print('%2s. %4s %s'%(l,count,word))
###        l +=1
###    stop_words={'the','and','i','to','of','a','you','my','that','in'}
###    num=0
###    print("闄ゅ幓甯哥敤鍗曡瘝澶")
###    for u,uu in lst:
###        if u not in stop_words:
###            print(u,b[u])
###            num+=1
###        if num==10:
###            break
###    num2=0
###    print("缃曡佸瓧")
###    for ll in b:
###        if b[ll]==1:
###            print(ll+' '+str(1))
###            num2+=1
###        if num2==10:
###            break
class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):
        '''初始化'''
        self.name=name
        self.age=age
    def sit(self):
        '''模拟小狗坐下'''
        print(self.name.title()+"is now sitting.")
    def roll_over(self):
        '''模拟小狗打滚'''
        print(self.name.title()+"rolled over!")
        
