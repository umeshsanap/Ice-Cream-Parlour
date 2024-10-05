{% extends 'base.html' %}

{% load static %}  <!-- Load static files -->

{% block title %} Home {% endblock title %}

{% block body %}
<div id="carouselExampleCaptions" class="carousel slide mt-4">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{% static 'img/img1.png' %}" class="d-block w-100" alt="First slide">
      <div class="carousel-caption d-none d-md-block">
        <h2 class="text-dark bg-light p-2 d-inline">Chill & Thrill: Sweet Moments at Sunset</h2>
      </div>
    </div>
    <div class="carousel-item">
      <img src="{% static 'img/img2.png' %}" class="d-block w-100" alt="Second slide">
      <div class="carousel-caption d-none d-md-block">
        <h2 class="text-dark bg-light p-2 d-inline">Rise & Shine: A Sweet Start to Your Day</h2>
      </div>
    </div>
    <div class="carousel-item">
      <img src="{% static 'img/img3.png' %}" class="d-block w-100" alt="Third slide">
      <div class="carousel-caption d-none d-md-block">
        <h2 class="text-dark bg-light p-2 d-inline">Life is like ice cream; it’s better enjoyed at sunset!</h2>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
<div class="container" style="display : flex">
  <div class="row1">
    <div class="col-12">
      <img src="{% static 'img/ProfiteOfIceCreame.png' %}" class="img-thumbnail mt-5" alt="Ice Cream Image" style="height: 450px; width: auto;">
    </div>
  </div>
  <div class="row2">
    <div class="col-12">
      <div>
        <h2 class="mt-5 ms-5">Why Ice Cream is More Than Just a Dessert?</h2>
        <ul class="mt-3 ms-5">
          <li style = "font-size : 17px"><b>Mood Booster:</b> Indulging in ice cream can elevate your mood, thanks to its sweet and comforting flavors.</li><br>
          <li style = "font-size : 17px"><b>Calcium Source:</b> Ice cream provides a delicious way to boost your daily calcium intake, supporting strong bones and teeth.</li><br>
          <li style = "font-size : 17px"><b>Energy Boost:</b> Packed with carbohydrates, ice cream offers a quick source of energy to fuel your day.</li><br>
          <li style = "font-size : 17px"><b>Nutritional Value:</b> Ice cream contains essential nutrients like vitamins and minerals that can contribute to your overall health.</li> <br>
          <li style = "font-size : 17px"><b>Cooling Effect:</b> A cold scoop of ice cream is a refreshing treat that helps cool you down on hot days.</li> <br>
          <li style = "font-size : 17px"><b>Social Enjoyment:</b> Ice cream is a perfect treat for sharing, bringing people together for joyful moments.</li>
        </ul>
      </div>
    </div>
  </div>
</div>
<div class="container" style="display : flex">
  <div class="row1">
    <div class="col-12">
      <div>
        <h2 class="mt-5 ">Is It Safe to Eat Expired Ice Cream?</h2>
        <ul class="mt-3 ">
          <li style = "font-size : 17px"><b>Growth of Harmful Bacteria:</b> Expired ice cream can harbor bacteria like Listeria, Salmonella, and E. coli, which cause severe foodborne illnesses.</li><br>
          <li style = "font-size : 17px"><b>Formation of Harmful Gases:</b> As ice cream spoils, it can produce gases like ammonia, carbon dioxide, and hydrogen sulfide, leading to bad odors and potential health risks.</li><br>
          <li style = "font-size : 17px"><b>Toxins Produced by Bacteria:</b> Certain bacteria can produce heat-stable toxins that remain harmful, even if the ice cream is refrozen.</li><br>
          <li style = "font-size : 17px"><b>Loss of Nutritional Value:</b> Expired ice cream loses essential nutrients over time, reducing its health benefits.</li> <br>
          <li style = "font-size : 17px"><b>Off-Taste and Odor:</b> Spoiled ice cream develops a rancid taste and smell, making it unpleasant and unsafe to consume.</li> <br>
        </ul>
      </div>
    </div>
  </div>
  <div class="row2">
    <div class="col-12">
      <img src="{% static 'img/ExpiryDate.webp' %}" class="img-thumbnail mt-5 ms-5" alt="Ice Cream Image" style="height: 450px; width: auto;">
    </div>
  </div>
</div>
{% endblock body %}