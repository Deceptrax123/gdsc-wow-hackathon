# Death Clock

## Disclaimer
Use the [pre-trained models](https://github.com/Deceptrax123/gdsc-wow-hackathon/blob/master/model_train.ipynb) instead of building your own model for the hackathon


This repository contains the boilerplate code for the [Mortality Dataset](https://www.kaggle.com/datasets/rajanand/mortality). You can refer to the kaggle workspaces to fetch/download your data.


## Description of files
|FileName| Functionality|
| --- |---|
|[App.py](https://github.com/Deceptrax123/gdsc-wow-hackathon/blob/master/app.py) | Contains the HTTP server |
| [model-train.ipynb](https://github.com/Deceptrax123/gdsc-wow-hackathon/blob/master/model_train.ipynb)| Notebook for training|
|[model.json](https://github.com/Deceptrax123/gdsc-wow-hackathon/blob/master/model.json) | Saved model|
|[model.h5](https://github.com/Deceptrax123/gdsc-wow-hackathon/blob/master/model.h5) | Saved weights of the previous training|
|[Requirements.txt](https://github.com/Deceptrax123/gdsc-wow-hackathon/blob/master/Requirements.txt)|Dependencies used| 

## Flow
- **Install dependencies**
```bash
pip install -r requirements.txt
```
- **Test the server**
```bash
python app.py
```
- **Train the model**
Open the Jupyter Notebook and tune the model for higher accuracy
- **Save the model**
```python
model.save()
```
- **Test the model**
- Deploy it

## Reccomenedations

Once you've completed tuning the model for higher accuracy, you can train the model on:
- [Azure ML](https://ml.azure.com)
- [Amazon Sagemaker](https://aws.amazon.com/sagemaker/)
- [Kaggle Worksapces](https://www.kaggle.com/getting-started/106737)
- [Google's Colab](https://colab.research.google.com/)

