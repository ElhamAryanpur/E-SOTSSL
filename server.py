from flask import Flask, request
import file_ext
from os import environ

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():

    data = request.data
    data = data.decode('utf-8')

    f = file_ext.FileStuff()
    f.level = 38245
    salt = f.encrypt_salt("Suck on this!5")
    data = f.decrypt_string(salt, data)
    
    if "<" in data:
        n = 0
        start_and_end = []
        while True:
            if n >= len(data):
                break
            else:
                if data[n] == "<":
                    start_and_end.append(n + 1)
                    n += 1
                if data[n] == ">":
                    start_and_end.append(n)
                    n += 1
                else:
                    n += 1
        
        seed = data[start_and_end[0]:start_and_end[1]]
        to_delete = "<" + seed + ">"
        data = str(data).replace(to_delete, "")
        seed = str(seed).split()
        f.level = int(seed[0])
        salt = f.encrypt_salt(seed[1])
        data = f.decrypt_string(salt, str(data))

        path = seed
        del path[0]
        del path[0]
        path = "".join(path)

        with open(str(path), "w") as f:
            f.write(data)

        return "SUCCESS!"

    else:
        print("FILE HAS NOT BEEN SENT BY E-SOTSSL!")

    return "SUCCESSFUL!"

if __name__ == "__main__":
    environ['WERKZEUG_RUN_MAIN'] = 'true'
    app.run()