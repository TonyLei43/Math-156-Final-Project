# Math-156-Final-Project

## Project Summary
We use CNNs for an image binary classification task. We want to be able to classify whether or not an image of a building is Royce Hall or not. Using our model, we achieved a final train accuracy of $0.9718$ and a validation accuracy of $0.9375$. 

## Pipeline
- Take pictures of Royce Hall using own phones
- Preprocess and augment images for classification
- Input processed into model
- Predict!
- Evaluate results

## How to Run

### Prerequisites
- Python 3.x
- TensorFlow 2.x
- Keras

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TonyLei43/Math-156-Final-Project
   ```
2. Navigate to the project directory:
   ```bash
   cd Math-156-Final-Project
   ```

### Running the Model
1. Run the notebook `model.ipynb`

> [!IMPORTANT]
> Make sure the `dataset/` folder is in the same location as `model.ipynb`.


## Demo
For a live demonstration of the project, [click here](https://roycehall.streamlit.app/).


