
var expect = chai.expect;
var assert = chai.assert;

describe('icon change when mouse over and out', function() {
  it('mouse over, img focused', function() {
    img_over(item);

    var bordercolor = document.getElementById("item").style.borderColor;
    var borderwidth = document.getElementById("item").style.borderWidth;

document.getElementById("info1").innerHTML= bordercolor.toString();

document.getElementById("info2").innerHTML= borderwidth.toString();

    assert(bordercolor == 'rgb(175, 190, 255)', 'border color set to purple');
    assert(borderwidth == '10px', 'border width set to 10px');
  });

  it('mouse out, img restored', function() {
    img_out(item);

    var bordercolor = document.getElementById("item").style.borderColor;
    var borderwidth = document.getElementById("item").style.borderWidth;

    assert(bordercolor == 'rgb(255, 255, 255)', 'border color set to white');
    assert(borderwidth == '0px', 'border width set to 0px');
  });
});


describe('show images', function(){
  var loc = 'file:///home/fei/Documents/github/EE461L-sp19-owl-team/Application/plant_app/plants/test/images/';
  it('show transpecos img', function() {

   transpecosfunc();

      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;

//document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_transpecos.jpg','eco_pic is transpecos!');
    //  assert(imgsrc.toString() !== loc+'eco_transpecos.jpg','eco_pic is not transpecos!');
  })
  it('show edwards img', function() {

      edwardsfunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_edwards.png','eco_pic is edwards!');
  })
  it('show crosstimbers img', function() {
      crosstimbersfunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_crosstimbers.png','eco_pic is crosstimbers!');
  })

  it('show southplains img', function() {
      southplainsfunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_southplains.png','eco_pic is southplains!');
  })

  it('show postoaksavanah img', function() {
      postoakfunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_postoaksavanah.jpg','eco_pic is postoaksavanah!');
  })

  it('show pineywoods img', function() {
      pineywoodsfunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_pineywoods.png','eco_pic is pineywoods!');
  })

  it('show blacklandprairie img', function() {
      blacklandprairiefunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_blacklandprairie.jpg','eco_pic is blacklandprairie!');
  })

  it('show marshes img', function() {
      coastfunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_marshes.png','eco_pic is marshes!');
  })

  it('show highplains img', function() {
      highplainsfunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_highplains.png','eco_pic is highplains!');
  })
  it('show rollingplains img', function() {
      rollingplainsfunc();
      const image = document.querySelector("img");
      var imgsrc = document.getElementById("eco_pic").src;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgsrc == loc+'eco_rollingplains.jpg','eco_pic is rollingplains!');
  })

  it('img hidden', function() {
      leave();
      const image = document.querySelector("img");
      var imgvb = document.getElementById("eco_pic").visibility;
  //document.getElementById("eco_text").innerHTML=imgsrc.toString();
      assert(imgvb =='hidden','eco_pic is hidden!');
  })

});
