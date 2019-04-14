from functools import wraps

def type_checker(*types):
    def accepter(func):
        @wraps(func)
        def check_types(self,*argv, **kwargs):
            '''
            if len(kwargs) != 0:
                for i, elem in enumerate(kwargs.values()):
                    if type(elem) != types[i]:
                        raise ValueError('In {} not correct types are given!'.format(func.__name__))
            elif len(argv) != 0:
                for i in range(len(argv)):
                    if type(argv[i]) != types[i]:
                        raise ValueError('In {} not correct types are given!'.format(func.__name__))
            '''
            temp = kwargs.values()
            values = iter(temp)
            for i in range(len(types)):
                if len(argv) != 0:
                    if type(argv[i]) != types[i]:
                        raise ValueError('In {} not correct types are given!'.format(func.__name__))
                elif len(kwargs) != 0:
                    if type(next(values)) != types[i]:
                        raise ValueError('In {} not correct types are given!'.format(func.__name__))
            return func(self,*argv, **kwargs)
        return check_types
    return accepter