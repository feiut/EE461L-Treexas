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
