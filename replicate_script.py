import replicate
import webbrowser
from PIL import Image

""" urls = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": "a high definition picture of the footballer Kylian Mbappé"},
    ) 
    
print(urls)
if urls: 
    webbrowser.open(urls[0])
"""

training = replicate.trainings.create(
    model="stability-ai/sdxl",
    version="39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input={
      "input_images": "https://drive.google.com/file/d/1bIcOtsOYoyuDx-AQ9RVQz4WhP7avT65N/view?usp=sharing",
      "token_string": "TOK",
      "caption_prefix": "a photo of TOK",
      "max_train_steps": 1000,
      "use_face_detection_instead": False
    },
    # You need to create a model on Replicate that will be the destination for the trained version.
    destination="gileslerockeur/mbappe"
)