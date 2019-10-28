from flask import Flask, escape, request,make_response

import podcast
app = Flask(__name__)

@app.route('/feed.rss')
def root():
    response = make_response(podcast.podcast())
    response.headers['Content-Type'] = 'application/rss+xml'
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
