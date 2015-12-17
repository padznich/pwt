data = 'are ghjwe are slfmhere sdf.' # 'are' 'we' 'here'
args = {'are', 'we', 'here'}

def de(data, args):
    import re
    data.lower()
    out = 0
    for arg in args:
        if arg in data:
            out += 1
#        print('DEBUG:', arg)
    print(out)

de(data, args)