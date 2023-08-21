import tomllib
import threading

from application import config
from application import mysql
from error import exception


class Application:
    """
    服务启动的全局应用，实现了单例模式，仅能初始化一次。
    存储了启动时的命令行参数以及加载的整个配置
    """

    config = None
    mysql = None
    projectPath = None
    env = None
    model = None
    command = None
    configPath = None
    __instance = None
    __lock = threading.RLock()

    def __new__(cls, projectPath, env, model, command, configPath, *args, **kwargs):
        if cls.__instance:
            return cls.__instance

        with cls.__lock:
            if not cls.__instance:
                cls.__instance = super().__new__(cls, *args, **kwargs)
                cls.projectPath = projectPath
                cls.env = env
                cls.model = model
                cls.command = command
                cls.configPath = configPath

                # 基于环境变量，加载全局配置
                with open(configPath, mode="rb") as handle:
                    configDict = tomllib.load(handle).get(env)
                    if not configDict:
                        raise exception.ErrorConfigEnvNotFind
                    cls.config = config.Config(**configDict)

                # 注册mysql连接池对象
                cls.mysql = mysql.ConnectionPool()
            return cls.__instance

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            raise exception.ErrorApplicationNotInit
        return cls.__instance
