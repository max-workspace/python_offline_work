import controller
from application import app


class HelloWorld(controller.abstractController, controller.baseController):
    """
    hello world
    必须实现抽象类controller.abstractController
    必须继承父类controller.baseController
    """

    def __init__(self):
        """
        初始化函数
        必须执行父类的初始化函数，第一个参数为模块名称，第二个参数为当前脚本所需的配置路径
        """
        super().__init__(self.__class__.__name__, "./config/hello_world.toml")

    def handle(self):
        print("HelloWorld handle start")
        self.log.info("HelloWorld handle")
        print(self.config.label.a)
        print(app.Application.getInstance().mysql.test)

        print("HelloWorld handle end")


if __name__ == "__main__":
    print("HelloWorld")
    c = HelloWorld()
    c.handle()
