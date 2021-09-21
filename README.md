# Fish classifier 🐠

Through this project I have created a web application which recognize the fish from Reunion Island's lagoon. The way the application works is simple. (a) The user uploads a photo of a fish. (b) This photo is sent to the Deep Learning algorithm which makes a prediction. (c) This prediction is returned to the user

<h3 align="center">
  <span>🕹 </span>
  <a href="https://share.streamlit.io/axelearning/fish_and_chips/app.py">Test the app</a>
</h3>
<br>

<p align="center">
  <img src='img/app.gif' alt="GIF of the image" width=750>
</p>
<h3 align="center">
  <span>🎣 </span>
  <a href="https://grizzly-cress-b32.notion.site/Fishes-b1e1c38339bc49249cf70fbcb2836944">Fishes used to train the model</a>
</h3>
<br>

Here are the different steps put in place in order to realize this project:

1. Collected the data | [get_the_data.ipynb](https://colab.research.google.com/drive/1ybB06Y8hXg-3iuXqVMnTCBRF4LGhDJCQ?usp=sharing)
2. Trained the model | [modeling.ipynb](https://colab.research.google.com/drive/1UptvOjCSB7BK8Af8NTRGJJm8UPMfy51U?usp=sharing)
3. Built and deploy a web app with streamlit | [app.py](https://github.com/axelearning/fish_and_chips/blob/master/app.py)

## What did I learn?

- **Create my own dataset** by getting pictures from Bing search API
- **Use state of the art deep learning models** : [Resnet50](https://en.wikipedia.org/wiki/Residual_neural_network) and apply **transfer learning** to allow the model to adapt to our problem
- **Understand the errors** and improve its performance
- **Deploy a machine learning application** with Streamlit

## Why this project?

At first to `develop my skills in artificial intelligence` and then to `spend more time with my grandfather`, fan of snorkeling, he spends a lot of time observing the fish. He made me discover his world (🐠) I made him discover mine (🤖)!

After explaining him the project we collected photos in the lagoon together to test the performance of the model in production.

<details><summary><b>Pictures from our expedition</b></summary>
  
  <p align="center">
    <img src='img/pic2.JPG' alt="GIF of the image" width=750>
    <img src='img/pic3.JPG' alt="GIF of the image" width=750>
    <img src='img/pic1.JPG' alt="GIF of the image" width=750>
    <img src='img/pic4.JPG' alt="GIF of the image" width=750>
    <img src='img/pic5.JPG' alt="GIF of the image" width=750>
    <img src='img/pic6.JPG' alt="GIF of the image" width=750>
  </p>

 </details>
