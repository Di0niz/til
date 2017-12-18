## Настройки для приложения 

Команды для Visual Studio Code для формирования схемы:




## Оформление стилей

Пример отображения схемы в стиле ARIS

```dot
digraph G {
    {
        // start
        node [shape="point",style="filled", color="mediumblue", fillcolor="cornflowerblue"]
    }
    {
        // stop
        node [rounded="ellipse",style="filled", color="mediumblue", fillcolor="cornflowerblue"]

    }

    {
        // data
        node [shape="parallelogram",style="filled", color="darkblue", fillcolor="dodgerblue"];
    }

    {
        // process
        node [shape="box",style="filled", color="gold", fillcolor="yellow"];
    }    

    {
        // decision
        node [shape="diamond",style="filled", color="limegreen", fillcolor="palegreen"]
    } 
    
    {
        // document
        node [shape="note",style="filled", color="forestgreen", fillcolor="limegreen"]
    }  

    {
        // DirectData 
        node [shape="cylinder",style="filled", color="olive", fillcolor="darkkhaki"]
    }  

}
```
