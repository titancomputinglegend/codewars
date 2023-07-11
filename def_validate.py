def validate_usr(username):
    #your code here
    alpha=list("qwertyuioplkjhgfdsazxcvbnm")
    num=list("0123456789")
    key="_"

    if len(username)>=4 and len(username)<=16:
        len_state=1
    else:
        len_state=0
    state=1
    for i in username:
        if i not in alpha:
            if i not in num:
                if i not in key:
                    state=0
    return bool(state&len_state)
print(validate_usr(""))