from flask import Flask,render_template,request,escape
from findinghistory import history
from findinggame import gamess
from hotel import lucky
from finding import find
from ticket_list import ticket
import csv


app = Flask(__name__)

"""谭怡颖"""
def log_request(req: 'flask_request') -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, file=log, sep='|')
     
@app.route('/profile',methods=['GET','POST'])
def do_search() -> 'html':
    content=[]
    with open("迪士尼人物.csv",encoding='gbk')as c:
        for para in csv.reader(c):
            content.append([])
            for line in para:
                content[-1].append(line)
    title = '以下是迪士尼人物的介绍:' 
    return render_template('profile.html',
                        the_title = title,
                        the_results = content
                        )

@app.route('/profile_results',methods=['POST','GET'])
def get_results() -> 'html':
    name = request.form['character']
    title = '迪士尼人物搜索结果'
    when = {}
    with open("迪士尼人物.csv",encoding='gbk') as data:
        for a,b in csv.reader(data):
            if a == name:
                when[a] = b
    return render_template('results_profile.html',
                           the_title=title,
                           the_name=name,
                           the_results=list(when.values()))

@app.route('/board',methods=['POST','GET'])
def message_aboard() -> 'html':
    return render_template('board.html',
                           
                           the_title='留言板')
                           
@app.route('/thanks',methods=['POST','GET'])
def thanks_page() -> 'html':
    messages = request.form['themessage']
    log_request(request)
    return render_template('thanks.html',
                           the_content= messages,
                           the_title='感谢您的留言！')                    

@app.route('/viewlog')
def viewlog()->str:
    data = []
    with open('vsearch.log') as log:
        for line in log:
            data.append([])
            for item in line.split('|'):
                data[-1].append(escape(item))
    titles = ('留言内容', 'Remote_addr', 'User_agent')
    return render_template('viewlog.html',
                           the_title='留言板信息',
                           the_row_titles=titles,
                           the_data=data,)

"""郭璐"""
@app.route('/history', methods=['POST','GET'])
def do_search_history() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    title = 'Here are your results:'
    results = history(phrase)
    titles5 = ('乐园')
    return render_template('viewhistory.html',
                           the_title='迪士尼乐园介绍',
                           the_row_titles5=titles5,
                           the_data=results,)

@app.route('/introduction')
def view_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('六大乐园.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(escape(item))
                
    contents1 = []
    with open('品牌文化.csv') as csv1:
        for line1 in csv1:
            contents1.append([])
            for item1 in line1.split(','):
                contents1[-1].append(escape(item1))
                
    contents2 = []
    with open('发展历程.csv') as csv2:
        for line2 in csv2:
            contents2.append([])
            for item2 in line2.split(','):
                contents2[-1].append(escape(item2))
                
    titles3 = ('文化', '介绍')
    titles2 = ('乐园', '介绍')
    titles4 = ('时间', '历程')
    return render_template('viewloghistory.html',
                            the_title2='六大乐园简介',
                            the_row_titles2=titles2,
                            the_data2=contents,
                           
                            the_title3='品牌文化',
                            the_row_titles3=titles3,
                            the_data3=contents1,

                            the_title4='发展历程',
                            the_row_titles4=titles4,
                            the_data4=contents2,)


"""张柳燕"""
@app.route('/game', methods=['POST','GET'])
def do_search_game() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    title = '迪士尼十大经典游戏:'
    results = gamess(phrase)
    titles = ('游戏名','游戏介绍')
    return render_template('view.html',
                        the_title='搜索结果',
                            the_title2 = '迪士尼十大经典游戏之一',
                           the_row_titles=titles,
                           the_data=results,)

@app.route('/games')
def game() -> 'html':
    information = []
    with open("迪士尼前十经典游戏.csv",encoding='utf-8') as data:
        for para1 in csv.reader(data):
            information.append([])
            for line1 in para1:
                information[-1].append(line1)
    titles = ('游戏名','游戏介绍')
    return render_template('games.html',
                        the_title = '迪士尼十大经典游戏',
                        the_title2 = '',
                        the_row_title = titles,
                        the_data = information,)

"""赖绮薇"""
@app.route('/ticket', methods=['POST','GET'])
def do_search_ticket() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    title = '迪士尼乐园门票:'
    results = ticket(phrase)
    titles = ('园区名称','所在国家','所在城市','门票类型','门票价格','购票须知')
    return render_template('tickets_view.html',
                           the_title='迪士尼乐园门票',
                           the_row_titles=titles,
                           the_data=results,)

@app.route('/tickets')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    information = []
    with open('ticketlist.csv',encoding = 'utf-8') as csv:
        for line in csv:
            information.append([])
            for item in line.split(','):
                information[-1].append(escape(item))
    titles = ('园区名称','所在国家','所在城市','门票类型','门票价格','购票须知')
    return render_template('tickets.html',
                           the_title = '全球迪士尼乐园门票清单',
                           the_row_titles=titles,
                           the_data=information,)


"""莫欣妹"""
@app.route('/beaty', methods=['POST','GET'])
def do_beaty() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    title = '迪士尼酒店搜索结果:'
    results = lucky(phrase)
    titles = ('酒店名称','地址','简介')
    return render_template('living.html',
                           the_title='迪士尼酒店搜索结果',
                           the_row_titles=titles,
                           the_data=results,)

@app.route('/hotel')
def hotel() -> 'html':
    contents = []
    with open("迪士尼酒店介绍.csv",encoding='gbk')as data:
        for para in csv.reader(data):
            contents.append([])
            for line in para:
                contents[-1].append(line)
    title = ('酒店名称','地址','简介') 
    return render_template('hotel.html',
                        the_row_title = title,
                        the_data = contents,)

"""黄舒静"""
@app.route('/classic', methods=['POST','GET'])
def do_search3() -> 'html':
    """Extract the posted data; perform the search; return results."""
    movie = request.form['movie']
    title = '搜索结果'
    results = find(movie)
    titles = ('影名','主演','编剧','主演','简介')
    return render_template('consequence.html',
                           the_title='搜索结果',
                           the_row_titles=titles,
                           the_data=results,)

@app.route('/movie')
def movie() -> 'html':
    information = []
    with open("迪士尼前十经典电影.csv",encoding='utf-8') as data:
        for para1 in csv.reader(data):
            information.append([])
            for line1 in para1:
                information[-1].append(line1)
    titles = ('影名','主演','编剧','主演','简介')
    return render_template('movie.html',
                        the_title = '迪士尼经典电影',
                        the_title2 = '电影清单',
                        the_row_title = titles,
                        the_data = information,)


@app.route('/') 
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html')


if __name__ == '__main__':
    app.run(debug=True)

