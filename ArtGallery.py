import torch
import json
import os
import re
import platform
from PIL import Image, ImageOps, ImageSequence
import numpy as np
import safetensors.torch


def read_json_file(file_path):
    try:
        # Open file, load JSON content into python dictionary, and return it.
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_name(json_data):
    # Check that data is a list
    if not isinstance(json_data, list):
        print("Error: input data must be a list")
        return None

    names = []

    # Iterate over each item in the data list
    for item in json_data:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that 'name' is a key in the dictionary
            if 'name' in item:
                # Append the value of 'name' to the names list
                names.append(item['name'])

    return names

def get_prompt(json_data, template_name):
    try:
        # Check if json_data is a list
        if not isinstance(json_data, list):
            raise ValueError("Invalid JSON data. Expected a list of templates.")
            
        for template in json_data:
            # Check if template contains 'name' and 'tags' fields
            if 'name' not in template or 'tags' not in template:
                raise ValueError("Invalid template. Missing 'name' or 'tags' field.")
            
            if template['name'] == template_name:
                name = template.get('name', "")
                tags = template.get('tags', "")
                print("Extracted tags:", tags)
                return name

        # If function hasn't returned yet, no matching template was found
        raise ValueError(f"No template found with name '{template_name}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        

def get_img_path(template_name, template_type):
    p = os.path.dirname(os.path.realpath(__file__))
    # 根据操作系统选择合适的分隔符
    if os.name == 'posix':  # Unix/Linux/macOS
        separator = '/'
    elif os.name == 'nt':  # Windows
        separator = '\\'
    else:
        separator = '/'  # 默认使用斜杠作为分隔符

    image_path = os.path.join(p, 'img_lists', template_type)  # 使用适当的分隔符构建路径
    image_filename = f"{template_name}.png"

    full_image_path = image_path + separator + image_filename

    return full_image_path


class ArtGallery_Zho:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        # Get current file's directory
        p = os.path.dirname(os.path.realpath(__file__))

        # Paths for various JSON files
        artist_file_path = os.path.join(p, 'lists/artists/artist_list.json')
        camera_file_path = os.path.join(p, 'lists/cameras/camera_list.json')

        # Read JSON from file
        self.artist_data = read_json_file(artist_file_path)
        self.camera_data = read_json_file(camera_file_path)

        # Retrieve name from JSON data
        artist_list = get_name(self.artist_data)
        artist_list = ['-'] + artist_list
        camera_list = get_name(self.camera_data)
        camera_list = ['-'] + camera_list

        # Paths for various image files
        #artist_image_path = os.path.join(p, 'img_lists/artists/')

        max_float_value = 1.75

        return {
            "required": {
                "artist": (artist_list, {
                    "default": artist_list[0],
                }),
                "artist_weight": ("FLOAT", {
                    "default": 1.5,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "camera": (camera_list, {
                    "default": camera_list[0],
                }),
                "camera_weight": ("FLOAT", {
                    "default": 1.5,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
            }
        }

    RETURN_TYPES = ("STRING","STRING","STRING",)
    RETURN_NAMES = ("prompt","artist","camera",)
    FUNCTION = "artgallery"
    CATEGORY = "Zho模块组/🎨 ArtGallery 艺术画廊"

    def artgallery(self, artist="-", artist_weight=1, camera="-", camera_weight=1):

        artist = get_prompt(self.artist_data, artist)
        camera = get_prompt(self.camera_data, camera)

        artist_full_image_path = get_img_path(artist, "artists")
        camera_full_image_path = get_img_path(camera, "cameras")

        prompt = []


        if artist != "-" and artist_weight > 0:
            P_artist = f"({artist}:{round(artist_weight, 2)})"
            prompt.append(P_artist)

        if camera != "-" and camera_weight > 0:
            P_camera = f"({camera}:{round(camera_weight, 2)})"
            prompt.append(P_camera)

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        return (prompt, P_artist, P_camera,)


class ArtistsImage_Zho:
    @classmethod
    def INPUT_TYPES(s):
        p = os.path.dirname(os.path.realpath(__file__))
        atsimg_dir = os.path.join(p, 'img_lists/artists/')
        files = [f for f in os.listdir(atsimg_dir) if os.path.isfile(os.path.join(atsimg_dir, f))]

        max_float_value = 1.75

        return {
            "required": {
                "image": (sorted(files), {"image_upload_artist": True}),
                "weight": ("FLOAT", {
                    "default": 1.2,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
               }),
            }
        }


    CATEGORY = "Zho模块组/🎨 ArtGallery 艺术画廊"

    RETURN_TYPES = ("STRING", "IMAGE",)
    RETURN_NAMES = ("name", "image",)
    FUNCTION = "artists_image"

    def artists_image(self, image, weight=1):
        image_full_name = image
        image_name = image_full_name.rsplit('.', 1)[0]

        image_path =  get_img_path(image_name, "artists")
        img = Image.open(image_path)
        output_images = []
        output_masks = []
        for i in ImageSequence.Iterator(img):
            i = ImageOps.exif_transpose(i)
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))

        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        prompt = []

        if weight > 0:
            P_artist = f"({image_name}:{round(weight, 2)})"
            prompt.append(P_artist)

        return (P_artist, output_image,)


    @classmethod
    def IS_CHANGED(s, image):
        image_path = get_img_path(image_name, "artists")
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()


class CamerasImage_Zho:
    @classmethod
    def INPUT_TYPES(s):
        p = os.path.dirname(os.path.realpath(__file__))
        camerasimg_dir = os.path.join(p, 'img_lists/cameras/')
        files = [f for f in os.listdir(camerasimg_dir) if os.path.isfile(os.path.join(camerasimg_dir, f))]

        max_float_value = 1.75

        return {
            "required": {
                "image": (sorted(files), {"image_upload_camera": True}),
                "weight": ("FLOAT", {
                    "default": 1.2,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
               }),
            }
        }


    CATEGORY = "Zho模块组/🎨 ArtGallery 艺术画廊"

    RETURN_TYPES = ("STRING", "IMAGE",)
    RETURN_NAMES = ("name", "image",)
    FUNCTION = "cameras_image"

    def cameras_image(self, image, weight=1):
        image_full_name = image
        image_name = image_full_name.rsplit('.', 1)[0]

        image_path =  get_img_path(image_name, "cameras")
        img = Image.open(image_path)
        output_images = []
        output_masks = []
        for i in ImageSequence.Iterator(img):
            i = ImageOps.exif_transpose(i)
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))

        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        prompt = []

        if weight > 0:
            P_camera = f"({image_name}:{round(weight, 2)})"
            prompt.append(P_camera)

        return (P_camera, output_image,)


    @classmethod
    def IS_CHANGED(s, image):
        image_path = get_img_path(image_name, "cameras")
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()


class FilmsImage_Zho:
    @classmethod
    def INPUT_TYPES(s):
        p = os.path.dirname(os.path.realpath(__file__))
        filmsimg_dir = os.path.join(p, 'img_lists/films/')
        files = [f for f in os.listdir(filmsimg_dir) if os.path.isfile(os.path.join(filmsimg_dir, f))]

        max_float_value = 1.75

        return {
            "required": {
                "image": (sorted(files), {"image_upload_film": True}),
                "weight": ("FLOAT", {
                    "default": 1.2,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
               }),
            }
        }


    CATEGORY = "Zho模块组/🎨 ArtGallery 艺术画廊"

    RETURN_TYPES = ("STRING", "IMAGE",)
    RETURN_NAMES = ("name", "image",)
    FUNCTION = "films_image"

    def films_image(self, image, weight=1):
        image_full_name = image
        image_name = image_full_name.rsplit('.', 1)[0]

        image_path =  get_img_path(image_name, "films")
        img = Image.open(image_path)
        output_images = []
        output_masks = []
        for i in ImageSequence.Iterator(img):
            i = ImageOps.exif_transpose(i)
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))

        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        prompt = []

        if weight > 0:
            P_film = f"({image_name}:{round(weight, 2)})"
            prompt.append(P_film)

        return (P_film, output_image,)


    @classmethod
    def IS_CHANGED(s, image):
        image_path = get_img_path(image_name, "films")
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

