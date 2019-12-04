function usConversion()
{
    
    var cupInput = parseInt(document.getElementById("cups").value);
    var tablespoonInput = parseInt(document.getElementById("tablespoons").value);
    var teaspoonInput = parseInt(document.getElementById("teaspoons").value);

    if(cupInput) {
        var litresOutput = cupInput * 0.2365;
        var millilitresOutput = litresOutput * 1000;

        document.getElementById("litres").value = litresOutput.toFixed(4);
        document.getElementById("millilitres").value = millilitresOutput.toFixed(4);

        document.getElementById("cups").value = "";
        document.getElementById("tablespoons").value = "";
        document.getElementById("teaspoons").value = "";

    }

    if(tablespoonInput)
    {
        var litresOutput = tablespoonInput * 0.0147;
        var millilitresOutput = litresOutput * 1000;

        document.getElementById("litres").value = litresOutput.toFixed(4);
        document.getElementById("millilitres").value = millilitresOutput.toFixed(4);

        document.getElementById("cups").value = "";
        document.getElementById("tablespoons").value = "";
        document.getElementById("teaspoons").value = "";
    }

    if(teaspoonInput)
    {
        var litresOutput = teaspoonInput * 0.0049;
        var millilitresOutput = litresOutput * 1000;

        document.getElementById("litres").value = litresOutput.toFixed(4);
        document.getElementById("millilitres").value = millilitresOutput.toFixed(4);

        document.getElementById("cups").value = "";
        document.getElementById("tablespoons").value = "";
        document.getElementById("teaspoons").value = "";
    }
};

function ukConversion() 
{
    var litreInput = parseInt(document.getElementById("litres").value);
    var millilitresInput= parseInt(document.getElementById("millilitres").value)

    if(litreInput)
    {
        var cupOutput = litreInput * 4.22675;
        var tablespoonOutput = litreInput * 67.628;
        var teaspoonOutput = litreInput * 202.884;

        document.getElementById("cups").value = cupOutput.toFixed(4);
        document.getElementById("tablespoons").value = tablespoonOutput.toFixed(4);
        document.getElementById("teaspoons").value = teaspoonOutput.toFixed(4);

        document.getElementById("litres").value = "";
        document.getElementById("millilitres").value = "";

    }

    if(millilitresInput)
    {
        var cupOutput = millilitresInput * 4.22675 / 1000;
        var tablespoonOutput = millilitresInput * 67.628 / 1000;
        var teaspoonOutput = millilitresInput * 202.884 / 1000;

        document.getElementById("cups").value = cupOutput.toFixed(4);
        document.getElementById("tablespoons").value = tablespoonOutput.toFixed(4);
        document.getElementById("teaspoons").value = teaspoonOutput.toFixed(4);

        document.getElementById("litres").value = "";
        document.getElementById("millilitres").value = "";
    }
}

function ukConversionKiloGram()
{
    var kiloInput = parseInt(document.getElementById("kilos").value);
    var gramInput = parseInt(document.getElementById("grams").value);

    if(kiloInput)
    {
        var poundOutput = kiloInput * 2.20462;
        var ounceOutput = kiloInput * 35.274;

        document.getElementById("pounds").value = poundOutput.toFixed(4);
        document.getElementById("ounces").value = ounceOutput.toFixed(4);

        document.getElementById("kilos").value = "";
        document.getElementById("grams").value = "";
    }

    if(gramInput)
    {
        var poundOutput = gramInput / 1000 * 2.20462;
        var ounceOutput = gramInput / 1000 * 35.274;

        document.getElementById("pounds").value = poundOutput.toFixed(4);
        document.getElementById("ounces").value = ounceOutput.toFixed(4);

        document.getElementById("kilos").value = "";
        document.getElementById("grams").value = "";
    }
}

function usConersionOuncePound()
{
    var poundsInput = parseInt(document.getElementById("pounds").value);
    var ouncesInput = parseInt(document.getElementById("ounces").value);

    if(poundsInput)
    {
        var kiloOutput = poundsInput * 0.453592;
        var gramsOutput = poundsInput * 0.453592 * 1000;

        document.getElementById("kilos").value = kiloOutput.toFixed(4);
        document.getElementById("grams").value = gramsOutput.toFixed(4);

        document.getElementById("pounds").value = "";
        document.getElementById("ounces").value = "";
    }
    if(ouncesInput)
    {
        var kiloOutput = ouncesInput * 0.0283495;
        var gramsOutput = ouncesInput * 0.0283495 * 1000;

        document.getElementById("kilos").value = kiloOutput.toFixed(4);
        document.getElementById("grams").value = gramsOutput.toFixed(4);

        document.getElementById("pounds").value = "";
        document.getElementById("ounces").value = "";
    }

}


