from configparser import ConfigParser

cfg = ConfigParser()
cfg_file = "config.ini"
"""创建实例预读config.ini文件"""
# cfg.read("config.ini")
cfg.read(cfg_file)

"""ini文件中的段落"""
print(cfg.sections())

"""取init下的workspace"""
print(cfg.get("init", "workspace"))

"""设值"""
cfg.set("init", "workspace", "aa")

"""写入"""
# cfg.write(open("config.ini", "w"))