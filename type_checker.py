from functools import wraps

def type_checker(*types):
    def accepter(func):
        @wraps(func)
        def check_types(*argv, **kwargs):
            for i in range(len(types)):
                if type(argv[i+1]) != types[i]:
                    raise ValueError('In {} not correct types are given!'.format(func.__name__))
            for i, elem in enumerate(kwargs):
                if type(elem) != types[i]:
                    raise ValueError
            return func(*argv, **kwargs)
        return check_types
    return accepter