# Computational Photography Project
Team : Ewan André Golfier, Ulysse Widmer, Mariia Eremina

## Project : Feature Visualization - Robust Neural Networks
<img width="1126" alt="Screenshot 2023-08-22 at 11 56 24" src="https://github.com/marerem/Feature-Visualization-of-Robust-Neural-Networks/assets/101661237/cc330649-f21b-43da-bf3f-7eadefdba3af">
This project aims to employ feature visualization techniques(this part is the reproduction work of Google Brain Team : https://distill.pub/2017/feature-visualization/) to analyze sensitive neurons, channels, or layers in both robust and non-robust neural networks. Specifically, we will focus on the ResNet34 model and compare its non-robust variant obtained from the PyTorch library with the robust variant obtained from Robust.Art. To identify the sensitive neurons, we will generate adversarial images using the validation dataset of ImageNet100 to deceive the models. Subsequently, we will compare and contrast the feature visualizations of the sensitive neurons across the different models.

**This is one of the final results of comparing the feature visualizations of the sensitive neurons across the robust and not-robust models:**
<img width="873" alt="Screenshot 2023-08-22 at 12 05 20" src="https://github.com/marerem/Feature-Visualization-of-Robust-Neural-Networks/assets/101661237/3a36f051-4279-4e3d-851d-aae8e18fe4a7">


### Literature review
You can find a literature review in the corresponding folder. There is (should be) a list of the papers we read as well as short descriptions in [`literature-review/README.md`](literature-review/README.md).


### Project Notebook
The code of the project can be found in `project.ipynb` which can be run locally as a Jupyter Notebook. The notebook will download the robust resnet34 model from [Robust.Art](http://robust.art) (~250MB)

### DATA FOLDER
The data folder will generate, populate and maintain itself automagically when you run the notebook. Don't push it on Git please.

**A downloadable version of the generated data is available here :** https://drive.belle-ferme.ch/index.php/s/XdrixzBNbeqtHiS/download/data.zip
