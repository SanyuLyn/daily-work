#!/usr/bin/env python3
# 每交易日抓 A股 ETF 真实收盘价，写 investment/prices.json。
# 设计：在 GitHub Actions(有外网)里跑；云端 CCR 投资日报只读产物 prices.json。
# 零第三方依赖(仅标准库 urllib)。Yahoo 主源(US runner 直连稳) + 东财/腾讯兜底。
import json, os, sys, urllib.request
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
HERE = os.path.dirname(os.path.abspath(__file__))
PRICES = os.path.join(HERE, "prices.json")
PORT = os.path.join(HERE, "portfolio.json")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

def _get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def market(code):
    return "SS" if code[0] in "56" else "SZ"   # 沪 5/6，深 0/1/3

def from_yahoo(code):
    tk = f"{code}.{market(code)}"
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{tk}?range=5d&interval=1d"
    res = json.loads(_get(url))["chart"]["result"][0]
    ts, closes = res["timestamp"], res["indicators"]["quote"][0]["close"]
    for i in range(len(closes) - 1, -1, -1):        # 取最后一个非 null 收盘
        if closes[i] is not None:
            day = datetime.fromtimestamp(ts[i], CST).strftime("%Y-%m-%d")
            return round(float(closes[i]), 3), day, "yahoo"
    raise ValueError("yahoo: 无有效收盘")

def from_eastmoney(code):
    secid = f"{'1' if market(code) == 'SS' else '0'}.{code}"
    beg = (datetime.now(CST) - timedelta(days=12)).strftime("%Y%m%d")
    end = datetime.now(CST).strftime("%Y%m%d")
    url = (f"https://push2his.eastmoney.com/api/qt/stock/kline/get?secid={secid}"
           f"&fields1=f1&fields2=f51,f53&klt=101&fqt=0&beg={beg}&end={end}")
    kl = json.loads(_get(url))["data"]["klines"]
    if not kl:
        raise ValueError("eastmoney: klines 为空")
    day, close = kl[-1].split(",")[:2]
    return round(float(close), 3), day, "eastmoney"

def from_tencent(code):
    q = ("sh" if market(code) == "SS" else "sz") + code
    parts = _get(f"https://qt.gtimg.cn/q={q}").split("~")
    return round(float(parts[3]), 3), datetime.now(CST).strftime("%Y-%m-%d"), "tencent"

def fetch(code):
    errs = []
    for fn in (from_yahoo, from_eastmoney, from_tencent):
        try:
            return fn(code)
        except Exception as e:               # noqa: BLE001
            errs.append(f"{fn.__name__}={e}")
    raise RuntimeError(f"{code} 全部源失败: {' | '.join(errs)}")

def symbols():
    codes = {"588000", "159625", "518880"}   # 当前持仓 + 黄金候选
    try:
        for pos in json.load(open(PORT, encoding="utf-8")).get("positions", []):
            if pos.get("code"):
                codes.add(str(pos["code"]))
    except Exception:
        pass
    return sorted(codes)

def main():
    prev = {}
    try:
        prev = json.load(open(PRICES, encoding="utf-8")).get("prices", {})
    except Exception:
        pass
    out = {"prices": {}}
    for code in symbols():
        try:
            close, day, src = fetch(code)
            out["prices"][code] = {"close": close, "date": day, "source": src}
            print(f"{code}: {close} ({day}, {src})")
        except Exception as e:               # noqa: BLE001
            print(f"[WARN] {e}", file=sys.stderr)
            if code in prev:                 # 抓不到就沿用旧值并标 stale
                old = dict(prev[code]); old["stale"] = True
                out["prices"][code] = old
    dates = [v["date"] for v in out["prices"].values() if not v.get("stale")]
    out["trading_date"] = max(dates) if dates else datetime.now(CST).strftime("%Y-%m-%d")
    out["updated_at"] = datetime.now(CST).strftime("%Y-%m-%d %H:%M:%S %z")
    json.dump(out, open(PRICES, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {PRICES} | trading_date={out['trading_date']}")

if __name__ == "__main__":
    main()
