## Анимированное меню с кареткой

Определяем перечень элементов меню и внешний вид картетки.

```html
<div>
  <div class="carpet">
    lll
  </div>
  <UL>
  <li class="active">elem1</li>
  <li>elem2</li>
  <li>elem3</li>
  <li>elem4</li>
 </ul>
</div>
```

```css
/* Элементы меню располагаем горизонтально, с отступом в 10 px */
li {
  display: block;
  float: left;
  margin-right: 10px;
}

/* определяем стиль текущего элемента, требуется для отладки */
.active {
  background-color: red;
}

/* внешний вид каретки, позиционирование любое, индекс верхний
по умолчанию не отображаем */
.carpet {  
  background-color: red;
  position: absolute;
  z-index: 1;
  display:none;
}
```

```js
//  перехватываем событие мыши
$( "li" ).click(function() {
  // снимаем текущее выделение
  $(".active").removeClass("active");
  
  // устанавливаем выделение текущего элемента
  $(this).addClass("active");
 
  // так каретка по умолчанию не отображает, то показываем
  $( ".carpet").show();
  // делаем анимацию для перемещения элемента слево
  $( ".carpet").animate({'left':$(this).offset().left}, "easy");
  
  
});
```
