import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root123@realmcluster.jkwav.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.member_system
print("資料庫連線建立成功！")

# 初始化 Flask 伺服器
from flask import *
app = Flask(__name__, static_folder = "public", static_url_path = "/")
app.secret_key = "any string but secret"

# 首頁
@app.route("/")
def index():
    return render_template("index.html")

# 會員頁面
@app.route("/member")
def member():
    # 判斷nickname有無在session裡有無紀錄
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

# 錯誤訊息頁面, /error?msg=錯誤訊息
@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤！請聯繫客服")
    return render_template("error.html", message = message)

# 建立signup路由,檢查註冊訓資訊是否已被註冊過
@app.route("/signup", methods = ["POST"])
def signup():
    # 從前端接收資料
    nickname = request.form["nickname"]
    email = request.form["email"]
    password = request.form["password"]
    # 根據接收的資料和資料庫互動
    collection = db.user
    # 檢查是否有相同email的文件資料
    result = collection.find_one({
        "email":email
    })
    if result != None:
        return redirect("/error?msg=信箱已被註冊過！")
    # 把資料放進資料庫完成註冊
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })
    return redirect("/")

# 登入
@app.route("/signin", methods = ["POST"])
def signin():
    # 從前端取得使用者輸入
    email = request.form["email"]
    password = request.form["password"]
    # 和資料庫互動
    collection = db.user
    # 檢查信箱密碼是否正確
    result = collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    # 登入失敗導向到錯誤頁面
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤！")
    # 登入成功, 導向到會員頁面
    session["nickname"] = result["nickname"]
    return redirect("/member")

# 登出
@app.route("/signout")
def signout():
    # 移除session中的會員資訊
    del session["nickname"]
    return redirect("/")

app.run(port = 3000)
