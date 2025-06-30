import torch
from transformers import pipeline

# Optimized configuration
device = 0 if torch.cuda.is_available() else -1
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=15,  # Smaller chunks
    device=device,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

sample = 'downloaded_audio.mp3'
prediction = pipe(sample, batch_size=16)["text"]  # Larger batch
print(prediction)