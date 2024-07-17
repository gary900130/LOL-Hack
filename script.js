// 注意：這段代碼需要在支持 ES6 的瀏覽器環境中運行

// 引入 axios（假設你已經在 HTML 中引入了 axios）
// <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

// 獲取當前時間
const now = new Date();

// 準備請求數據
const url = "https://p.china95.net/paipan/liuyao/liuyao.asp";
const headers = {
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "accept-language": "zh-TW,zh;q=0.9,en;q=0.8",
  "content-type": "application/x-www-form-urlencoded",
};
const data = new URLSearchParams({
  "csyear": "2001",
  "mysex": "男",
  "whyarea": "0",
  "year": now.getFullYear().toString(),
  "month": (now.getMonth() + 1).toString(),
  "day": now.getDate().toString(),
  "hour": now.getHours().toString(),
  "minute": now.getMinutes().toString(),
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
});

// 發送請求並處理響應
axios.post(url, data, { headers })
  .then(response => {
    // 使用 DOMParser 解析 HTML
    const parser = new DOMParser();
    const doc = parser.parseFromString(response.data, 'text/html');

    // 尋找並提取所需信息
    const decision = doc.evaluate('//text()[contains(., "决策：")]', doc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    const zhouyi = doc.evaluate('//font[contains(text(), "《周易》")]', doc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    const explanation = doc.evaluate('//text()[contains(., "这个卦")]', doc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

    // 輸出結果
    if (decision) {
      console.log("決策:");
      console.log(decision.textContent.trim());
      console.log();
    }
    if (zhouyi) {
      console.log("周易:");
      console.log(zhouyi.textContent.trim());
      console.log();
    }
    if (explanation) {
      console.log("解釋:");
      console.log(explanation.textContent.trim());
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });