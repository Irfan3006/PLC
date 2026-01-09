from flask import Flask, render_template, request, jsonify, abort
import os


if os.getenv("MAINTENANCE_MODE") == "true":
    abort(503)

app = Flask(__name__, template_folder='../templates', static_folder='../static')

mapping = {
    "A": "da778688000ji", "B": "ic7575729344jktk", "C": "c7668682048dr", "D": "hi7940149875ah",
    "E": "ng7833173256ja", "F": "an7495014493jb", "G": "go8108486729rgrpkt", "H": "ll7880599000spj",
    "I": "io7988005999bf", "J": "va7940149875jg", "K": "in8132727331ab", "L": "sp7506509912jm",
    "M": "ab7809531904cm", "N": "im8096384512ar", "O": "ml7952095936xl", "P": "on7868724669gvr",
    "Q": "rp20178205738913mr", "R": "by7940149875ym", "S": "ft8169178744cl", "T": "pt8144865728ah",
    "U": "da7988005999dm", "V": "v8230172859am", "W": "ly8181353375wc", "X": "ry8036054027mk",
    "Y": "ck7952095936dhm", "Z": "ig8193540096ak", "0": "ar8108486729mhab", "1": "ct8157016197jw",
    "2": "ue8169178744ey", "3": "te8193540096rh", "4": "er8132727331yktd", "5": "ne8120601000ja",
    "6": "ry8072216216jr", "7": "ap8132727331mojt", "8": "xt8193540096gr", "9": "id8217949832rc",
}

reverse_mapping = {v: k for k, v in mapping.items()}

def run_encrypt(text):
    text = text.upper()
    parts = []
    for ch in text:
        if ch in mapping:
            parts.append(mapping[ch])
        else:
            parts.append(ch) 
    ciphertext = "".join(parts)
    return ciphertext[::-1]

def run_decrypt(ciphertext):
    
    ciphertext = ciphertext[::-1].lower() 
    result = []
    i = 0
    
    max_iter = len(ciphertext) * 2
    count = 0

    while i < len(ciphertext):
        match = False
        count += 1
        if count > max_iter: break 

        for code, letter in reverse_mapping.items():
            if ciphertext.startswith(code, i):
                result.append(letter)
                i += len(code)
                match = True
                break
        
        if not match:
            
            i += 1 
            
    if not result:
        return "Tidak ditemukan pola yang cocok"
        
    return "".join(result)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    text = data.get('text', '')
    mode = data.get('mode', 'encrypt')
    
    if not text:
        return jsonify({'result': ''})

    if mode == 'encrypt':
        result = run_encrypt(text)
    else:
        result = run_decrypt(text)
        
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)