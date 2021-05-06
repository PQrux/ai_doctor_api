import os
import string
import random
import subprocess
from flask import Flask, request, abort

SIMPLES_UPLOAD_FOLDER = "/tmp/"
ALLOWED_EXTENSIONS = {"png"}

def gen_file_id():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route('/captchasimples', methods=['GET', 'POST'])
def captchasimples():
    if request.method == 'POST':
        if 'file' not in request.files:
            abort(400, {"message": 'Sem arquivos!'})
        file = request.files['file']
        if file.filename == '':
            abort(400, {"message": 'Nenhum arquivo selecionado!'})
        ext = file.filename.rsplit('.', 1)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            abort(400, {"message": 'Tipo de arquivo inválido!'})
        filepath = os.path.join(SIMPLES_UPLOAD_FOLDER, gen_file_id() + ".png")
        file.save(filepath)
        rst = subprocess.run(['Rscript', '-e', 'decryptr::decrypt("'+filepath+'", "rfb")'], stdout=subprocess.PIPE)
        os.remove(filepath)
        return {"result": rst.stdout.decode('utf-8')}
    else:
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
        '''

@app.route('/')
def hello_world():
    return {"message": "Bem-vindo! Acesse /captchasimples para começar!"}




app.run(host='0.0.0.0', port=5000, use_reloader=True)