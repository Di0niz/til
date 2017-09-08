Для того, чтобы отображать SVG структуру в 1С:Предприятии, необходимо осуществить конвертацию SVG в PNG. Это можно сделать одним из следующих способов:
* Библиотека ImageMagic;
* Internet Explorer;

Для использования браузера, необходимо добавить поддержку HTML5.

```html
<meta http-equiv="X-UA-Compatible" content="IE=9">
```

Вставляем в поле HTML Документа вызов и генерацию файла SVG:

``` html
<!DOCTYPE html>
<html>
<meta http-equiv="X-UA-Compatible" content="IE=9"> 
<body>

<canvas id="canvas" style="border:2px solid black;" width="200" height="200"></canvas>
<span id="BufferData">js_result</span>
<script>
	var canvas = document.getElementById("canvas");
	var ctx = canvas.getContext("2d");
	var data =  "data:image/svg+xml;utf8," +
	           	"<svg width='200' height='200'>" + 
	  		 	"<circle cx='50' cy='50' r='40' stroke='green' stroke-width='4' fill='yellow' />" + 
				 "</svg>";
// Ширина и высота холста
var width = ctx.canvas.width;
var height = ctx.canvas.height;
            
// Радиус и центр круга
var radius = 0.4 * width;
var cx = width / 2;
var cy = height / 2;
            
// Делаем путь для круга от 0 до 2PI
ctx.beginPath();
ctx.arc(cx, cy, radius, 0, Math.PI * 2);
ctx.closePath();
            
// Устанавливаем отрисовку с тенью
ctx.shadowBlur = 10;
ctx.shadowColor = "black";
            
// Устанавливаем ширину и цвет линии и отрисовываем
ctx.lineWidth = 25;
ctx.strokeStyle = "#f00";
ctx.stroke();
            
// Убираем тень
ctx.shadowColor = "transparent";
            
// Создаем радиальный градиент для заливки
var gradient = ctx.createRadialGradient(cx, cx, 0, cx, cy, radius);
gradient.addColorStop(0, "#ddd");
gradient.addColorStop(1, "#eee");
            
// Устанавливаем градиент и делаем заливку
ctx.fillStyle = gradient;
ctx.fill();
            
// Устанавливаем стили текста и центрирование
ctx.textAlign = "center";
ctx.textBaseline = "middle";
ctx.font = "bold 55px 'Segoe UI', 'Tahoma', sans-serif";
ctx.fillStyle = "#333";
            
// Выводим надпись
ctx.fillText("STOP", cx, cy);

//	var img = new Image();
//	img.src = data;
//	img.onload = function() { ctx.drawImage(img, 0, 0); }

	var data = canvas.toDataURL("image/png");
	var buf = document.getElementById("BufferData");
	buf.innerText = data;
</script>

</body>
</html>

```
Используем буфер "BufferData" для хранения данных картинки в формате base64.

Потом через id документа осуществляем конвертацию:

```bsl
Функция ПолучитьДвоичныеДанныеPNG(canvas)
	дд = Base64Значение(Сред(canvas,23));
	возврат дд
КонецФункции
```
