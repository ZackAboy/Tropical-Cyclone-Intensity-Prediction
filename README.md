<h1>TCI-Net: A Deep Learning Approach for Tropical Cyclone Intensity Prediction</h1>

<p>
  <a href="https://github.com/ZackAboy/Tropical-Cyclone-Intensity-Prediction">
    <img src="https://img.shields.io/badge/Project-TCI--Net-blue.svg" alt="TCI-Net">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  </a>
  <a href="https://www.tensorflow.org/">
    <img src="https://img.shields.io/badge/TensorFlow-2.x-green.svg" alt="TensorFlow">
  </a>
</p>

<hr>

<h2>Abstract</h2>
<p>
  Tropical cyclones (TCs) are among the most devastating weather phenomena, causing extensive damage and loss of life. Accurate intensity prediction is critical for timely warnings and disaster management. In this work, we propose <strong>TCI-Net</strong>, a deep learning approach that leverages geostationary satellite imagery to predict TC intensity. Our model utilizes a modified Convolutional Neural Network (CNN) architecture with tailored pre-processing (including middle-cropping and channel selection) to extract robust features from infrared (IR) and passive microwave (PMW) channels. Experiments on a benchmark dataset demonstrate that TCI-Net achieves competitive performance compared to state-of-the-art models while exhibiting remarkable stability.
</p>
<p>
  <strong>Read the full research paper</strong>
  <a href="https://ieeexplore.ieee.org/abstract/document/10276163?casa_token=Ikpt8oee25wAAAAA:tQrygcGThvm6mqwuCj2z9otam6DRz_-vr_kKNvUsuEhmMPS8_M6ZGx2gfC_szTJPQpfg5RYVKA" target="_blank">here</a>
</p>

<hr>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#introduction">Introduction</a></li>
  <li><a href="#background-and-related-works">Background and Related Works</a></li>
  <li><a href="#proposed-system">Proposed System</a></li>
  <li><a href="#data-preprocessing">Data Preprocessing</a></li>
  <li><a href="#tci-net-architecture">TCI-Net Architecture</a></li>
  <li><a href="#results">Results</a></li>
  <li><a href="#conclusion">Conclusion</a></li>
</ul>

<hr>

<h2 id="introduction">Introduction</h2>
<p>
  Tropical cyclones (also known as hurricanes or typhoons) have a profound impact on communities worldwide. With the increased frequency of extreme weather events due to climate change, accurately predicting TC intensity is more important than ever. Traditional methods rely on a combination of meteorological instruments and manual feature extraction, but these approaches face challenges in terms of data availability and real-time accuracy.
</p>
<p>
  Our research introduces <strong>TCI-Net</strong>, a CNN-based model designed specifically for predicting TC intensity using satellite imagery. By automating feature extraction through deep learning, TCI-Net offers a promising alternative to conventional methods and demonstrates competitive performance on a comprehensive dataset.
</p>

<hr>

<h2 id="background-and-related-works">Background and Related Works</h2>
<p>
  <strong>Collaborative and CNN-based Approaches:</strong> Traditional tropical cyclone intensity prediction methods involve statistical models and manual feature engineering. Recent advances have applied CNNs for image-based intensity regression. Prior work has explored various architectures:
</p>
<ul>
  <li>
    Deep CNNs with multiple convolutional and fully connected layers have achieved around 90% accuracy on cyclone images.
  </li>
  <li>
    Multi-dimensional CNNs (2D and 3D) have been utilized to analyze multi-spectral satellite data, achieving RMSE values in the range of 8-11 knots.
  </li>
  <li>
    Hybrid approaches that combine data from multiple channels (IR, PMW, VIS) have been developed, though challenges exist with noisy channels.
  </li>
</ul>
<p>
  <strong>Motivation:</strong> TCI-Net addresses the limitations of prior methods by selecting stable channels (IR and PMW), applying effective image pre-processing, and designing a tailored CNN architecture to capture relevant spatial features for accurate intensity prediction.
</p>

<hr>

<h2 id="proposed-system">Proposed System</h2>
<p>
  <strong>Objective:</strong> Develop a CNN-based model—TCI-Net—that predicts tropical cyclone intensity from satellite images. The model is designed to:
</p>
<ul>
  <li>Extract meaningful features from geostationary satellite imagery.</li>
  <li>Mitigate noise by selecting robust channels and applying middle-cropping.</li>
  <li>Utilize a deep CNN architecture with convolutional, pooling, and fully connected layers to perform regression.</li>
  <li>Provide stable and accurate intensity estimations across multiple regions.</li>
</ul>

<hr>

<h2 id="data-preprocessing">Data Preprocessing</h2>
<p>
  Data preprocessing is crucial for ensuring the quality and consistency of input images. The following steps are applied:
</p>
<ol>
  <li>
    <strong>Middle-Cropping:</strong> Images are cropped to 75x75 pixels to focus on the most informative central region while preserving peripheral details crucial for intensity prediction.
  </li>
  <li>
    <strong>Channel Selection:</strong> Only the IR and PMW channels are used. The IR channel provides temperature data for cloud pattern detection, while the PMW channel offers precipitation and cloud ice content information. The WV channel is dropped to avoid overfitting on correlated features, and the VIS channel is excluded due to instability under varying daylight conditions.
  </li>
  <li>
    <strong>Handling NaN Values:</strong> Missing values are addressed using interpolation and mean substitution techniques, ensuring data integrity and reducing noise.
  </li>
</ol>

<hr>

<h2 id="tci-net-architecture">TCI-Net Architecture</h2>
<p>
  The TCI-Net model is a modified Convolutional Neural Network specifically designed for image-to-intensity regression. Key components include:
