import io
import json
import time
import traceback
from base64 import b64decode, b64encode
from copy import deepcopy
from typing import Any, Union
import urllib.request
import urllib.parse
from urllib import request, parse
from httpx import get, post
import uuid
from base64 import b64decode
from PIL import Image
from yarl import URL

from core.tools.entities.common_entities import I18nObject
from core.tools.entities.tool_entities import ToolInvokeMessage, ToolParameter, ToolParameterOption
from core.tools.errors import ToolProviderCredentialValidationError
from core.tools.tool.builtin_tool import BuiltinTool

default_prompt_text = r"""
{
  "1": {
    "inputs": {
      "ckpt_name": "SDXL\\dreamshaperXL_lightningDPMSDE.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\Little_Tinies.safetensors",
      "lora_model_strength": 1,
      "lora_clip_strength": 1,
      "positive": [
        "80",
        0
      ],
      "negative": [
        "80",
        1
      ],
      "token_normalization": "none",
      "weight_interpretation": "comfy",
      "empty_latent_width": 1024,
      "empty_latent_height": 1024,
      "batch_size": 1
    },
    "class_type": "Efficient Loader",
    "_meta": {
      "title": "效率加载器"
    }
  },
  "2": {
    "inputs": {
      "seed": 851590489004658,
      "steps": 12,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "preview_method": "auto",
      "vae_decode": "true",
      "model": [
        "1",
        0
      ],
      "positive": [
        "1",
        1
      ],
      "negative": [
        "1",
        2
      ],
      "latent_image": [
        "1",
        3
      ],
      "optional_vae": [
        "1",
        4
      ]
    },
    "class_type": "KSampler (Efficient)",
    "_meta": {
      "title": "K采样器(效率)"
    }
  },
  "23": {
    "inputs": {
      "ckpt_name": "SDXL\\dreamshaperXL_lightningDPMSDE.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\Little_Tinies.safetensors",
      "lora_model_strength": 1,
      "lora_clip_strength": 1,
      "positive": [
        "81",
        0
      ],
      "negative": [
        "81",
        1
      ],
      "token_normalization": "none",
      "weight_interpretation": "comfy",
      "empty_latent_width": 1024,
      "empty_latent_height": 1024,
      "batch_size": 1
    },
    "class_type": "Efficient Loader",
    "_meta": {
      "title": "效率加载器"
    }
  },
  "24": {
    "inputs": {
      "seed": 1078544644003685,
      "steps": 12,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "preview_method": "auto",
      "vae_decode": "true",
      "model": [
        "23",
        0
      ],
      "positive": [
        "23",
        1
      ],
      "negative": [
        "23",
        2
      ],
      "latent_image": [
        "23",
        3
      ],
      "optional_vae": [
        "23",
        4
      ]
    },
    "class_type": "KSampler (Efficient)",
    "_meta": {
      "title": "K采样器(效率)"
    }
  },
  "27": {
    "inputs": {
      "image": "$27-0",
      "images": [
        "45",
        0
      ]
    },
    "class_type": "PreviewBridge",
    "_meta": {
      "title": "桥接预览图像"
    }
  },
  "28": {
    "inputs": {
      "preset": "custom",
      "text_top": "",
      "text_bottom": "啊！终于到家啦，开心！\n",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "max_font_size": 150,
      "font_color": "black",
      "font_outline": "none",
      "bar_color": "white",
      "bar_options": "bottom",
      "font_color_hex": "#000000",
      "bar_color_hex": "#000000",
      "image": [
        "2",
        5
      ]
    },
    "class_type": "CR Simple Meme Template",
    "_meta": {
      "title": "meme模板(简易)"
    }
  },
  "29": {
    "inputs": {
      "preset": "custom",
      "text_top": "",
      "text_bottom": " 我晕!这是谁干的好事？？\n",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "max_font_size": 150,
      "font_color": "black",
      "font_outline": "none",
      "bar_color": "white",
      "bar_options": "bottom",
      "font_color_hex": "#000000",
      "bar_color_hex": "#000000",
      "image": [
        "24",
        5
      ]
    },
    "class_type": "CR Simple Meme Template",
    "_meta": {
      "title": "meme模板(简易)"
    }
  },
  "30": {
    "inputs": {
      "ckpt_name": "SDXL\\dreamshaperXL_lightningDPMSDE.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\Little_Tinies.safetensors",
      "lora_model_strength": 1,
      "lora_clip_strength": 1,
      "positive": [
        "82",
        0
      ],
      "negative": [
        "82",
        1
      ],
      "token_normalization": "none",
      "weight_interpretation": "comfy",
      "empty_latent_width": 1024,
      "empty_latent_height": 1024,
      "batch_size": 1
    },
    "class_type": "Efficient Loader",
    "_meta": {
      "title": "效率加载器"
    }
  },
  "31": {
    "inputs": {
      "seed": 49142047746649,
      "steps": 10,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "preview_method": "auto",
      "vae_decode": "true",
      "model": [
        "30",
        0
      ],
      "positive": [
        "30",
        1
      ],
      "negative": [
        "30",
        2
      ],
      "latent_image": [
        "30",
        3
      ],
      "optional_vae": [
        "30",
        4
      ]
    },
    "class_type": "KSampler (Efficient)",
    "_meta": {
      "title": "K采样器(效率)"
    }
  },
  "33": {
    "inputs": {
      "preset": "custom",
      "text_top": "",
      "text_bottom": "留言 :\"你忘了给我买猫粮!\"\n",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "max_font_size": 150,
      "font_color": "black",
      "font_outline": "none",
      "bar_color": "white",
      "bar_options": "bottom",
      "font_color_hex": "#000000",
      "bar_color_hex": "#000000",
      "image": [
        "31",
        5
      ]
    },
    "class_type": "CR Simple Meme Template",
    "_meta": {
      "title": "meme模板(简易)"
    }
  },
  "34": {
    "inputs": {
      "layout_options": "header and footer",
      "header_height": 200,
      "header_text": "一日生活",
      "header_align": "left",
      "footer_height": 100,
      "footer_text": "",
      "footer_align": "right",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "font_color": "black",
      "header_font_size": 150,
      "footer_font_size": 60,
      "border_thickness": 10,
      "border_color": "black",
      "background_color": "white",
      "font_color_hex": "#000000",
      "border_color_hex": "#000000",
      "bg_color_hex": "#000000",
      "image_panel": [
        "68",
        0
      ]
    },
    "class_type": "CR Page Layout",
    "_meta": {
      "title": "页面布局"
    }
  },
  "45": {
    "inputs": {
      "top_thickness": 20,
      "bottom_thickness": 20,
      "left_thickness": 20,
      "right_thickness": 20,
      "border_color": "custom",
      "outline_thickness": 100,
      "outline_color": "navy",
      "border_color_hex": "#004E9C",
      "image": [
        "34",
        0
      ]
    },
    "class_type": "CR Image Border",
    "_meta": {
      "title": "图像边框"
    }
  },
  "46": {
    "inputs": {
      "ckpt_name": "SDXL\\dreamshaperXL_lightningDPMSDE.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\Little_Tinies.safetensors",
      "lora_model_strength": 1,
      "lora_clip_strength": 1,
      "positive": [
        "83",
        0
      ],
      "negative": [
        "83",
        1
      ],
      "token_normalization": "none",
      "weight_interpretation": "comfy",
      "empty_latent_width": 1024,
      "empty_latent_height": 1024,
      "batch_size": 1
    },
    "class_type": "Efficient Loader",
    "_meta": {
      "title": "效率加载器"
    }
  },
  "47": {
    "inputs": {
      "seed": 49142047746654,
      "steps": 10,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "preview_method": "auto",
      "vae_decode": "true",
      "model": [
        "46",
        0
      ],
      "positive": [
        "46",
        1
      ],
      "negative": [
        "46",
        2
      ],
      "latent_image": [
        "46",
        3
      ],
      "optional_vae": [
        "46",
        4
      ]
    },
    "class_type": "KSampler (Efficient)",
    "_meta": {
      "title": "K采样器(效率)"
    }
  },
  "49": {
    "inputs": {
      "preset": "custom",
      "text_top": "",
      "text_bottom": "哦，原来如此！\n",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "max_font_size": 150,
      "font_color": "black",
      "font_outline": "none",
      "bar_color": "white",
      "bar_options": "bottom",
      "font_color_hex": "#000000",
      "bar_color_hex": "#000000",
      "image": [
        "47",
        5
      ]
    },
    "class_type": "CR Simple Meme Template",
    "_meta": {
      "title": "meme模板(简易)"
    }
  },
  "51": {
    "inputs": {
      "ckpt_name": "SDXL\\dreamshaperXL_lightningDPMSDE.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\Little_Tinies.safetensors",
      "lora_model_strength": 1,
      "lora_clip_strength": 1,
      "positive": [
        "84",
        0
      ],
      "negative": [
        "84",
        1
      ],
      "token_normalization": "none",
      "weight_interpretation": "comfy",
      "empty_latent_width": 1024,
      "empty_latent_height": 1024,
      "batch_size": 1
    },
    "class_type": "Efficient Loader",
    "_meta": {
      "title": "效率加载器"
    }
  },
  "52": {
    "inputs": {
      "seed": 851590489004658,
      "steps": 8,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "preview_method": "auto",
      "vae_decode": "true",
      "model": [
        "51",
        0
      ],
      "positive": [
        "51",
        1
      ],
      "negative": [
        "51",
        2
      ],
      "latent_image": [
        "51",
        3
      ],
      "optional_vae": [
        "51",
        4
      ]
    },
    "class_type": "KSampler (Efficient)",
    "_meta": {
      "title": "K采样器(效率)"
    }
  },
  "54": {
    "inputs": {
      "ckpt_name": "SDXL\\dreamshaperXL_lightningDPMSDE.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\Little_Tinies.safetensors",
      "lora_model_strength": 1,
      "lora_clip_strength": 1,
      "positive": [
        "85",
        0
      ],
      "negative": [
        "85",
        1
      ],
      "token_normalization": "none",
      "weight_interpretation": "comfy",
      "empty_latent_width": 1024,
      "empty_latent_height": 1024,
      "batch_size": 1
    },
    "class_type": "Efficient Loader",
    "_meta": {
      "title": "效率加载器"
    }
  },
  "55": {
    "inputs": {
      "seed": 1078544644003683,
      "steps": 10,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "preview_method": "auto",
      "vae_decode": "true",
      "model": [
        "54",
        0
      ],
      "positive": [
        "54",
        1
      ],
      "negative": [
        "54",
        2
      ],
      "latent_image": [
        "54",
        3
      ],
      "optional_vae": [
        "54",
        4
      ]
    },
    "class_type": "KSampler (Efficient)",
    "_meta": {
      "title": "K采样器(效率)"
    }
  },
  "57": {
    "inputs": {
      "preset": "custom",
      "text_top": "",
      "text_bottom": "天呀！谢天谢地，之前买的还有一点存货~\n",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "max_font_size": 150,
      "font_color": "black",
      "font_outline": "none",
      "bar_color": "white",
      "bar_options": "bottom",
      "font_color_hex": "#000000",
      "bar_color_hex": "#000000",
      "image": [
        "52",
        5
      ]
    },
    "class_type": "CR Simple Meme Template",
    "_meta": {
      "title": "meme模板(简易)"
    }
  },
  "58": {
    "inputs": {
      "preset": "custom",
      "text_top": "",
      "text_bottom": "来吧！给你，小捣蛋鬼",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "max_font_size": 150,
      "font_color": "black",
      "font_outline": "none",
      "bar_color": "white",
      "bar_options": "bottom",
      "font_color_hex": "#000000",
      "bar_color_hex": "#000000",
      "image": [
        "55",
        5
      ]
    },
    "class_type": "CR Simple Meme Template",
    "_meta": {
      "title": "meme模板(简易)"
    }
  },
  "59": {
    "inputs": {
      "ckpt_name": "SDXL\\dreamshaperXL_lightningDPMSDE.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\Little_Tinies.safetensors",
      "lora_model_strength": 1,
      "lora_clip_strength": 1,
      "positive": [
        "86",
        0
      ],
      "negative": [
        "86",
        1
      ],
      "token_normalization": "none",
      "weight_interpretation": "comfy",
      "empty_latent_width": 1024,
      "empty_latent_height": 1024,
      "batch_size": 1
    },
    "class_type": "Efficient Loader",
    "_meta": {
      "title": "效率加载器"
    }
  },
  "60": {
    "inputs": {
      "seed": 49142047746648,
      "steps": 8,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "preview_method": "auto",
      "vae_decode": "true",
      "model": [
        "59",
        0
      ],
      "positive": [
        "59",
        1
      ],
      "negative": [
        "59",
        2
      ],
      "latent_image": [
        "59",
        3
      ],
      "optional_vae": [
        "59",
        4
      ]
    },
    "class_type": "KSampler (Efficient)",
    "_meta": {
      "title": "K采样器(效率)"
    }
  },
  "62": {
    "inputs": {
      "preset": "custom",
      "text_top": "",
      "text_bottom": "现在开心了吧，嗯？",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "max_font_size": 150,
      "font_color": "black",
      "font_outline": "none",
      "bar_color": "white",
      "bar_options": "bottom",
      "font_color_hex": "#000000",
      "bar_color_hex": "#000000",
      "image": [
        "60",
        5
      ]
    },
    "class_type": "CR Simple Meme Template",
    "_meta": {
      "title": "meme模板(简易)"
    }
  },
  "63": {
    "inputs": {
      "ckpt_name": "SDXL\\dreamshaperXL_lightningDPMSDE.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\Little_Tinies.safetensors",
      "lora_model_strength": 1,
      "lora_clip_strength": 1,
      "positive": [
        "87",
        0
      ],
      "negative": [
        "87",
        1
      ],
      "token_normalization": "none",
      "weight_interpretation": "comfy",
      "empty_latent_width": 1024,
      "empty_latent_height": 1024,
      "batch_size": 1
    },
    "class_type": "Efficient Loader",
    "_meta": {
      "title": "效率加载器"
    }
  },
  "64": {
    "inputs": {
      "seed": 49142047746644,
      "steps": 10,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "preview_method": "auto",
      "vae_decode": "true",
      "model": [
        "63",
        0
      ],
      "positive": [
        "63",
        1
      ],
      "negative": [
        "63",
        2
      ],
      "latent_image": [
        "63",
        3
      ],
      "optional_vae": [
        "63",
        4
      ]
    },
    "class_type": "KSampler (Efficient)",
    "_meta": {
      "title": "K采样器(效率)"
    }
  },
  "66": {
    "inputs": {
      "preset": "custom",
      "text_top": "",
      "text_bottom": "猫咪: 那是相当开心~",
      "font_name": "阿里巴巴普惠体-2.0-55.ttf",
      "max_font_size": 150,
      "font_color": "black",
      "font_outline": "none",
      "bar_color": "white",
      "bar_options": "bottom",
      "font_color_hex": "#000000",
      "bar_color_hex": "#000000",
      "image": [
        "64",
        5
      ]
    },
    "class_type": "CR Simple Meme Template",
    "_meta": {
      "title": "meme模板(简易)"
    }
  },
  "68": {
    "inputs": {
      "border_thickness": 20,
      "border_color": "white",
      "outline_thickness": 5,
      "outline_color": "black",
      "max_columns": 4,
      "border_color_hex": "#000000",
      "images": [
        "78",
        0
      ]
    },
    "class_type": "CR Image Grid Panel",
    "_meta": {
      "title": "图像表格面板"
    }
  },
  "78": {
    "inputs": {
      "image1": [
        "28",
        0
      ],
      "image2": [
        "29",
        0
      ],
      "image3": [
        "33",
        0
      ],
      "image4": [
        "49",
        0
      ],
      "image5": [
        "57",
        0
      ],
      "image6": [
        "58",
        0
      ],
      "image7": [
        "62",
        0
      ],
      "image8": [
        "66",
        0
      ]
    },
    "class_type": "ImpactMakeImageBatch",
    "_meta": {
      "title": "制作图像批次"
    }
  },
  "80": {
    "inputs": {
      "text_positive": "a cozy living room with a couch, a TV, and (a cat sleeping on a rug). A person is seen entering the room.",
      "text_negative": "bad anatomy",
      "milehigh": "Animation",
      "log_prompt": false
    },
    "class_type": "MilehighStyler",
    "_meta": {
      "title": "Milehigh Styler"
    }
  },
  "81": {
    "inputs": {
      "text_positive": "girl walks towards the couch, but sees something on the floor.\nfloor with torn pieces of papers",
      "text_negative": "bad anatomy",
      "milehigh": "Animation",
      "log_prompt": false
    },
    "class_type": "MilehighStyler",
    "_meta": {
      "title": "Milehigh Styler"
    }
  },
  "82": {
    "inputs": {
      "text_positive": "Close-up of the floor. It's a torn piece of paper with a message: :you forgot to buy cat treats!\" scribbled on it.",
      "text_negative": "bad anatomy",
      "milehigh": "Animation",
      "log_prompt": false
    },
    "class_type": "MilehighStyler",
    "_meta": {
      "title": "Milehigh Styler"
    }
  },
  "83": {
    "inputs": {
      "text_positive": "girl looks puzzled, then glances at the cat, who's now awake and staring at them.",
      "text_negative": "bad anatomy",
      "milehigh": "Animation",
      "log_prompt": false
    },
    "class_type": "MilehighStyler",
    "_meta": {
      "title": "Milehigh Styler"
    }
  },
  "84": {
    "inputs": {
      "text_positive": "girl is now in the kitchen and opening a box from the pantry with a box in the hand",
      "text_negative": "bad anatomy",
      "milehigh": "Animation",
      "log_prompt": false
    },
    "class_type": "MilehighStyler",
    "_meta": {
      "title": "Milehigh Styler"
    }
  },
  "85": {
    "inputs": {
      "text_positive": "girl grabs a handful of treats and offer it to the cat in the home",
      "text_negative": "bad fingers, bad hands, malformed hands, multiple hands",
      "milehigh": "Animation",
      "log_prompt": false
    },
    "class_type": "MilehighStyler",
    "_meta": {
      "title": "Milehigh Styler"
    }
  },
  "86": {
    "inputs": {
      "text_positive": "girl offer the treat to the cat",
      "text_negative": "bad anatomy",
      "milehigh": "Animation",
      "log_prompt": false
    },
    "class_type": "MilehighStyler",
    "_meta": {
      "title": "Milehigh Styler"
    }
  },
  "87": {
    "inputs": {
      "text_positive": "cat seeing happily ",
      "text_negative": "bad anatomy",
      "milehigh": "Animation",
      "log_prompt": false
    },
    "class_type": "MilehighStyler",
    "_meta": {
      "title": "Milehigh Styler"
    }
  },
  "88": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "45",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "保存图像"
    }
  }
}
"""