class MovementsImage_Zho:
    @classmethod
    def INPUT_TYPES(s):
        p = os.path.dirname(os.path.realpath(__file__))
        movementsimg_dir = os.path.join(p, 'img_lists/movements/')
        files = [f for f in os.listdir(movementsimg_dir) if os.path.isfile(os.path.join(movementsimg_dir, f))]

        max_float_value = 1.75

        return {
            "required": {
                "image": (sorted(files), {"image_upload_movement": True}),
                "weight": ("FLOAT", {
                    "default": 1.2,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
               }),
            }
        }


    CATEGORY = "Zho模块组/🎨 ArtGallery 艺术画廊"

    RETURN_TYPES = ("STRING", "IMAGE",)
    RETURN_NAMES = ("name", "image",)
    FUNCTION = "movements_image"

    def movements_image(self, image, weight=1):
        image_full_name = image
        image_name = image_full_name.rsplit('.', 1)[0]

        image_path =  get_img_path(image_name, "movements")
        img = Image.open(image_path)
        output_images = []
        output_masks = []
        for i in ImageSequence.Iterator(img):
            i = ImageOps.exif_transpose(i)
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))

        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        prompt = []

        if weight > 0:
            P_movement = f"({image_name}:{round(weight, 2)})"
            prompt.append(P_movement)

        return (P_movement, output_image,)


    @classmethod
    def IS_CHANGED(s, image):
        image_path = get_img_path(image_name, "movements")
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()


