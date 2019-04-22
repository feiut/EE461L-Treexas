function img_over(item){
	item.style.borderColor = "#57BC90";
}
function img_out(item){
	item.style.borderColor="#FFFFFF";
}

function xlist(button,elementID, variableID) {

	if(document.getElementById(variableID).innerHTML === 'false'){

		var x = document.getElementById(elementID);

		if(x.style.display === "none"){
			x.style.display="block";
			button.style.backgroundColor = "#57BC90";

		}else{
			x.style.display ="none";
			button.style.backgroundColor = "#A5A5AF";
		}

	}
	else{

		button.style.backgroundColor = "#FF6961";
	}
}

function backgroundColorBlue(item){

	item.style.backgroundColor = "#57BC90";
}

function backgroundColorGrey(button){
	button.style.backgroundColor = "#A5A5Af";
}

function img_over(item){
	item.style.borderColor = "#57BC90";
	item.style.borderWidth = "4px";
}
function img_out(item){
	item.style.borderColor = "#FFFFFF";
}

function buttonReverseColor(item){
	if(item.style.backgroundColor === "57BC90"){
		item.style.backgroundColor = "#A5A5Af";
	} else{
		item.style.backgroundColor = "#57BC90"
	}
}
