import ollama
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        question = request.form['question']
        
        # Ollama modeline soruyu gönderiyoruz
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": question + " bir tur rehberi gibi cevaplamalısın."}])
        
        # Gelen cevabı yazdıralım (debug için)
        print(response)

        # Cevabın yapısına göre doğru alandaki veriyi çekelim
        if 'content' in response:
            answer = response['content']  # Gelen cevabı alıyoruz
        else:
            answer = response
            
    return render_template('index.html', answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
