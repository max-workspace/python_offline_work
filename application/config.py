class Config:
    """
    配置类
    将外部读取的dict转化为类属性
    类属性为只读性质，禁止外部修改配置类属性
    """

    def __init__(self, **kwargs):
        """
        将外部dict转化为配置类属性
        """
        for key, value in kwargs.items():
            if isinstance(value, dict):
                self.__dict__[key] = Config(**value)
            else:
                self.__dict__[key] = value

    def __setattr__(self, name, value):
        """
        设置配置类为只读属性，防止外部修改配置类属性
        """
        pass
