from flask import Flask, render_template, request, redirect,url_for,jsonify
import os
from google.cloud import speech_v1p1beta1 as speech
import difflib


app = Flask(__name__)


# Google Speech to Text API 설정
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\still-primer-406515-9e17e40c8c06.json"
client = speech.SpeechClient()





# 음성 인식 함수
def transcribe_speech(audio_file):
    with open(audio_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ko-KR'
    )


    response = client.recognize(config=config, audio=audio)


    for result in response.results:
        return result.alternatives[0].transcript

# 초기 화면
@app.route('/')
def first():
    return render_template('first.html')

# 프론트앤드에서 {{ url_for('second') }}가 /second URL을 생성, /second URL 를 받은 백앤드가 second.html 로 이동
@app.route('/second')
def second():
    return render_template('second.html')



@app.route('/third_coffee')
def third_coffee():
    return render_template('third_coffee.html')

@app.route('/third_tea')
def third_tea():
    return render_template('third_tea.html')

@app.route('/third_beverage')
def third_beverage():
    return render_template('third_beverage.html')



@app.route('/third_beverage1')
def third_beverage1():
    return render_template('third_beverage1.html')

@app.route('/third_beverage2')
def third_beverage2():
    return render_template('third_beverage2.html')

@app.route('/third_beverage3')
def third_beverage3():
    return render_template('third_beverage3.html')

@app.route('/third_beverage4')
def third_beverage4():
    return render_template('third_beverage4.html')

@app.route('/third_beverage5')
def third_beverage5():
    return render_template('third_beverage5.html')

@app.route('/third_tea1')
def third_tea1():
    return render_template('third_tea1.html')

@app.route('/third_tea2')
def third_tea2():
    return render_template('third_tea2.html')

@app.route('/third_tea3')
def third_tea3():
    return render_template('third_tea3.html')

@app.route('/third_tea4')
def third_tea4():
    return render_template('third_tea4.html')

@app.route('/third_tea5')
def third_tea5():
    return render_template('third_tea5.html')

@app.route('/third_coffee1')
def third_coffee1():
    return render_template('third_coffee1.html')

@app.route('/third_coffee2')
def third_coffee2():
    return render_template('third_coffee2.html')

@app.route('/third_coffee3')
def third_coffee3():
    return render_template('third_coffee3.html')

@app.route('/third_coffee4')
def third_coffee4():
    return render_template('third_coffee4.html')

@app.route('/third_coffee5')
def third_coffee5():
    return render_template('third_coffee5.html')

@app.route('/fourth')
def fourth():
    return render_template('fourth.html')

@app.route('/fifth')
def fifth():
    return render_template('fifth.html')

@app.route('/sixth')
def sixth():
    return render_template('sixth.html')

@app.route('/seventh')
def seventh():
    return render_template('seventh.html')



# <막힌 부분> : 음성으로 '커피' 인식 받아서 다음 페이지로 넘어가는 함수
@app.route('/order/coffee_type', methods=['GET', 'POST'])
def choose_coffee_type():
    if request.method == 'POST':
        if 'voice_input' in request.files:
            voice_file = request.files['voice_input']
            voice_file.save('user_audio.wav')
            spoken_text = transcribe_speech('user_audio.wav')


            similar_words = ['커피', '코피', '꺼피', '컾이', '커비']  # 비슷한 단어 리스트


            similarity_threshold = 0.6  # 유사도 임계값


            # 유사한 단어가 있는지 확인
            similar_word = difflib.get_close_matches(spoken_text, similar_words, n=1, cutoff=similarity_threshold)
            if similar_word:
                selected_item = '커피'  # 선택된 항목이 '커피'로 설정
                return select_coffee(selected_item)
                #return render_template('select_option.html', selected_item=selected_item)
            # 여기서 음성으로 인식된 텍스트를 처리하고 다음 단계로 넘어가는 코드 작성
            # spoken_text를 분석하여 어떤 커피를 선택했는지 확인하고 처리하는 로직을 추가
        else:
            # 직접 선택한 경우에 대한 로직을 추가
            pass
    return render_template('second.html')


@app.route('/order/select_coffee', methods=['POST'])
def select_coffee():
    if request.method == 'POST':
        selected_coffee = request.form.get('coffee_type')
    #if selected_coffee == '커피':
        # 선택된 커피에 따른 다음 단계로 이동
        #return redirect(url_for('select_option'))


        # 여기에 선택된 커피에 대한 처리 로직 추가
        # EX) 선택된 커피에 따른 다음 단계로의 이동 등을 구현


    return render_template('third_coffee.html')  # 다음 단계로 이동




if __name__ == '__main__':
    app.run(debug=True)