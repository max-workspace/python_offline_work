from error import exception
import controller

# 自动加载入口，限制只能从特定入口加载使用
__launchBaseModuleName = "controller"
__launchFunctionName = "handle"


def commandModel(command):
    """
    通过命令行方式启动
    """
    moduleName, className = command.split("-", 1)
    # 检测要执行的模块是否是允许的路径
    if not moduleName.startswith(__launchBaseModuleName):
        raise exception.ErrorLaunchModuleNotAllow

    # 获取最终实际要加载的模块
    moduleNameList = moduleName.split(".")
    lastModuleName = moduleNameList.pop()

    # 加载要执行的模块
    module = __import__(moduleName, fromlist=[lastModuleName])
    if not hasattr(module, className):
        raise exception.ErrorLaunchClassNotFind

    # 检测要执行的类是否符合预期
    classInstance = getattr(module, className)
    if not issubclass(classInstance, controller.baseController):
        raise exception.ErrorLaunchClassNotConform
    if not issubclass(classInstance, controller.abstractController):
        raise exception.ErrorLaunchClassNotConform

    # 执行
    obj = classInstance()
    obj.execute(obj)


def crontabModel():
    """
    通过定时任务方式启动
    """
    pass
