#!/usr/bin/env python3
from util import *


if __name__ == '__main__':
    image_content = encode_image_to_base64('../data/src.jpg')

    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/img2img"
            },
            "payload": {
                "init_images": [
                    image_content
                ],
                "override_settings": {
                    "sd_model_checkpoint": "sd_xl_base_1.0",
                    "sd_vae": "sdxl_vae.safetensors"
                },
                "prompt": "at the ocean",
                "negative_prompt": "",
                "seed": -1,
                "batch_size": 1,
                "denoising_strength": 0.75,
                "steps": 30,
                "cfg_scale": 7,
                "width": 960,
                "height": 1280,
                "sampler_name": "DPM++ SDE Karras",
                "sampler_index": "DPM++ SDE Karras",
                "restore_faces": False,
                "alwayson_scripts": {
                    "controlnet": {
                        "args": [
                            {
                                "module": "canny",
                                "model": "diffusers_xl_canny_full",
                                "weight": 1,
                                "resize_mode": "Crop and Resize",
                                "lowvram": False,
                                "processor_res": 1024,
                                "threshold_a": 75,
                                "threshold_b": 75,
                                "guidance": 1,
                                "guidance_start": 0,
                                "guidance_end": 1,
                                "control_mode": "Balanced",
                                "pixel_perfect": False
                            }
                        ]
                    }
                }
            }
        }
    }

    post_request(payload)
