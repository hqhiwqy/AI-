class HtmlOutputer:
    """网页输出器"""

    def __init__(self):
        self.data = []

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        with open('output2.html', 'w', encoding='utf-8') as f:
            f.write("<html>")
            f.write("<head>")
            f.write("<title>爬取百度百科的1000个页面</title>")
            f.write("<meta charset='utf-8' />")
            f.write("</head>")
            f.write("<body>")
            f.write("<table>")
            for value in self.data:
                f.write("<tr>")
                f.write("<td><a href='{}' target='_blank'>{}</a></td>".format(value['url'], value['title']))
                f.write("<td>{}</td>".format(value['summary']))
            f.write("</body>")
            f.write("</table>")
            f.write("</html>")