</p>

<h3>1. Input Layer</h3>
<p>
  The input to TCI-Net is a pre-processed image of shape 75x75x2, where the two channels represent IR and PMW data.
</p>

<h3>2. Convolutional Layers</h3>
<p>
  TCI-Net comprises four consecutive 2D convolutional layers. Each layer:
</p>
<ul>
  <li>Uses a (3, 3) kernel to extract spatial features.</li>
  <li>Employs the ReLU activation function to introduce non-linearity.</li>
  <li>Gradually increases the number of filters (e.g., from 8 to 64) to capture increasingly complex features.</li>
</ul>

<h3>3. Average Pooling Layers</h3>
<p>
  Average pooling (using 2x2 windows) is applied after each convolutional layer to downsample the feature maps and maintain spatial invariance while reducing computational complexity.
</p>

<h3>4. Fully Connected Layers</h3>
<p>
  After flattening the feature maps, the model uses a series of fully connected layers to learn non-linear combinations of features. The final dense layer outputs a single regression value, which represents the predicted cyclone intensity.
</p>

<details>
  <summary><strong>Model Architecture Diagram (Fig. 2)</strong></summary>
  <p>(Refer to Fig. 2 in the paper for a visual representation of the TCI-Net architecture.)</p>
</details>

<hr>

<h2 id="results">Results</h2>
<p>
  The performance of TCI-Net is evaluated using standard regression metrics across different regions. Below are representative evaluation tables:
</p>

<h3>Table II. Evaluation Metrics of TCI-Net (Region-wise)</h3>
<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Region</th>
      <th>MSE</th>
      <th>RMSE</th>
      <th>MAE</th>
      <th>R<sup>2</sup></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>West Pacific</td>
      <td>101.62</td>
      <td>10.08</td>
      <td>7.75</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>East Pacific</td>
      <td>72.54</td>
      <td>8.51</td>
      <td>6.32</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>Atlantic</td>
      <td>83.93</td>
      <td>9.16</td>
      <td>6.95</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>Overall</td>
      <td>86.50</td>
      <td>9.30</td>
      <td>7.30</td>
      <td>0.90</td>
    </tr>
  </tbody>
</table>

<h3>Table III. RMSE Values for Each Model (Region-wise)</h3>
<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Model</th>
      <th>West Pacific</th>
      <th>East Pacific</th>
      <th>Atlantic</th>
      <th>Overall</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TCI-Net</td>
      <td>10.08</td>
      <td>8.51</td>
      <td>9.16</td>
      <td>9.30</td>
    </tr>
    <tr>
      <td>CNN-TC</td>
      <td>12.25</td>
      <td>9.42</td>
      <td>9.27</td>
      <td>10.59</td>
    </tr>
    <tr>
      <td>ADT</td>
      <td>12.25</td>
      <td>10.57</td>
      <td>12.87</td>
      <td>11.79</td>
    </tr>
    <tr>
      <td>AMSU</td>
      <td>15.68</td>
      <td>13.76</td>
      <td>11.39</td>
      <td>14.10</td>
    </tr>
    <tr>
      <td>SATCON</td>
      <td>9.90</td>
      <td>8.80</td>
      <td>8.42</td>
      <td>9.21</td>
    </tr>
  </tbody>
</table>

<h3>Table IV. RMSE Values for Each Model (Comparison)</h3>
<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Sr. No.</th>
      <th>Name of the Model</th>
      <th>RMSE (knots)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Kossin et al. (2007)</td>
      <td>13.20</td>
    </tr>
    <tr>
      <td>2</td>
      <td>FASI</td>
      <td>12.70</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Improved DAV-T</td>
      <td>12.70</td>
    </tr>
    <tr>
      <td>4</td>
      <td>TI Index</td>
      <td>9.34</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Y. Zhao et al. (2016)</td>
      <td>12.20</td>
    </tr>
    <tr>
      <td>6</td>
      <td>J. Miller et al. (2017)</td>
      <td>10.00</td>
    </tr>
    <tr>
      <td>7</td>
      <td>R. Pradhan et al. (2017)</td>
      <td>10.18</td>
    </tr>
    <tr>
      <td>8</td>
      <td>ADT</td>
      <td>11.79</td>
    </tr>
    <tr>
      <td>9</td>
      <td>AMSU</td>
      <td>14.10</td>
    </tr>
    <tr>
      <td>10</td>
      <td>SATCON</td>
      <td>9.21</td>
    </tr>
    <tr>
      <td>11</td>
      <td>CNN-TC</td>
      <td>10.59</td>
    </tr>
    <tr>
      <td>12</td>
      <td>CNN-TC (with smoothing)</td>
      <td>9.45</td>
    </tr>
    <tr>
      <td>13</td>
      <td>TCI-Net</td>
      <td>9.30</td>
    </tr>
  </tbody>
</table>

<p>
  Figures in the paper depict scatter plots comparing actual vs. predicted intensities for different regions (Atlantic, East Pacific, and West Pacific) using TC data from 2015–2016.
</p>

<hr>

<h2 id="conclusion">Conclusion</h2>
<p>
  This research presents <strong>TCI-Net</strong>, a CNN-based model for tropical cyclone intensity prediction using satellite imagery. By implementing tailored data preprocessing, robust channel selection, and a modified CNN architecture, TCI-Net achieves competitive performance with an RMSE of 9.30 knots—comparable to state-of-the-art methods like SATCON. The model not only outperforms many existing approaches but also offers a stable, automated solution for intensity estimation. Future work may extend the system to predict additional cyclone characteristics, such as TC size, and explore real-time deployment for improved disaster management.
</p>
