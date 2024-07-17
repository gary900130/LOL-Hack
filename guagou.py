import tkinter as tk
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from opencc import OpenCC

# 設置 OpenCC 轉換器
cc = OpenCC("s2t")  # 簡體到繁體

def get_liuyao():
    url = "https://p.china95.net/paipan/liuyao/liuyao.asp"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-TW,zh;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }

    # 獲取當前時間
    now = datetime.now()
    data = {
        "csyear": "2001",
        "mysex": "男",
        "whyarea": "0",
        "year": str(now.year),
        "month": str(now.month),
        "day": str(now.day),
        "hour": str(now.hour),
        "minute": str(now.minute),
        "mode": "1",
        "hanzi": "",
        "yinyang": "1",
        "upyao": "",
        "downyao": "",
        "dongyao": "1",
        "baosuo": "",
        "dongyao1": "1",
        "yao6": "1",
        "yao5": "1",
        "yao4": "1",
        "yao3": "1",
        "yao2": "1",
        "yao1": "1",
        "ok": "确定",
    }

    response = requests.post(url, headers=headers, data=data)
    response.encoding = "gbk"
    soup = BeautifulSoup(response.text, "html.parser")

    decision = soup.find(text=lambda text: text and "决策：" in text)
    zhouyi = soup.find("font", text=lambda text: text and "《周易》" in text)
    explanation = soup.find(text=lambda text: text and "这个卦" in text)

    result = ""
    if zhouyi:
        result += "周易:\n" + cc.convert(zhouyi.text.strip()) + "\n\n"
    if explanation:
        result += "解釋:\n" + cc.convert(explanation.strip()) + "\n\n"
    if decision:
        result += cc.convert(decision.strip())

    return result

def update_result():
    result = get_liuyao()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# 創建主窗口
root = tk.Tk()
root.title("六爻占卜")
root.geometry("800x600")

# 創建並放置按鈕
update_button = tk.Button(root, text="獲取六爻占卜結果", command=update_result, font=('DFKai-SB', 24))
update_button.pack(pady=10)

# 創建文本框
result_text = tk.Text(root, wrap=tk.WORD, width=70, height=20, font=('DFKai-SB', 24))
result_text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# 運行主循環
root.mainloop()
