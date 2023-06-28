import os
import wget
import torch
import torchinfo
import gc
from PIL import Image
import numpy as np
import string
from lucent.modelzoo.util import get_model_layers


from lucent.misc.io.showing import images, _image_url
from lucent.optvis import render

from torch.utils.data import Dataset
import torchvision.transforms as T


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

data_folder_url = "https://drive.belle-ferme.ch/index.php/s/XdrixzBNbeqtHiS/download/data.zip"


# empties GPU unused memory to be able to compute more stuff
def cleanMemGPU():
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def print_model_info(model):
    # get name of every layer
    model_layers = get_model_layers(model)
    print(len(model_layers), "layers")
    print(model_layers)
    # Get more complete summary of every layer
    torchinfo.summary(model, device=device, verbose=1)


def visualize_channels(channels, model, output_dir, epsilon="", save=True, name=""):
    imgs = []
    for c in channels:
        # visualize 5 channels from robust model
        if name == "":
            f_name =  model.name + "_" + str(c) + str(epsilon) + ".png"
        else:
            f_name = str(name) + ".png"
        f = os.path.join(output_dir, f_name)
        if os.path.exists(f):
            imgs.append(Image.open(f).convert("RGB"))
        else:
            imgs.append(render.render_vis(
                model=model,
                objective_f=c,
                show_inline=False,
                show_image=False,
                save_image=save,
                image_name=f
            ))
    images(imgs, labels=channels)


# redefine lucent animate_sequence function to be able to display multiple sequences
def html_sequence(sequence, domain=(0, 1), fmt='png'):
    steps, height, width, _ = sequence.shape
    sequence = np.concatenate(sequence, 1)
    code = string.Template('''
    <style> 
        #animation${html_id} {
            display: inline-block;
            margin: 5px;
            width: ${width}px;
            height: ${height}px;
            background: url('$image_url') left center;
            animation: play 1s steps($steps) infinite alternate;
        }
        @keyframes play {
            100% { background-position: -${sequence_width}px; }
        }
    </style><div id='animation${html_id}'></div>
    ''').substitute(
        image_url=_image_url(sequence, domain=domain, fmt=fmt),
        sequence_width=width*steps,
        width=width,
        height=height,
        steps=steps,
        html_id=np.random.randint(10000)
    )
    return code


class ImageNet100ValDataset(Dataset):
    def __init__(self, img_dir, size=5000):
        self.img_dir = img_dir
        self.labels = os.listdir(img_dir)[:(size//50)]
        
        mean = (0.485, 0.456, 0.406)
        std = (0.229, 0.224, 0.225)
        self.t1 = T.Compose([
            T.Resize(232),
            T.CenterCrop(224),
            T.ToTensor()
        ])
        self.transforms = T.Compose([
            T.Resize(232),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(mean, std),
        ])

    def __len__(self):
        return len(self.labels) * 50  # 5000 total images

    def __getitem__(self, idx):
        label_idx = int(idx / 50)  # 50 images per label
        img_idx = idx % 50  # idx of img in folder
        
        label = self.labels[label_idx]
        image = Image.open(self.img_dir + "/" + label + "/" + os.listdir(self.img_dir + "/" + label)[img_idx]).convert("RGB")
        
        return self.t1(image), self.transforms(image), label