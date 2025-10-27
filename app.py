from flask import Flask, jsonify
#                               flask:Flask框架的主类，用于创建Web应用实例
#                               jsonify:用于将Python字典转换为JSON格式的HTTP响应
app = Flask(__name__)
#                               app:创建Flask应用实例，__name__参数用于确定应用的根路径
@app.route("/")#                定义路由装饰器，指定URL路径和处理函数
def home():
    return jsonify(message="Hello Flask + GitHub!")

if __name__ == "__main__":#     直接运行此脚本时__name__=main，当被导入为模块时=模块名
    app.run(debug=True)   #     app.run()：启动内置的Web服务器；debug=True启用调试模式，便于开发时调试错误