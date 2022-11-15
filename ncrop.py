import datetime
import time
import gdal


def date_cunt(datetime1):
    """输入一个日期，判断是今年的第多少天"""
    date01 = time.mktime(time.strptime(datetime1[:4] + "0101", "%Y%m%d"))
    date02 = time.mktime(time.strptime(datetime1, "%Y%m%d"))
    cnt = (date02 - date01) / 60 / 60 / 24 + 1
    return cnt


def level(date):
    cunt = date_cunt(date)
    if cunt < 141 or cunt > 253:
        return None
    if 171 <= cunt:
        return 'FNQ'  # 分蘖期
    if 176 <= cunt:
        return 'YSFHQ'  # 幼穗分化期
    if 196 <= cunt:
        return 'BJQ'  # 拔节期
    if 206 <= cunt:
        return 'YSQ'  # 孕穗期
    if 222 <= cunt:
        return 'CSQ'  # 抽穗期
    if 253 <= cunt:
        return 'GJQ'  # 灌浆期


def appendN(date, spadtif):
    SQ = level(date)
    if SQ:
        if SQ == 'FNQ' or SQ == 'YSFHQ':
            rat = open(spadtif)
            band = rat.ReadAsArray()
            band1 = band[band > 32 and band < 35]
            # 遍历栅格SPAD数据，将大于32小于35的像元地块追加施肥，其他不符合像元施肥设置为0
            appendN_1 = (band1 - 32) * 1 + 30
            ds_tif = gdal.Create()
        elif SQ == 'BJQ':
            # SPAD 35-40
            # N 45-75
            pass
        elif SQ == 'YSQ':
            # SPAD 40-45
            # N 15-30
            pass
