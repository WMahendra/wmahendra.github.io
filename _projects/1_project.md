---
layout: page
<!DOCTYPE html>
<html>
<head>
    <style>
        /* CSS to style the title */
        h1 {
            font-size: 24px;
        }
        
        /* CSS to style the description */
        p {
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1 style="font-size: 20px;">LULC Mapping in Lund Kommun, Sweden</h1>
    <p style="font-size: 14px;">A brief explanation of two different algorithms</p>
    <!-- Add the rest of your content here -->
</body>
</html>

img: assets/img/project1/7.jpg
importance: 1
category: work
related_publications: einstein1956investigations, einstein1950meaning
---

Land cover information plays an important role in various sectors as it can be used to describe the spatial distribution of objects on the land surface Satellite remote sensing has been used for decades to assist land cover mapping activities due to its capability to capture vast areas and constant repetition. To produce land cover mapping, there are two general methods of image classification for land cover studies, namely visual interpretation and digital classification (Rambaldi et al., 2006). Digital classification has the advantage of automating based on pixel values that represent an object. However, field data is needed as input in formulating a classification scheme along with an evaluation of the classified land cover. This study aims to make land cover maps in Lund Kommun by integrating machine learning classification algorithms and field information.
The study area is located in Lund Municipality centered at approximately 13o 21’ 30” E and 55o 42’ 58” N. This region has a temperate climate and relatively flat topography. Additionally, the study area is characterized by agricultural fields and forests, with a small proportion of cover consisting of water bodies and built-up areas.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/project1/1.jpeg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/project1/4.jpeg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/project1/3.jpeg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Field data collections were collected on April 21st 2023. Stratified random sampling combined with purposive sampling were used to assess all the class within the study area. Image on the left represents agricultural area, on the middle represents built up area and on the right is coneferous forest.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/project1/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

Based on the classification scheme and machine learning classification used, in Figure 7, point B, urban areas tend to form clusters on the west side of the study area while point A tends to be sprawled over the study area. There is a significant difference in classification in deciduous forest and cropland between points A and B. Consulting the previous knowledge of the study area, the results from the multi-layer perceptron classification more closely resemble the reality that cropland is the predominant land cover class in the study area. Figure 8 represents the area’s extent of different land cover classes. It is clearly visible that cropland is the most dominant land cover class in the study area in all of the classification types. On the other hand, the water class covers the least portion of the area. Corine land cover has been used as a reference classification to compare the results. In MD classification, urban areas have been underestimated compared to Corine Land cover. Most of the urban areas and some croplands have been misclassified as deciduous and coniferous forests. Moreover, added together, the deciduous and coniferous forests made up more than half of the area (54.11%) of Lunds Kommun. In contrast, MLP classified all of the classes quite accurately. Cropland accounted for the vast majority of users, at 62.23%. Then deciduous forests accounted for 16.36% followed by coniferous and urban areas, 9.32 % and 8.76% respectively. The difference in the areas in every class type between Corine LC and MLP is comparatively very low and therefore the result of MLP is more valid.
To evaluate the accuracy of both algorithms, we used the confusion matrices (Table 1-2). It is clear that MLP is more accurate than MD classification. Overall accuracy in MLP is 82%, which is far better than MD classification, which is 40.3%. Concerning to kappa index, for MD, the value of the kappa coefficient is 0.31, whereas in MLP is 0.72. It is already mentioned that we added NDVI as an input band because the overall accuracy of MD only using four bands was 40.3%. We tested the performance of NDVI in the MD classification and the overall accuracy increased to 56.1% and the kappa index increased to 0.38.
The evaluation of this project is that the field data were collected by various groups. When examining the samples, problems were found such as the sample cover class was located on the edge of two different classes. In addition, remote sensing images used with fieldwork have a three years temporal difference (Figure 9). Therefore, it will be better to utilize remote sensing imagery, that has a closer acquisition time to the field data collection period. Therefore, the results of the classification and accuracy will be better.
The use of supervised classification on Sentinel 2B imagery and field data can be utilized to map land cover in Lund Kommun. The MLP algorithm produces better results for mapping land cover in Lund Kommun, compared to the MD algorithm, which has significantly higher accuracy values. The Cropland class dominates the area in Lund Kommun, while the water class has the smallest coverage. Furthermore, the use of NDVI as the input band enables the model to distinguish vegetation features, thereby increasing the accuracy.


<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/project1/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>


The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}
```html
<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
```
{% endraw %}
