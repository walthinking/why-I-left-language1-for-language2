from flask import Flask
from wuliao import template_format, read_helloworld, read_template
from wuliao import CURRENT_DIR

app = Flask(__name__)


@app.route('/')
def index():
    return _why()


@app.route('/why-I-left-<lan1>-for-<lan2>')
def why(lan1='Java', lan2='Python'):
    return _why(lan1, lan2)


def _why(lan1='Java', lan2='Python'):
    title = 'Why I left %s for %s' % (lan1, lan2)
    t = '''<html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet"
    href="http://guojing.me/style/qiajigou.css"
    type="text/css">
    <title>why I left {lan1} for {lan2}</title>
    <meta content="{title}" name="description"/>
    <meta content="Programming,Language,Choice" name="keywords"/>
    <meta property="og:type" content="article" />
    <meta property="og:url" content="/why-I-left-{lan1}-for-{lan2}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="This is {title}" />
    </head>
    <body>
    <div class="container" style="margin: 0px auto">
        <div class="main clearfix">
            <div class="title">
            {title}
            </div>
            <div class="content">
            {fmt}
            </div>
        </div>
    </div>
    </body>
    </html>
    '''
    tmp = CURRENT_DIR + '/templates/en/article.html'
    template = read_template(tmp)
    hello1 = read_helloworld(lan1)
    hello2 = read_helloworld(lan2)
    fmt = template_format(
        template=template,
        language0='C',
        language1=lan1,
        language2=lan2,
        language1_hello_world=hello1,
        language2_hello_world=hello2,
        language3='Python3',
        project_names=', '.join(['Spring MVC, Tomcat'])
    )
    return t.format(lan1=lan1, lan2=lan2, fmt=fmt, title=title)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
