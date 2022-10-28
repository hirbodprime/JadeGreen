$(document).ready(function () {
    $.ajax({
        method : 'GET',
        url : 'https://jadegreen.pythonanywhere.com/JadeShop/',
        success : function (result)
        {
            var array = result.results;
            var contents = "";
            for(var i = 0 ; i < array.length ; i++){
                var product = array[i];
                console.log(product);
                contents += `
                <div class="product swiper-slide">
                    <div class="offer-badge">
                        <span class="takhfif">30%</span>
                    </div>
                    <img src="${product.image}" class="product-image img-fluid">
                    <p class="husky-bird">${product.name}</p>

                    <div class="span-price">
                        <span class="price">${product.offer} هزار تومان</span>
                        <span class="price last-price">${product.price} هزار تومان</span>
                    </div>
                </div>
                `
            }
            $('.product-model').html(contents);
        }
    })
    $.ajax({
        method : 'GET',
        url : 'https://jadegreen.pythonanywhere.com/JadeActivity/',
        success : function (result)
        {
            var array = result.results;
            var contents = "";
            for(var i = 0 ; i < array.length ; i++){
                var activity = array[i];
                contents += `
                <div class="swiper-slide category">
                    <div class="CatImage">
                        <img src="${activity.image}" class="category-image img-fluid">
                        <p class="text-image">${activity.name}</p>
                    </div>
                </div>
                `
            }
            $('.activities-model').html(contents);
        }
    })
    $.ajax({
        method : 'GET',
        url : 'https://jadegreen.pythonanywhere.com/JadeBlog/',
        success : function (result)
        {
            var array = result.results;
            var contents = "";
            for(var i = 0 ; i < array.length ; i++){
                var blog = array[i];
                contents += `
                <div class="guide col-lg-4 col-md-6 col-sm-12 mx-auto">
                <img class="img-fluid" src="${blog.image}">
                <div class="content">
                  <h3> ${blog.name}</h3>
                  <p>${blog.discription}</p>
                  <div class="div-actions">
                    <p class="actions">نویسنده : احمدرضا سلیمانی</p>
                    <div class="row">
                      <div class="col-3">
                        <p >12 شهریور </p>
                      </div>
                      <div class="col-6"></div>
                      <div class="col-3 d-md-none d-sm-block text-more">
                        <span>بیشتر</span>
                        <i class="material-symbols-outlined">keyboard_backspace</i>
                      </div>    
                    </div>
                  </div>
                </div>
              </div>
        
                `
            }
            $('.guides').html(contents);
        }
    })
})