class DisneyStyleCartoonTool(BuiltinTool):

    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        client_id = str(uuid.uuid4())
        base_url = self.runtime.credentials.get('base_url', None)

        if not base_url:
            return self.create_text_message('Please input base_url')

        # validate server status
        try:
            url = str(URL(base_url) / 'object_info')
            response = get(url)
            if response.status_code != 200:
                raise ToolProviderCredentialValidationError(f'Failed connect server {base_url}')
        except Exception as e:
            raise ToolProviderCredentialValidationError(f'Failed connect server {base_url}')

        return self.text2img(client_id, base_url=base_url,tool_parameters=tool_parameters)

    def get_history(self, base_url, prompt_id):
        with urllib.request.urlopen(f"{base_url}/history/{prompt_id}", timeout=3000) as response:
            return json.loads(response.read())
        
    def get_image_url(self, base_url, filename, subfolder, folder_type):
        data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
        url_values = urllib.parse.urlencode(data)
        img_url = f"{base_url}/view?{url_values}"
        return img_url

    def get_image(self, base_url, filename, subfolder, folder_type):
        data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
        url_values = urllib.parse.urlencode(data)
        img_url = f"{base_url}/view?{url_values}"
        with urllib.request.urlopen(img_url) as response:
            return response.read()
      
        
    def text2img(self, client_id, base_url: str, tool_parameters: dict[str, Any]) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        """
            generate image
        """
        
        prompt = json.loads(default_prompt_text)

        model = tool_parameters.get('model', '')
        if model:
            for node in [1,23,30,46,51,54,59,63]:
                prompt[str(node)]["inputs"]["ckpt_name"] = model

        lora_model = tool_parameters.get('lora', '')
        if lora_model:
            for node in [1,23,30,46,51,54,59,63]:
                prompt[str(node)]["inputs"]["lora_name"] = lora_model

        width = tool_parameters.get('width', '')
        if width:
            for node in [1,23,30,46,51,54,59,63]:
                prompt[str(node)]["inputs"]["empty_latent_width"] = width

        height = tool_parameters.get('height', '')
        if height:
            for node in [1,23,30,46,51,54,59,63]:
                prompt[str(node)]["inputs"]["empty_latent_height"] = height

        topic = tool_parameters.get('topic', '')
        if topic:
            prompt["34"]["inputs"]["header_text"] = topic
        
        for idx, ord in zip(range(0, 8), range(80, 88)):
            text_positive = tool_parameters.get(f'text_positive_{idx+1}', '')
            if text_positive:
                prompt[str(ord)]["inputs"]["text_positive"] = text_positive
        for idx, ord in zip(range(0, 8), [28,29,33,49,57,58,62,66]):
            text_bottom = tool_parameters.get(f'text_bottom_{idx+1}', '')
            if text_positive:
                prompt[str(ord)]["inputs"]["text_bottom"] = text_bottom
        
        try:
            # 提交任务
            p = {"prompt": prompt, "client_id": client_id}
            response = post(f"{base_url}/prompt", json=p, timeout=3600)
            response.raise_for_status()
            
            # 获取 prompt_id
            prompt_id = response.json().get("prompt_id", None)
            if prompt_id is None:
                return self.create_text_message(f'Failed to generate image: Missing prompt_id in response')

            # 轮询任务状态
            time.sleep(10)  # 初始等待时间
            while True:
                response = get(f"{base_url}/queue", timeout=3600)
                response.raise_for_status()
                queue_data = response.json()
                
                # 调试信息：打印 queue_data 内容
                print(f"Queue data: {queue_data}")

                if 'queue_running' in queue_data:
                    task_list = [task[1] for task in queue_data["queue_running"]]
                    if prompt_id in task_list:
                        print(f"Prompt ID {prompt_id} is still running.")
                        time.sleep(2)  # 持续轮询
                    else:
                        print(f"Prompt ID {prompt_id} has completed.")
                        break
                else:
                    print("Queue is empty or 'queue_running' key is missing.")
                    break
            
            # 获取生成历史
            history_data = self.get_history(base_url, prompt_id)
            if prompt_id not in history_data:
                return self.create_text_message(f'Failed to retrieve history for prompt_id: {prompt_id}')
            
            history = history_data[prompt_id]
            output_images = {}
            for node_id, node_output in history['outputs'].items():
                if 'images' in node_output:
                    images_output = []
                    for image in node_output['images']:
                        image_url = self.get_image_url(base_url, image['filename'], image['subfolder'], image['type'])
                        images_output.append(image_url)
                    output_images[node_id] = images_output
            
            return self.create_text_message(json.dumps(output_images, ensure_ascii=False))
        except json.JSONDecodeError as e:
            return self.create_text_message(f"JSON decode error: {str(e)}")
        except Exception as e:
            return self.create_text_message(f"Failed to process the image: {traceback.format_exc()} {str(e)}")
        
    def get_models(self) -> list[str]:
        """
            get sd models
        """
        try:
            base_url = self.runtime.credentials.get('base_url', None)
            if not base_url:
                return [], []
            api_url = str(URL(base_url) / 'object_info')
            response = get(url=api_url, timeout=3600)
            if response.status_code != 200:
                return [], []
            else:
                json_data = response.json()
                models = json_data["CheckpointLoaderSimple"]["input"]["required"]["ckpt_name"][0]
                lora_models = json_data["LoraLoader"]["input"]["required"]["lora_name"][0]
                return models, lora_models
        except Exception as e:
            return [], []

    def get_runtime_parameters(self) -> list[ToolParameter]:
        
        parameters = []
        ## 加载模型
        models, lora_models = self.get_models()
        if models and lora_models:
            parameters += [
                ToolParameter(name='model',
                    label=I18nObject(en_US='model', zh_Hans='sd 模型'),
                    human_description=I18nObject(
                      en_US='Model of Stable Diffusion, you can check the official documentation of Stable Diffusion',
                      zh_Hans='Stable Diffusion 的模型，您可以查看 Stable Diffusion 的官方文档',
                    ),
                    type=ToolParameter.ToolParameterType.SELECT,
                    form=ToolParameter.ToolParameterForm.FORM,
                    llm_description='Model of Stable Diffusion, you can check the official documentation of Stable Diffusion',
                    required=True,
                    default=models[0],
                    options=[ToolParameterOption(
                        value=i,
                        label=I18nObject(en_US=i, zh_Hans=i)
                    ) for i in models]),
                ToolParameter(name='lora',
                    label=I18nObject(en_US='lora', zh_Hans='lora 模型'),
                    human_description=I18nObject(
                      en_US='lora model',
                      zh_Hans='lora 模型',
                    ),
                    type=ToolParameter.ToolParameterType.SELECT,
                    form=ToolParameter.ToolParameterForm.FORM,
                    llm_description='lora model',
                    required=True,
                    default=lora_models[0],
                    options=[ToolParameterOption(
                        value=i,
                        label=I18nObject(en_US=i, zh_Hans=i)
                    ) for i in lora_models])
            ]
        
        parameters += [
            ToolParameter(name='topic',
                         label=I18nObject(en_US='topic', zh_Hans='topic'),
                         human_description=I18nObject(
                             en_US='漫画主题',
                             zh_Hans='漫画主题',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='漫画主题',
                         required=True),
            ToolParameter(name='text_positive_1',
                         label=I18nObject(en_US='text_positive_1', zh_Hans='text_positive_1'),
                         human_description=I18nObject(
                             en_US='分镜提示词1',
                             zh_Hans='分镜提示词1',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='分镜提示词1',
                         required=True),
            ToolParameter(name='text_positive_2',
                         label=I18nObject(en_US='text_positive_2', zh_Hans='text_positive_2'),
                         human_description=I18nObject(
                             en_US='分镜提示词2',
                             zh_Hans='分镜提示词2',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='分镜提示词2',
                         required=True),
            ToolParameter(name='text_positive_3',
                         label=I18nObject(en_US='text_positive_3', zh_Hans='text_positive_3'),
                         human_description=I18nObject(
                             en_US='分镜提示词3',
                             zh_Hans='分镜提示词3',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='分镜提示词3',
                         required=True),
            ToolParameter(name='text_positive_4',
                         label=I18nObject(en_US='text_positive_4', zh_Hans='text_positive_4'),
                         human_description=I18nObject(
                             en_US='分镜提示词4',
                             zh_Hans='分镜提示词4',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='分镜提示词4',
                         required=True),
            ToolParameter(name='text_positive_5',
                         label=I18nObject(en_US='text_positive_5', zh_Hans='text_positive_5'),
                         human_description=I18nObject(
                             en_US='分镜提示词5',
                             zh_Hans='分镜提示词5',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='分镜提示词5',
                         required=True),
            ToolParameter(name='text_positive_6',
                         label=I18nObject(en_US='text_positive_6', zh_Hans='text_positive_6'),
                         human_description=I18nObject(
                             en_US='分镜提示词6',
                             zh_Hans='分镜提示词6',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='分镜提示词6',
                         required=True),
            ToolParameter(name='text_positive_7',
                         label=I18nObject(en_US='text_positive_7', zh_Hans='text_positive_7'),
                         human_description=I18nObject(
                             en_US='分镜提示词7',
                             zh_Hans='分镜提示词7',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='分镜提示词7',
                         required=True),
            ToolParameter(name='text_positive_8',
                         label=I18nObject(en_US='text_positive_8', zh_Hans='text_positive_8'),
                         human_description=I18nObject(
                             en_US='分镜提示词8',
                             zh_Hans='分镜提示词8',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='分镜提示词8',
                         required=True),
            ToolParameter(name='text_bottom_1',
                         label=I18nObject(en_US='text_bottom_1', zh_Hans='text_bottom_1'),
                         human_description=I18nObject(
                             en_US='对话1',
                             zh_Hans='对话1',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='对话1',
                         required=True),
            ToolParameter(name='text_bottom_2',
                         label=I18nObject(en_US='text_bottom_1', zh_Hans='text_bottom_2'),
                         human_description=I18nObject(
                             en_US='对话2',
                             zh_Hans='对话2',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='对话2',
                         required=True),
            ToolParameter(name='text_bottom_3',
                         label=I18nObject(en_US='text_bottom_3', zh_Hans='text_bottom_3'),
                         human_description=I18nObject(
                             en_US='对话3',
                             zh_Hans='对话3',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='对话3',
                         required=True),
            ToolParameter(name='text_bottom_4',
                         label=I18nObject(en_US='text_bottom_4', zh_Hans='text_bottom_4'),
                         human_description=I18nObject(
                             en_US='对话4',
                             zh_Hans='对话4',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='对话4',
                         required=True),
            ToolParameter(name='text_bottom_5',
                         label=I18nObject(en_US='text_bottom_5', zh_Hans='text_bottom_5'),
                         human_description=I18nObject(
                             en_US='对话5',
                             zh_Hans='对话5',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='对话5',
                         required=True),
            ToolParameter(name='text_bottom_6',
                         label=I18nObject(en_US='text_bottom_6', zh_Hans='text_bottom_6'),
                         human_description=I18nObject(
                             en_US='对话6',
                             zh_Hans='对话6',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='对话6',
                         required=True),
            ToolParameter(name='text_bottom_7',
                         label=I18nObject(en_US='text_bottom_7', zh_Hans='text_bottom_7'),
                         human_description=I18nObject(
                             en_US='对话7',
                             zh_Hans='对话7',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='对话7',
                         required=True),
            ToolParameter(name='text_bottom_8',
                         label=I18nObject(en_US='text_bottom_8', zh_Hans='text_bottom_8'),
                         human_description=I18nObject(
                             en_US='对话8',
                             zh_Hans='对话8',
                         ),
                         type=ToolParameter.ToolParameterType.STRING,
                         form=ToolParameter.ToolParameterForm.LLM,
                         llm_description='对话8',
                         required=True)]
        
        return parameters
