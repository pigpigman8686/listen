from flask import Flask,request,render_template,redirect,url_for,flash
from flask import request
from flask import jsonify
from db import *
from function import *
import re


app = Flask(__name__,static_url_path='')


@app.route("/index",methods=['GET','POST'])
def index():
    if request.method == 'POST' and request.form.get('button') == '问卷':
        id = add_user(request.form.get('name'),int(request.form.get('age')),request.form.get('sex'))
        return redirect(url_for('question',id=id))
    elif request.method == 'POST' and request.form.get('button') == '提交':
        id = add_user(request.form.get('name'),int(request.form.get('age')),request.form.get('sex'))
        return redirect(url_for('test',id=id))
    else:
        return render_template('index.html')

@app.route("/question/<id>",methods=['GET','POST'])
def question(id):
    if request.method == 'POST':
        print(type(request.form))
        #add_question()
        return redirect(url_for('test',id))
    else:
        return render_template('question.html',id=id)

@app.route("/test/<id>",methods=['GET','POST'])
def test(id):
    if request.method == 'POST':#此处修改为直接操纵数据库记录每一次测试结果
        #------------------------------------------------------#
        #截取文件名信息，right.group(1)为正确数字，right.group(2)为信噪比
        patten = re.compile('(\d{1,})-(\d{1,})')
        right = re.search(patten,request.form.get('message'))
        #print("right:"+right.group(1))
        #------------------------------------------------------#
        count = int(request.form.get('count'))#获取count
        if int(request.form.get('count')) == int(right.group(1)):#看答案是否正确
            message = getMessage(True,int(right.group(2)),count)
        else:
            message = getMessage(False,int(right.group(2)),count)
        #------------------------------------------------------#
        #选择进行下一次测试
        count = count+1
        if count>24:
            return redirect(url_for('end',id=id))
        if count>5:
            right_ans = str(right.group(1))+"-"+str(right.group(2))
            add_test(id,right_ans,request.form.get('ans'),count-5) 
        return render_template('test.html',message=message,count=count,id=id)#顺序不要变，就放这里。很坑= =
        #------------------------------------------------------#
    else:
        message = getMessage()#用来获取每次要播放的音频信息，格式为voice\\page\\音频名称
        return render_template('test.html',message=message,count=1,id=id)

@app.route("/end/<id>",methods=['GET','POST'])
def end(id):
    result = getResult(id)
    snr = average(result)
    print(snr)
    return render_template('end.html',snr=snr)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)