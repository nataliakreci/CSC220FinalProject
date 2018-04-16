/* CSC220 Project */
/* Natalia Kreciglowa & Mégane Michaud - April 2018 */

// create a variable to store the images/words informations
var images;

// use fetch to retrieve it, and report any errors that occur in the fetch operation
// once the images have been successfully loaded and formatted as a JSON object
// using response.json(), run the initialize() function
fetch('images_words.json').then(function(response) {
	if(response.ok) {
    	response.json().then(function(json) {
    		images = json;
      		initialize();
    	});
	} 
	else {
		console.log('Network request for houses.json failed with response ' + response.status + ': ' + response.statusText);
  	}
});

function initialize() {
	var displayedImage = document.querySelector('.displayed-img');
	var img = images[0]
	displayedImage.setAttribute('src', 'images/'+img.img);
	displayedImage.setAttribute('id', img.name);
	
	btn = document.querySelector('button');
	
	btn.onclick= function() {
		var input = document.querySelector('.input');
		if (input.value==displayedImage.id){
			alert("correct");
			var index = Math.floor(Math.random() * images.length);
			var img = images[index]
			displayedImage.setAttribute('src', 'images/'+img.img);
			displayedImage.setAttribute('id', img.name);
			input.value= '';
		}
		else{
			alert("try again");
			input.value= '';
		}
	}
}