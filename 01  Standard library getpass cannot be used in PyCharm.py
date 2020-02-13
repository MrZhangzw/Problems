def win_getpass(prompt='Password: ', stream=None): # Lib_getpass Line72
    """Prompt for password with echo off, using Windows getch()."""
    if sys.stdin is not sys.__stdin__: 
        # 调试1：VScode,PyCharm的stdin判断是is,都跳过了此if
        return fallback_getpass(prompt, stream)

    for c in prompt:
        # print(c,end='')
        msvcrt.putwch(c) 
        # print('put it!')
        # 调试3：发现Pycharm在这里完成循环了,可是没办法显示prompt里的c，不同于VScode
        # 猜测：msvcrt.putwch()未运行
        '''
        PyCharm单独运行msvcrt.putch()与msvcrt.putwch()不可用
        结论:PyCharm控制台对putch无法运行，控制台在程序有机会读取之前消耗了输入。CSDN有同样反映。
        '''
    
    pw = "" # pw是password吧，下面都是管密码的
    while 1: # 上面改print之后这里getwch仍然不行
        c = msvcrt.getwch()
        # print('cget'),PyCharm这里没运行
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            pw = pw[:-1]
        else:
            pw = pw + c
            # print('haha我get啦') 
            #调试2：VScode运行了，Pycharm没有到这里。说明卡在上面了
    msvcrt.putwch('\r')
    msvcrt.putwch('\n')
    return pw
