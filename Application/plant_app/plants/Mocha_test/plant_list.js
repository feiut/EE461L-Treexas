function img_over(item){
	item.style.borderColor = "#57BC90";
}
function img_out(item){
	item.style.borderColor="#FFFFFF";
}



function xlist1(button,elementID) {
	var x = document.getElementById(elementID);
	if(x.style.display === "none"){
		x.style.display="block";
		button.style.backgroundColor = "#57BC90";
	}else{
		x.style.display ="none";
		button.style.backgroundColor = "#A5A5AF";
	}
}