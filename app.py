import glob
import tarfile
import io
import os
from flask import Flask,send_file
app = Flask(__name__)

@app.route("/")
def index():
    files = [(f,io.BytesIO(open(f,'rb').read())) for f in glob.glob('./images/*')]

    file_like_object = io.BytesIO()
    with tarfile.open(fileobj=file_like_object,mode='w|gz') as tar:
        for k,v in files:
            tar.addfile(tarfile.TarInfo(os.path.basename(k)),v)
    file_like_object.seek(0)
    
    return send_file( file_like_object,attachment_filename='archive.tar.gz',as_attachment=True)