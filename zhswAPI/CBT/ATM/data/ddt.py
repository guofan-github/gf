def data(params):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            if isinstance(params, list):
                for p in params:
                    pm = list(args)
                    pm.extend(p)
                    fun(*pm, **kwargs)
            else:
                pm = list(args)
                pm.extend(params)
                fun(*pm, **kwargs)
        return wrapper
    return decorator

