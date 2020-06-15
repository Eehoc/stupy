import requests
try:
    kv={"User-Agent": "Mozilla/5.0"}
    r=requests.get("http://119.36.33.158/mv.music.tc.qq.com/ACLdjBPhBr5OhsLgHoTrLhGrvBZvOEKy0fAj-Tp-uYPg/BC6ABC8DD1EB00252F6106844025D9C672F6F9EDE559658687F40FA091D009B8BD92F10ADD49B47DB62E1A0A03CE97F1ZZqqmusic_default/1049_M0140900000UP9mZ3FYPHY1001607265.f40.mp4?fname=1049_M0140900000UP9mZ3FYPHY1001607265.f40.mp4",headers=kv)
    print(r.status_code)
    r.raise_for_status()
    path="D:\\kokobop-mv.mp4"
    with open(path,"wb") as f:
        f.write(r.content)
    print("爬取成功")
except:
    print("爬取失败")