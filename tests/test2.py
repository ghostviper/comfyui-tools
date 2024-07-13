import json

default_prompt_text = r"""
{
  "1": {
    "inputs": {
      "ckpt_name": "SDXL\\Juggernaut_X_RunDiffusion_Hyper.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\sdxl_lightning_4step_lora.safetensors",
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
      "empty_latent_width": 576,
      "empty_latent_height": 576,
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
      "steps": 6,
      "cfg": 2,
      "sampler_name": "lcm",
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
      "ckpt_name": "SDXL\\Juggernaut_X_RunDiffusion_Hyper.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\sdxl_lightning_4step_lora.safetensors",
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
      "empty_latent_width": 576,
      "empty_latent_height": 576,
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
      "steps": 8,
      "cfg": 2,
      "sampler_name": "lcm",
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
      "text_bottom": " Ah, finally home sweet heart.\n",
      "font_name": "comic.ttf",
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
      "text_bottom": " Huh? What's this?\n",
      "font_name": "comic.ttf",
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
      "ckpt_name": "SDXL\\Juggernaut_X_RunDiffusion_Hyper.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\sdxl_lightning_4step_lora.safetensors",
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
      "empty_latent_width": 576,
      "empty_latent_height": 576,
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
      "steps": 8,
      "cfg": 2,
      "sampler_name": "lcm",
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
      "text_bottom": "Message :\"You forgot to buy cat treats!\"\n",
      "font_name": "comic.ttf",
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
      "header_text": "Day in the Life",
      "header_align": "left",
      "footer_height": 100,
      "footer_text": "",
      "footer_align": "right",
      "font_name": "Quicksand-Bold.ttf",
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
      "ckpt_name": "SDXL\\Juggernaut_X_RunDiffusion_Hyper.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\sdxl_lightning_4step_lora.safetensors",
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
      "empty_latent_width": 576,
      "empty_latent_height": 576,
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
      "steps": 8,
      "cfg": 2,
      "sampler_name": "lcm",
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
      "text_bottom": "Oh, really?\n",
      "font_name": "comic.ttf",
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
      "ckpt_name": "SDXL\\Juggernaut_X_RunDiffusion_Hyper.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\sdxl_lightning_4step_lora.safetensors",
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
      "empty_latent_width": 576,
      "empty_latent_height": 576,
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
      "sampler_name": "lcm",
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
      "ckpt_name": "SDXL\\Juggernaut_X_RunDiffusion_Hyper.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\sdxl_lightning_4step_lora.safetensors",
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
      "empty_latent_width": 576,
      "empty_latent_height": 576,
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
      "steps": 6,
      "cfg": 2,
      "sampler_name": "lcm",
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
      "text_bottom": "Phew! Thankfully, I remembered to buy some.\n",
      "font_name": "comic.ttf",
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
      "text_bottom": "Here you go, troublemaker.\n",
      "font_name": "comic.ttf",
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
      "ckpt_name": "SDXL\\Juggernaut_X_RunDiffusion_Hyper.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\sdxl_lightning_4step_lora.safetensors",
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
      "empty_latent_width": 576,
      "empty_latent_height": 576,
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
      "steps": 12,
      "cfg": 2,
      "sampler_name": "lcm",
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
      "text_bottom": " Are you happy now?\n",
      "font_name": "comic.ttf",
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
      "ckpt_name": "SDXL\\Juggernaut_X_RunDiffusion_Hyper.safetensors",
      "vae_name": "Baked VAE",
      "clip_skip": -2,
      "lora_name": "SDXL\\sdxl_lightning_4step_lora.safetensors",
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
      "empty_latent_width": 576,
      "empty_latent_height": 576,
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
      "steps": 12,
      "cfg": 2,
      "sampler_name": "lcm",
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
      "text_bottom": "Cat: Purrfectly happy.",
      "font_name": "comic.ttf",
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
      "milehigh": "Disney Animation_Animation",
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
      "milehigh": "Disney Animation_Animation",
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
      "milehigh": "Disney Animation_Animation",
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
      "milehigh": "Disney Animation_Animation",
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
      "milehigh": "Disney Animation_Animation",
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
      "milehigh": "Disney Animation_Animation",
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
      "milehigh": "Disney Animation_Animation",
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
      "milehigh": "Disney Animation_Animation",
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

print(json.loads(default_prompt_text))