var number = 89

function compute(){
	code = number * 5;
	zone = code + 3;

	if( zone > 100){
		console.log('The number is less than 100');
	}else{
		console.error('The number is greater than 100');
		console.log('You can start-again');
	}
      }

compute();

var zl_no = window.prompt(' ziology code ');
var depar = window.confirm('Internal or External');

function validate(){
	compute();


	if(zone  == code[7]){
		console.log('OK');
	}else{
		console.error('Invalid Code')
	}  
}


