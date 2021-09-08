from flask import Flask
app=Flask(__name__)
@app.route('/')
def test():
    return "你好，flask."
if __name__=='__main__':
    app.run()