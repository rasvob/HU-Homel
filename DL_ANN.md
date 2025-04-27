# Final Project Information [🠔](https://homel.vsb.cz/~svo0175/)
* You can get **20 to 40** points

* 🎯 Goal of the final project is to create more thorough analysis of the chosen dataset compared to the previous two smaller projects
  
* 💡 The dataset selection is up to you however it must come from image, text or time series domain

* 📒 Every project must include brief description of the dataset so you get to know the data you are working with
  * Number of instances, number of classes and class balance information
  * Examples of the data

* 🔎 What model performance metrics have you decided to use?
  * e.g. Accuracy, Precision, Recall, F1-score etc.
  * 📒 State which one of the scores is the most important from your point of view given the class balance, task, ... in a Markdown cell!

* 🎯 Try multiple different deep learning models
  > 🚀 **Creativity is king in the final project**

  * The first models should be built from scratch, i.e. create your own architecture and train the models to have some baseline results
    * 💡 The project will include hyper parameter tuning so try different batch sizes, optimizers, etc. and document everything accordingly
      * i.e. 📒 Tables with results, plots, ...
      * 💡 Using hyperparameter optimization frameworks like [Optuna](https://optuna.org/) is **highly recommended** for efficient tuning
  * 🚀 Other models will employ transfer learning techniques
      * 💡 Try to fine-tune multiple pre-trained models:
        * For image data: Use pre-trained models from Keras applications (ResNet, EfficientNet, etc.) and YOLO variants
        * For text data: Leverage HuggingFace Transformers and word embeddings like GloVe, FastText, or Word2Vec
      * You can also try to pre-process the data if needed, use re-sampling, data augmentation and so on
  * 📊 Implement experiment tracking for better organization and reproducibility
      * 💡 Consider using tracking tools like [Comet ML](https://www.comet.ml), [Neptune.ai](https://neptune.ai), [Weights & Biases](https://wandb.ai), or [MLflow](https://mlflow.org) or [TensorBoard](https://www.tensorflow.org/tensorboard)
      * Document model versions, hyperparameters, and performance metrics systematically
      * Create visualization dashboards to compare experiment results efficiently
  * 📌 **Compare the models and summarize your results**
  * 🚀 Create a deployment-ready inference pipeline
      * Select one of your models and export it (e.g., ONNX)
      * Implement a simple inference class with a `predict` method that:
        * Takes raw input data
        * Applies necessary preprocessing steps
        * Feeds the processed data to the model
        * Returns formatted predictions
      * Document the pipeline usage with examples

## General Information
**✅ Mandatory part of every project is a summary at the end in which you summarize the most interesting insight obtained**.
  
Upload a **📝 Jupyter Notebook with descriptions included** or a PDF report + source codes.

💡 Estimated time for the project is 10-15h, this value heavily depends on your skill, but you can use it as a guidance for a project size.

> #### **🎯 Deadline is 8. 6. 2025 🍀**
  
**Upload the project to:**

* Dropbox:
  * Mon, 09:00: [Dropbox](https://www.dropbox.com/request/ZCgxEExv1BrwfJQZCkHZ)
  * Wed, 14:15: [Dropbox](https://www.dropbox.com/request/WL0w5GRX1YgT3vM1PDEk)

* **💡 Dropbox will ask you for your name - use your VSB login please 👍**
  
* 🎯 The final project will be presented, please choose one of the proposed dates using the Google Form URL - [https://forms.gle/JmoNaWx7dL2QJsGJ9](https://forms.gle/JmoNaWx7dL2QJsGJ9)
  * There are 18 slots for each day
    * **Please, check the table linked to the form if there is a free slot before you choose the day 👍**

## Dataset
>  *Select a dataset of your individual choice at [Kaggle](https://www.kaggle.com/) (or other data source) and drop me an email so I can approve your choice or give some recommendation.*


> **If you work with DL in your semestral project, it is possible to use this in this project as well. Just drop me an email and we will solve it individually.**