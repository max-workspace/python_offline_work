import tomllib
from abc import ABC, abstractmethod
from error import exception
from application import config
from loguru import logger
from application import app


class abstractController(ABC):
    @abstractmethod
    def handle(self):
        pass


class baseController:
    def __init__(self, command, configPath):
        self.config = None
        self.log = None
        self.command = command
        self.configPath = configPath

    def loadConfig(self):
        # 配置路径不存在时，不加载配置
        if not self.configPath:
            return

        # 加载配置
        with open(self.configPath, mode="rb") as handle:
            configDict = tomllib.load(handle)
            if not configDict:
                raise exception.ErrorConfigEnvNotFind
            self.config = config.Config(**configDict)

    def initLog(self):
        path = (
            app.Application.getInstance().projectPath + "/log/" + self.command + ".log"
        )
        logName = self.command
        self.log = logger.bind(name=logName)

        self.log.add(
            path,
            filter=lambda record: record["extra"]["name"] == logName,
            encoding="utf-8",
            rotation="500MB",
        )
        self.log.info("log init")

    def execute(self, c):
        # 加载具体命令所需的配置
        c.loadConfig()

        # 初始化当前命令日志对象
        c.initLog()

        # 执行实际逻辑
        c.handle()
