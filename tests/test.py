import json
import requests
import urllib.request
import urllib.parse
from urllib import request, parse
import random

#This is the ComfyUI api prompt format.

#If you want it for a specific workflow you can "enable dev mode options"
#in the settings of the UI (gear beside the "Queue Size: ") this will enable
#a button on the UI to save workflows in api format.

#keep in mind ComfyUI is pre alpha software so this format will change a bit.

#this is the one for the default workflow
prompt_text = """
{
  "3": {
    "inputs": {
      "seed": 100667782383638,
      "steps": 20,
      "cfg": 8,
      "sampler_name": "euler",
      "scheduler": "normal",
      "denoise": 1,
      "model": [
        "4",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "5",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "4": {
    "inputs": {
      "ckpt_name": "juggernautXL_v9Rundiffusionphoto2.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "5": {
    "inputs": {
      "width": 512,
      "height": 512,
      "batch_size": 1
    },
    "class_type": "EmptyLatentImage",
    "_meta": {
      "title": "Empty Latent Image"
    }
  },
  "6": {
    "inputs": {
      "text": "beautiful scenery nature glass bottle landscape, , purple galaxy bottle,",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "text, watermark",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "4",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "9": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  }
}
"""

server_addr = "https://comfyui-dify-demo.tonori.cn"

def queue_prompt(prompt):
    p = {"prompt": prompt}
    
    req =  requests.post(f"{server_addr}/prompt", json=p)
    return req

def get_history(prompt_id):
    with urllib.request.urlopen(f"{server_addr}/history/{prompt_id}") as response:
        return json.loads(response.read())

def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    img_url = f"{server_addr}/view?{url_values}"
    print(img_url)
    with urllib.request.urlopen(img_url) as response:
        return response.read()
    
def get_image_url(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    img_url = f"{server_addr}/view?{url_values}"
    return img_url
    
def get_images(prompt_id, is_url=True):
    history = get_history(prompt_id)[prompt_id]
    output_images = {}
    for o in history['outputs']:
        for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            if 'images' in node_output:
                images_output = []
                for image in node_output['images']:
                    if is_url:
                        images_output.append(get_image_url(image['filename'], image['subfolder'], image['type']))
                    else:
                        image_data = get_image(image['filename'], image['subfolder'], image['type'])
                        images_output.append(image_data)
            output_images[node_id] = images_output
    return output_images

# fdce0722-d81f-4d92-a8be-bd543fab5363
prompt = json.loads(prompt_text)

"""
req = queue_prompt(prompt)
print(req.status_code)
print(req.json())
"""

images = get_images("0e4af774-61b2-45d5-865a-5801df724596")
print(images)
