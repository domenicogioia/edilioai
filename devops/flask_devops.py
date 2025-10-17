from flask import Flask, jsonify
import os
app = Flask(__name__)

@app.route("/github_pull_request_443221285869_edilioai", methods = ['GET', 'POST'])
def git_pull():
    os.system('git reset --hard')
    os.system('git pull')
    # riavvio gunicorn
    # os.system('docker exec ubuntu fuser -k -HUP 5000/tcp')

    # riavvio flask
    # os.system('docker exec ubuntu tmux send-keys -t flask C-c')     # ctr+c
    # os.system('docker exec ubuntu tmux send-keys -t flask Up')      # freccai su
    # os.system('docker exec ubuntu tmux send-keys -t flask Enter')   # invio
    return jsonify(dict(outcome="Ok"))

    # docker exec ubuntu fuser -k -HUP 5000/tcp


if __name__ == '__main__':
    # print(app.url_map)
    app.run(debug=False, port=5151, host='0.0.0.0')