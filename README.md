# Awarded Modeling Competition Solution
This is the Winner solution to the UCM Business Modeling Competition of 2024 in Machine Learning held at the Universidad Complutense de Madrid in Spain in cooperation with the company GMV Innovating Solutions SL.
## Competition Website
This is the link to the website where the competition is published: [UCM Business Modeling Competition](https://matematicas.ucm.es/concurso2023-24)
## Team
The team who won the competition was the team _Platanos_Canarias_ formed by Gonzalo García Fernández, Sergio Javier Hernando Rivero, Jon Mañueco Rubio  and me, Lucas Martín García.
## **Solution**
This document provides a comprehensive overview of a groundbreaking project aimed at the classification and generation of fruit images, with a special focus on a diverse dataset of 33 fruit type. Employing state-of-the-art machine learning algorithms, our team has developed a sophisticated fruit classifier that demonstrates exceptional accuracy and efficiency.  
The Final Report of this project containing all the details is located in the file [Final Report](https://github.com/lucasmg18/Awarded-Modeling-Competition/blob/main/PROJECT%20REPORT/memoria_platanos_canarias.pdf) of this repository.

#### **Data Preprocessing**
The initial phase of the project involved meticulous data preprocessing, where images were converted into 100x100x3 pixel matrices to represent the RGB values. Labels were transformed using OneHotEncoding, eliminating ordinal relationships between classes and preventing inference biases. The dataset, characterized by its high quality and noise-free images against a white background, did not require class balancing or normalization, simplifying the preprocessing steps.
#### **Classification Model**
Our classification approach utilized a convolutional neural network (CNN), a choice driven by its proven effectiveness in image recognition tasks. The model was trained on the preprocessed dataset, ensuring a robust framework capable of accurately distinguishing between the 33 fruit types. The data preprocesing together with the final CNN model are described and implemented in the file [Modelo Clasificacion](https://github.com/lucasmg18/Awarded-Modeling-Competition/blob/main/CODE/Modelo_clasificacion.ipynb). An exhaustive hyperparameter grid-search was undertaken to ensure the optimal hyperparameter for our model. This grid-search evaluation is located in the file [Modelo Eleccion Hiperparametros](https://github.com/lucasmg18/Awarded-Modeling-Competition/blob/main/CODE/Modelo_eleccion_hiperparametros.ipynb) of this repository.

#### **Data Augmentation and Generation**
Given the constraints posed by a limited dataset, innovative strategies were employed to enrich the data pool. Data augmentation techniques, including geometric transformations and color adjustments, were applied to a subset of the original dataset, effectively increasing its size and diversity. This process utilized the Albumentations library, allowing for a wide range of image modifications.

Furthermore, the project explored the potential of Generative Adversarial Networks (GANs) for synthetic data generation. The GAN architecture comprised a generator and discriminator working in tandem to produce high-quality, realistic fruit images. This approach not only expanded our dataset but also provided valuable insights into the capabilities and limitations of synthetic data in machine learning applications.  
This part is described and implemented in the files [Modelo Data Augmentation](https://github.com/lucasmg18/Awarded-Modeling-Competition/blob/main/CODE/Modelo_generacion_data_augmentation.ipynb), [Modelo Generacion Gan](https://github.com/lucasmg18/Awarded-Modeling-Competition/blob/main/CODE/Modelo_generacion_gan.ipynb).

#### **Experimental Results and Evaluation**
The effectiveness of our classification model was rigorously tested using various datasets, including the original, augmented, and GAN-generated ones. The evaluation metrics employed, such as accuracy, F1-score, and sensitivity, demonstrated the model's exceptional performance, when trained on the original dataset and also in the augmented datasets generated.  
In the following table we can see the results, scored by the chosen metrics, of the CNN Classification Model trained with the different datasets including the original dataset and the generated datasets of the solution:
| Utilized Dataset    | Test Error    | Accuracy | F1-Score | Sensitivity | Custom Metric         |
|---------------------|---------------|----------|----------|-------------|-----------------------|
| Original Dataset    | 0.024357      | 0.993177 | 0.992709 | 0.991694    | 0.992884              |
| Generated Dataset 1 | 1.526816      | 0.899436 | 0.878473 | 0.898398    | 0.896136              |
| Generated Dataset 2 | 0.923319      | 0.883862 | 0.868885 | 0.879858    | 0.881015              |
| Generated Dataset 3 | 1.506544      | 0.866953 | 0.845595 | 0.863690    | 0.863260              |


#### **Conclusion and Future Directions**
This project represents a significant advancement in fruit classification and synthetic data generation. The successful implementation of CNNs, combined with innovative data augmentation and GAN techniques, has established a robust framework for similar tasks in the field of machine learning and computer vision.

Our findings underscore the potential of synthetic data to supplement training datasets, although the computational costs associated with GANs suggest a cautious approach. Future work will explore the optimization of GAN architectures and further investigate the integration of synthetic data in machine learning pipelines.

This project sets a precedent for the effective use of advanced machine learning techniques in agricultural and food technology sectors, paving the way for more efficient and accurate classification systems.





## Data
### Fruit Types
The original data of the problem is uploaded to the following website: [Fruit Classification](https://www.kaggle.com/datasets/sshikamaru/fruit-recognition/data)  
This consists of a dataset of photos of different types of fruits.
### New Datasets Generated
One of the main goals of this competition was to create a new dataset solely based on a very small set of data to be able to train a machine learning model and achieve a result similar to that obtained from the original dataset.  
The datasets generated with the different methods we have implemented are abailable in the following website: [Datasets Generated](https://www.kaggle.com/datasets/lucasmartingarcia/modeling-competition-generated-datasets/data)
