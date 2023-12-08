# Royce_Hall

## Project Summary
We use CNNs for an image binary classification task. We want to be able to classify whether or not an image of a building is Royce Hall or not. Using our model, we achieved a final train accuracy of $0.9718$ and a validation accuracy of $0.9375$. 

## Pipeline
- Take pictures of Royce Hall using own phones
- Preprocess and augment images for classification
- Input processed into model
- Predict!
- Evaluate results

## Dataset
We used pictures taken of Royce Hall and the dataset from [the University of Salford](https://salford.figshare.com/articles/dataset/UoS_Buildings_Image_Dataset_for_Computer_Vision_Algorithms/20383155), which we used for our negative class. See the `dataset/` folder in the repository. 

## How to Run

### Prerequisites
- Python 3.x
- TensorFlow 2.x
- Keras

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TonyLei43/Royce_Hall
   ```
2. Navigate to the project directory:
   ```bash
   cd Royce_Hall
   ```

### Running the Model
1. Run the notebook `model.ipynb`

> [!IMPORTANT]
> Make sure the `dataset/` folder is in the same location as `model.ipynb`.


## Demo
For a live demonstration of the project, [click here](https://roycehall.streamlit.app/).

This was a final project for Math 156 MAchine Learning at UCLA.


