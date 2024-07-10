import whisper

# model = whisper.load_model("base")
model = whisper.load_model("medium")
result = model.transcribe("kivy clock A v2 x265.mp4", fp16=False)
print(result["text"])


# model = whisper.load_model("base")

# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("kivy clock A v2 x265.mp4")
# audio = whisper.pad_or_trim(audio)

# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# # decode the audio
# # options = whisper.DecodingOptions()
# options = whisper.DecodingOptions(language= 'en', fp16=False)
# # result = whisper.decode(model, mel, options)
# result = whisper.decode(model, "kivy clock A v2 x265.mp4", options)

# # print the recognized text
# print(result.text)