class StylesImage_Zho:
    @classmethod
    def INPUT_TYPES(s):
        p = os.path.dirname(os.path.realpath(__file__))
        stylesimg_dir = os.path.join(p, 'img_lists/styles/')
        files = [f for f in os.listdir(stylesimg_dir) if os.path.isfile(os.path.join(stylesimg_dir, f))]

        max_float_value = 1.75

        return {
            "required": {
                "image": (sorted(files), {"image_upload_style": True}),
                "weight": ("FLOAT", {
                    "default": 1.2,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
               }),
            }
        }


    CATEGORY = "Zho模块组/🎨 ArtGallery 艺术画廊"

    RETURN_TYPES = ("STRING", "IMAGE",)
    RETURN_NAMES = ("name", "image",)
    FUNCTION = "styles_image"

    def styles_image(self, image, weight=1):
        image_full_name = image
        image_name = image_full_name.rsplit('.', 1)[0]

        image_path =  get_img_path(image_name, "styles")
        img = Image.open(image_path)
        output_images = []
        output_masks = []
        for i in ImageSequence.Iterator(img):
            i = ImageOps.exif_transpose(i)
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))

        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        prompt = []

        if weight > 0:
            P_style = f"({image_name}:{round(weight, 2)})"
            prompt.append(P_style)

        return (P_style, output_image,)


    @classmethod
    def IS_CHANGED(s, image):
        image_path = get_img_path(image_name, "styles")
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()


NODE_CLASS_MAPPINGS = {
    "ArtGallery_Zho": ArtGallery_Zho,
    "ArtistsImage_Zho": ArtistsImage_Zho,
    "CamerasImage_Zho": CamerasImage_Zho,
    "FilmsImage_Zho": FilmsImage_Zho,
    "MovementsImage_Zho": MovementsImage_Zho,
    "StylesImage_Zho": StylesImage_Zho,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ArtGallery_Zho": "🎨 ArtGallery_Zho",
    "ArtistsImage_Zho": "🎨 ArtistsGallery_Zho",
    "CamerasImage_Zho": "🎨 CamerasGallery_Zho",
    "FilmsImage_Zho": "🎨 FilmsGallery_Zho",
    "MovementsImage_Zho": "🎨 MovementsGallery_Zho",
    "StylesImage_Zho": "🎨 StylesGallery_Zho",

}



