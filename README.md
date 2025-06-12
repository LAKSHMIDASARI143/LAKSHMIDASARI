
# 🌾 Crop Recommendation Website

This is a web-based crop recommendation system for farmers. It uses soil and weather inputs to predict the most suitable crop to grow.

## 🚀 Features

- Collects user input for soil, NPK, pH, temperature, humidity, etc.
- Uses a trained ML model to recommend crops.
- Built using Python (Flask) for backend, HTML/CSS for frontend.

## 📁 Project Structure

```
crop-recommendation/
├── app.py                  # Flask backend
├── crop_model.pkl          # Trained ML model (you must add this file)
├── templates/
│   └── form.html           # Input form
└── README.md               # Project info
```

## ⚙️ How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/crop-recommendation.git
   cd crop-recommendation
   ```

2. Install dependencies:
   ```bash
   pip install flask scikit-learn numpy
   ```

3. Make sure `crop_model.pkl` is present in the root folder.

4. Run the app:
   ```bash
   python app.py
   ```

5. Visit `http://127.0.0.1:5000` in your browser.

## 🧠 Dataset and Model

You can train the model using your own data or use existing dataset like `crop_recommendation.csv`.

## 🧑‍💻 Developed for BCDES Rural Farmers
