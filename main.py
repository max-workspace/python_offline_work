import os
import argparse
import traceback
import application.launch as launch
from application import app


# 整个项目启动入口
def main():
    """
    整个程序的入口函数
    解析命令行参数
    加载全局配置
    通过命令行参数选择启动模式
    """
    try:
        # 解析命令行参数
        parser = argparse.ArgumentParser(description="命令行参数")
        parser.add_argument(
            "--env",
            "-e",
            type=str,
            help="项目启动配置环境，非必须参数，online表示线上环境，dev表示开发环境，默认值为开发环境",
            default="dev",
        )
        parser.add_argument(
            "--model",
            "-m",
            type=str,
            help="项目启动模式，非必须参数，command表示命令行模式，crontab表示定时任务模式，默认值为令行模式",
            default="command",
        )
        parser.add_argument(
            "--command",
            "-cmd",
            type=str,
            help="命令行模式下要执行的命令，格式为 模块-类名",
            default="",
        )
        args = parser.parse_args()

        projectPath = os.path.dirname(os.path.realpath(__file__))

        # 初始化应用
        app.Application(
            projectPath, args.env, args.model, args.command, "./config/application.toml"
        )

        # 根据执行模式进行启动执行
        if args.model == "command":
            launch.commandModel(args.command)

        if args.model == "crontab":
            launch.crontabModel()
    except Exception as e:
        print("execute exception:%s" % e)
        traceback.print_exc()


if __name__ == "__main__":
    main()
