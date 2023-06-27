import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
processor = BlipProcessor.from_pretrained("noamrot/FuseCap")
model = BlipForConditionalGeneration.from_pretrained("noamrot/FuseCap").to(device)

img_url = 'https://huggingface.co/spaces/noamrot/FuseCap/resolve/main/bike.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

text = "a picture of "
inputs = processor(raw_image, text, return_tensors="pt").to(device)

out = model.generate(**inputs, num_beams = 3)
print(processor.decode(out[0], skip_special_tokens=True))
