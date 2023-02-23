import logging


def init_logger(name, level, filename, fh_level):
    # 创建日志收集器
    log = logging.getLogger(name)
    # 设置日志收集器的等级
    log.setLevel(level)
    # 设置日志输出渠道
    fh = logging.FileHandler(filename, 'a+', encoding='utf-8')
    # 设置输出渠道的日志等级
    fh.setLevel(fh_level)
    # 绑定输出渠道到日志收集器
    log.addHandler(fh)
    # 设置日志输出渠道到控制台
    sh = logging.StreamHandler()
    sh.setLevel(level)
    log.addHandler(sh)
    log_format = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[%(lineno)d]>>>%(message)s')
    fh.setFormatter(log_format)
    sh.setFormatter(log_format)
    return log
