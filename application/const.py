import sys


class _const:
    """
    自定义常量类
    该类定义了一个方法__setattr()__, 通过调用类自带的字典__dict__, 判断定义的常量是否包含在字典
    中。如果字典中包含此变量，将抛出异常，否则，给新创建的常量赋值。
    """

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value


# 将当前代码归入到module中使用，当其他模块import当前模块时，将获取一个指向_const的实例
sys.modules[__name__] = _const()
