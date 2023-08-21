import threading
import pymysql
from pymysql import cursors
from dbutils.pooled_db import PooledDB
from application import app


class ConnectionPool:
    """
    mysql的连接池
    采用赖加载并保证每个数据库配置只对应一个连接池单例
    """

    __lock = threading.RLock()

    def __getattr__(self, name):
        print("__getattr__", name)
        # 加锁
        with ConnectionPool.__lock:
            # 通过全局对象配置查找对应db配置
            mysqlConfig = app.Application.getInstance().config.mysql
            detailConfig = getattr(mysqlConfig, name)
            # 基于配置生成db连接池对象，并为对应属性进行赋值
            self.__dict__[name] = PooledDB(
                creator=pymysql,
                maxconnections=detailConfig.maxconnections,
                mincached=detailConfig.mincached,
                maxcached=detailConfig.maxcached,
                maxshared=detailConfig.maxshared,
                blocking=detailConfig.blocking,
                maxusage=None,
                setsession=detailConfig.setsession,
                ping=detailConfig.ping,
                host=detailConfig.host,
                port=detailConfig.port,
                user=detailConfig.user,
                passwd=detailConfig.passwd,
                database=detailConfig.database,
                charset=detailConfig.charset,
                cursorclass=cursors.DictCursor,
            )
        return self.__dict__[name]

    def __setattr__(self, name, value):
        """
        设置类属性方法
        设置前检测当前类属性是否存在，如果存在设置无效
        """
        # 检测对应属性是否存在
        if name in self.__dict__:
            return
        self.__dict__[name] = value
