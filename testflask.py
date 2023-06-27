import html
from flask import Flask,  render_template, request, escape
from vsearch import searchForletters

app = Flask (__name__)

 

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log: #open a log file called vsearch_log
       #print(str(dir(req)), res, file=log) # print vals req $ res in file display as log 
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
       

@app.route('/search4', methods=['POST']) #decorator identify function as POST
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'here the result human'
    results = str (searchForletters(phrase, letters))
    log_request(request, results)
    return render_template(
        'result.html',
        the_phrase = phrase,
        the_letters = letters,
        the_title = title,
        the_results = results, 

    )
@app.route('/') #     return redirect('/entry') #redirect to entry / '302': #if 302
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!') #call and render the_tittle value on page

@app.route('/viewlog')
def view_logs() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
        titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
    the_title='View Log',
    the_row_titles=titles,
    the_data=contents,)
        #return escape(contents) # can use escape keyword to view all logs without newline

if __name__ == '__main__':
    app.run(debug=True)

