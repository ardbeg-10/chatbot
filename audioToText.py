from openai import OpenAI
import csv

client = OpenAI(api_key = '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')

# read audio file
with open("audio/lecture03_audio.mp3", "rb") as audio_file:
    # 调用翻译接口
    transcript = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file
    )

# extract text from transcript
translated_text = transcript.text

csv_file_path = 'output/lecture03.csv'

# save translated text to csv file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerow([translated_text])
